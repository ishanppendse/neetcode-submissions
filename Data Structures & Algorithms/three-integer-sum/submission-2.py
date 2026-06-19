from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        ans = []
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                if len(dic[-(nums[i]+nums[j])]) > 0:
                    for elem in dic[-(nums[i]+nums[j])]:
                        if elem != i and elem != j and elem > j:
                            candidate = [nums[i], nums[j], nums[elem]]
                            if sorted(candidate) not in ans:
                                ans.append(sorted(candidate))
        
        return ans



        """
        [-1, 0, 1, 2, -1, -4]
        i = 0
        j = 1

        dic = {1: [2]}
        elem = 2

        """