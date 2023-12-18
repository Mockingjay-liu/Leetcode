# 23:00
class Solution:
    def longestConsecutive(self, nums):
        nums = list(set(nums))
        nums = sorted(nums)
        if nums == []:
            return 0
        count = 1
        max_count = 1
        for i in range(0, len(nums)-1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
                max_count = max(count, max_count)
            else:
                max_count = max(count, max_count)
                count = 1
        return max_count

S = Solution()
nums = []
print(S.longestConsecutive(nums))
print()

# 23:14