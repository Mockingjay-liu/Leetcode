# 23:00
class Solution:
    def longestConsecutive(self, nums):
        if nums == []:
            return 0
        nums = sorted(list(set(nums)))
        last = nums[0]
        count = 1
        max_count = 1
        for i in nums[1:]:
            if last + 1 == i:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 1
            last = i
        max_count = max(count, max_count)
        return max_count

S = Solution()
nums = [0,3,7,2,5,8,4,6,0,1]
print(S.longestConsecutive(nums))
print()

# 23:14