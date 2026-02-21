class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime = set()
        def priming(n):
            if n <= 1:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True

        for i in range(1,32):
            if priming(i):
                prime.add(i)
        res = 0
        for i in range(left,right+1):
            k = bin(i)[2:].count("1")
            if k in prime:
                res += 1
        return res
