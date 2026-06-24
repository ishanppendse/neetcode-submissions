from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        desired = defaultdict(int)
        desired[k] += 1
        cum = 0
        ans = 0
        for i in nums:
            cum += i
            ans += desired[cum]
            desired[cum+k] += 1
        return ans