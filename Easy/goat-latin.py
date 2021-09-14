class Solution:     # 36ms
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            first = sentence[i][0]
            if first.lower() not in 'aeiou':
                sentence[i] = sentence[i][1:] + first
            sentence[i] += 'maa'
            for _ in range(i):
                sentence[i] += 'a'
                
        return " ".join(sentence)