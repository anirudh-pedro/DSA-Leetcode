class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # self.res = float('inf')
        # n = len(costs)
        
        # def back(i,a,b,cost1,cost2,n):
        #     if a > n//2 or b > n//2:
        #         return
        #     if a == b == n // 2:
        #         self.res = min(self.res,cost1+cost2)
        #         return
        #     back(i+1,a+1,b,cost1+costs[i][0],cost2,n)
        #     back(i+1,a,b+1,cost1,cost2+costs[i][1],n)
        # back(0,0,0,0,0,n)
        # return self.res

        costs.sort(key = lambda a : a[0] - a[1])
        res = 0
        l = len(costs) // 2
        for i in range(l):
            res += costs[i][0]
            res += costs[l+i][1]
        return res
