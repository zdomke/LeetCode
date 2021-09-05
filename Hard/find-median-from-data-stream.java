// class MedianFinder {

//     /** initialize your data structure here. */
//     ArrayList<Double> arrL;
//     ArrayList<Double> arrR;
//     boolean odd;
//     double x;

//     public MedianFinder() {
//         this.arrL = new ArrayList();
//         this.arrR = new ArrayList();
//         this.odd = false;
//         this.x = null;
//     }
    
//     public void addNum(int num) {
//         if(x == null){
//             x = num;
//         } else if(num <= x){
//             arrL.add((double)num);
//         } else {
//             arrR.add((double)num);
//         }
//         odd = !odd;
//     }
    
//     public double findMedian() {
//         if((odd && arrL.size() != arrR.size()) || 
//             (!odd && (arrL.size() != (arrR.size() - 1) || arrL.size() != (arr.size() + 1)))){
//             ArrayList<Double> temp = new ArrayList(arrL);
//             temp.addAll(arrR);
//             temp.add(x);
//             Collections.sort(temp);
//             int ind = temp.size() / 2;
//             x = temp.get(ind);
//             arrL = new ArrayList(temp.subList(0, ind));
//             arrR = new ArrayList(temp.subList(ind + 1, temp.size()));
//         }
//         if(odd) return x;
//         if(arrL.size() > arrR.size()) return (x + arrL.get(arrL.size() - 1)) / 2;
//         return (x + arrR.get(0)) / 2;
//     }
// }

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */

class MedianFinder{     // 89ms
    PriorityQueue<Integer> maxQ;
    PriorityQueue<Integer> minQ;
    public MedianFinder(){
        this.maxQ = new PriorityQueue<>(Collections.reverseOrder());
        this.minQ = new PriorityQueue<>();
    }

    public void addNum(int num){
        if(minQ.size() == 0 || num > minQ.peek()){
            minQ.add(num);
        } else {
            maxQ.add(num);
        }
        
        if(maxQ.size() == (minQ.size() + 1)){
            minQ.add(maxQ.poll());
        } else if((maxQ.size() + 2) == minQ.size()){
            maxQ.add(minQ.poll());
        }
    }

    public double findMedian(){
        if(maxQ.size() == minQ.size())
            return (maxQ.peek() + minQ.peek()) / 2.0;
        return (double)minQ.peek();
    }
}