from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def crawl(i, dic):
            count = 1
            while dic[i]:
                i += 1
                count += 1
            return count

        if len(nums) == 0:
            return 0
        dic = defaultdict(int)
        for i in nums:
            dic[i-1] = True
        ans = 1
        for i in nums:
            ans = max(ans, crawl(i, dic))
        return ans
        