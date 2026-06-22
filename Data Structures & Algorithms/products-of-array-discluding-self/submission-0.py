class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def left_prod(cum, i):
            n = len(cum)
            if i == 0:
                return 1
            else:
                return cum[i-1]
        
        def right_prod(cum, i):
            n = len(cum)
            if i == n-1:
                return 1
            else:
                return cum[i+1]
        
        n = len(nums)
        left_cum = [1 for _ in range(n)]
        prod = 1
        for i in range(n):
            prod *= nums[i]
            left_cum[i] = prod
        
        right_cum = [1 for _ in range(n)]
        prod = 1
        for i in range(n-1, -1, -1):
            prod *= nums[i]
            right_cum[i] = prod
        
        output = [
            left_prod(left_cum, i) * 
            right_prod(right_cum, i)
            for i in range(n)
            ]
        
        return output
        