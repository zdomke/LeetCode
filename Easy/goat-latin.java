class Solution {        // 17ms
    public String toGoatLatin(String sentence) {
        String ret = "";
        Set<Character> vowel = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        
        int j = 0, i = 0;
        for(String w : sentence.split(" ")){
            ret += ' ' + (vowel.contains(w.charAt(0)) ? w : w.substring(1) + w.charAt(0)) + "ma";
            for(j = 0, i++; j < i; j++){
                ret += 'a';
            }
        }
        return ret.substring(1);
    }
}