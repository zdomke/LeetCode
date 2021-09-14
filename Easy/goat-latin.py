class Solution:     # 45ms
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        ret = ""
        for i in range(len(sentence)):
            first = sentence[i][0]
            if first.lower() not in 'aeiou':
                sentence[i] = sentence[i][1:] + sentence[i][0]
            sentence[i] += 'maa'
            for _ in range(i):
                sentence[i] += 'a'
            ret += sentence[i] + ' '
                
        return ret[:-1]