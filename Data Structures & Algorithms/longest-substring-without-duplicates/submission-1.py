from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        pos_latest_occurence = defaultdict(lambda: -1)
        dp = [0 for i in range(len(s))]
        for i, elem in enumerate(s):
            max_with_prev = 0
            if i > 0:
                left_pos = max([
                    0,
                    pos_latest_occurence[elem]+1,
                    i-dp[i-1],
                ])
                max_with_prev = i-left_pos+1
            pos_latest_occurence[elem] = i
            dp[i] = max(max_with_prev, 1)
        return(max(dp))
        