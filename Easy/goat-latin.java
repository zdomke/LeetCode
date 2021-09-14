class Solution {        // 7ms
    public String toGoatLatin(String sentence) {
        Set<Character> vowel = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        StringBuilder ret = new StringBuilder();

        int j = 0, i = 0;
        for(String w : sentence.split(" ")){
            ret.append(' ' + (vowel.contains(w.charAt(0)) ? w : w.substring(1) + w.charAt(0)) + "ma");
            for(j = 0, i++; j < i; j++){
                ret.append('a');
            }
        }
        return ret.toString().substring(1);
    }
}