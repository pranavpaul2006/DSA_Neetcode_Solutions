class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1)
        for i in range(len(s2) - length + 1):
            res = s2[i:i+length]
            if Counter(res) == Counter(s1):
                return True
        return False 





            