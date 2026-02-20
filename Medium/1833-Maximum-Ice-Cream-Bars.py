class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = 0
        i = 0
        costs.sort()
        while i < len(costs):
            if coins - costs[i] >= 0:
                res += 1
                coins = coins - costs[i]
            else:
                break
            i += 1
        return res
