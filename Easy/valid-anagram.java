// First solution. Slower than second solution

// class Solution {
//     public boolean isAnagram(String s, String t) {
//          if(s.length() != t.length())
//             return false;

//         int[] map = new int[26];
//         for(int i = 0; i < s.length(); i++){
//             map[s.charAt(i) - 'a']++;
//             map[t.charAt(i) - 'a']--;
//         }

//         Arrays.sort(map);
//         return (map[0] == 0 && map[25] == 0);
//     }
// }

class Solution {
    public boolean isAnagram(String s, String t) {
        char[] arrS = s.toCharArray();
        char[] arrT = t.toCharArray();

        if(arrS.length != arrT.length){
            return false;
        }

        Arrays.sort(arrS);
        Arrays.sort(arrT);
        for(int i = 0; i < arrS.length; i++){
            if(arrS[i] != arrT[i]){
                return false;
            }
        }
        return true;
    }
}