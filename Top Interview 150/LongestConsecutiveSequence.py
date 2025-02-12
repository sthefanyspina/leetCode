class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        max_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                cur_streak = 1

                while num + cur_streak in num_set:
                    cur_streak += 1

                max_streak = max(max_streak, cur_streak)

        return max_streak
