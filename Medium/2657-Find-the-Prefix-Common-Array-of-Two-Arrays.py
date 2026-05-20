class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s1 = set()
        s2 = set()
        res = []
        for i in range(len(A)):
            s2.add(B[i])
            s1.add(A[i])
            c = len(s1 & s2)
            res.append(c)
        return res
