class Solution:     # 24ms
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        for i in range(len(sentence)):
            first = sentence[i][0]
            if first.lower() not in 'aeiou':
                sentence[i] = sentence[i][1:] + first
            sentence[i] += 'maa' + ('a' * i)
                
        return " ".join(sentence)