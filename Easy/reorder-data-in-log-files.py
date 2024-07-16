class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig = []
        let = []
        
        for l in logs:
            if l.split()[1].isdigit():
                dig.append(l)
            else:
                let.append(l)
        
        let.sort(key=lambda l: l.split()[0])
        let.sort(key=lambda l: l.split()[1:])
        return let + dig