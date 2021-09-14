class Solution:     # 46ms
    def toGoatLatin(self, sentence: str) -> str:
        sentence = sentence.split()
        ret = ""
        for i in range(len(sentence)):
            char = sentence[i][0]
            if char.lower() in 'aeiou':
                ret += char
            ret += sentence[i][1:]
            if char.lower() not in 'aeiou':
                ret += char
            ret += 'maa'
            for _ in range(i):
                ret += 'a'
            ret += ' '
                
        return ret[:-1]