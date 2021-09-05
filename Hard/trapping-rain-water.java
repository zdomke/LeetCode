// class Solution{		// 297ms
// 	public int trap(int[] height){
// 		int sum = 0;
// 		int min;

// 		for(int start = 0; start < (height.length - 1); start++){
// 			boolean endFound = false;
// 			for(int x = 0; x < height[start]; x++){
// 				if(height[start] - x > height[start + 1]){
// 					for(int end = (start + 2); end < height.length; end++){
// 						if((height[start] - x) <= height[end]){
// 							endFound = true;
// 							min = Math.min(height[start] - x, height[end]);
// 							int[] temp = Arrays.copyOfRange(height, (start + 1), end);
// 							for(int i : temp) sum += min - i;
// 							break;
// 						}
// 					}
// 					if(endFound) break;
// 				}
// 			}
// 		}

// 		return sum;
// 	}
// }

// class Solution{		// 177ms
// 	public int trap(int[] height){
// 		int sum = 0;

// 		for(int start = 0; start < (height.length - 1); start++){
// 			while(height[start] > height[start + 1]){
// 				for(int end = (start + 2); end < height.length; end++){
// 					if(height[start] <= height[end]){
// 						sum += (end - start - 1);
// 						break;
// 					}
// 				}
// 				height[start]--;
// 			}
// 		}
// 		return sum;
// 	}
// }

// class Solution{		//419ms		(given brute force algorithm)
// 	public int trap(int[] height){
// 		int sum = 0;

// 		for(int i = 0; i < height.length; i++){
// 			int left_max = 0;
// 			int right_max = 0;

// 			for(int j = 0; j < i; j++)
// 				left_max = (left_max < height[j]) ? height[j] : left_max;
// 			for(int j = i; j < height.length; j++)
// 				right_max = (right_max < height[j]) ? height[j] : right_max;

// 			sum += Math.max(Math.min(left_max, right_max) - height[i], 0);
// 		}
// 		return sum;
// 	}
// }

// class Solution{		// 4ms 		(given dynamic programming solution)
// 	public int trap(int[] height){
// 		int sum = 0;
// 		int[][] heights = new int[height.length][2];
// 		int left_max = 0;
// 		int right_max = 0;

// 		for(int i = 0, j = (height.length - 1); i < height.length; i++, j--){
// 			left_max = (left_max < height[i]) ? height[i] : left_max;
// 			right_max = (right_max < height[j]) ? height[j] : right_max;

// 			heights[i][0] = left_max;
// 			heights[j][1] = right_max;
// 		}
// 		for(int i = 0; i < height.length; i++){
// 			sum += Math.max(Math.min(heights[i][0], heights[i][1]) - height[i], 0);
// 		}
// 		return sum;
// 	}
// }

// class Solution{		// 5ms		(given Stack solution)
// 	public int trap(int[] height){
// 		int sum = 0;
// 		int ind = 0;

// 		Deque<Integer> st = new ArrayDeque<Integer>();
// 		while(ind < height.length){
// 			while(!st.isEmpty() && (height[ind] > height[st.peek()])){
// 				int top = st.pop();
// 				if(st.isEmpty()) break;

// 				int dist = ind - st.peek() - 1;
// 				int bound = Math.min(height[ind], height[st.peek()]) - height[top];
// 				sum += dist * bound;
// 			}
// 			st.push(ind++);
// 		}
// 		return sum;
// 	}
// }

class Solution{		// 1ms	(given 2 pointer solution)
	public int trap(int[] height){
		int left = 0, left_max = -1;
		int right = height.length - 1, right_max = -1;
		int sum = 0;

		while(left < right){
			if(height[left] < height[right]){
				if(height[left] > left_max){
					left_max = height[left++];
				} else {
					sum += left_max - height[left++];
				}
			} else {
				if(height[right] > right_max){
					right_max = height[right--];
				} else {
					sum += right_max - height[right--];
				}
			}
		}

		return sum;
	}
}