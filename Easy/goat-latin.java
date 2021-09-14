class Solution {        // 8ms
    public String toGoatLatin(String sentence) {
        String ret = "";
        String[] arr = sentence.split(" ");
        
        for(int i = 0; i < arr.length; i++){
            if(!"aeiouAEIOU".contains("" + arr[i].charAt(0))){
                ret += arr[i].substring(1);
                ret += arr[i].charAt(0);
            } else {
                ret += arr[i];
            }
            ret += "maa";
            for(int j = 0; j < i; j++){
                ret += 'a';
            }
            ret += ' ';
        }
        return ret.substring(0, ret.length() - 1);
    }
}