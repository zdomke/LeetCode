class Solution:     # 32ms
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        ret = ""
        for i in range(len(sentence)):
            first = sentence[i][0]
            if first.lower() not in 'aeiou':
                sentence[i] = sentence[i][1:] + first
            sentence[i] += 'maa'
            ret += sentence[i]
            for _ in range(i):
                ret += 'a'
            ret += ' '
                
        return ret[:-1]