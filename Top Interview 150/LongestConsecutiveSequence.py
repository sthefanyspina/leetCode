class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        max_streak = 1
        cur_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                cur_streak += 1
            else:
                max_streak = max(max_streak, cur_streak)
                cur_streak = 1
        
        return  max(max_streak, cur_streak)
