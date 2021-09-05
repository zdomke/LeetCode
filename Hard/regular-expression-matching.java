// class Solution {
//     public boolean isMatch(String s, String p) {
//         int indS = 0;
//         int indP = 0;
        
//         while(indS < s.length() && indP < p.length()){
//             if(indP < (p.length() - 1) && p.charAt(indP + 1) == '*'){
//                 if(p.charAt(indP) == '.'){
//                     indS = s.length() - 1;
//                 }
//                 while(indS < s.length() && s.charAt(indS) == p.charAt(indP)){
//                     indS++;
//                 }
//                 indP += 2;
//             } else if(p.charAt(indP) == '.' || (s.charAt(indS) == p.charAt(indP))){
//                 indS++;
//                 indP++;
//             } else {
//                 return false;
//             }
//         }
//         return (indS >= s.length() && indP >= p.length());
//     }
// }

// class Solution {        // 639ms
//     public boolean isMatch(String s, String p) {
//         if(s.length() == 0 && p.length() == 0){
//             return true;
//         } else if(s.charAt(0) == p.charAt(0) || p.charAt(0) == '.'){
//             if(p.length() >= 2 && p.charAt(1) == '*'){
//                 int i = 0;
//                 boolean found = false;
//                 while(i <= s.length() && (s.charAt(i) == p.charAt(0) || p.charAt(0) == '.'))
//                     found |= isMatch(s.substring(i++), p.substring(2));
//                 return found || isMatch(s.substring(i), p.substring(2));
//             }
//             return isMatch(s.substring(1), p.substring(1));
//         } else {
//             return false;
//         }
//     }
// }

// class Solution {        // 66ms (somehow changed to 180ms after)
//     public boolean isMatch(String s, String p) {
//         if(s.charAt(0) == p.charAt(0) || p.charAt(0) == '.'){
//             if(p.length() >= 2 && p.charAt(1) == '*'){
//                 int i = 0;
//                 while(i <= s.length() && (s.charAt(i) == p.charAt(0) || p.charAt(0) == '.'))
//                     if(isMatch(s.substring(i++), p.substring(2)))
//                         return true;
//             }
//             return isMatch(s.substring(1), p.substring(1));
//         } else {
//             return (s.length() == 0 && p.length() == 0);
//         }
//     }
// }

class Solution{         // 136ms
    public boolean isMatch(String s, String p){
        if(p.isEmpty()) return s.isEmpty();
        boolean first = (!s.isEmpty() && (s.charAt(0) == p.charAt(0) || p.charAt(0) == '.'));
        
        if(p.length() >= 2 && p.charAt(1) == '*'){
            return (isMatch(s, p.substring(2)) || (first && isMatch(s.substring(1), p)));
        } else {
            return first && isMatch(s.substring(1), p.substring(1));
        }

    }
}