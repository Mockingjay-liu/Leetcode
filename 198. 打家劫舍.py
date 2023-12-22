class Solution:
    def rob(self, nums):
        l = len(nums)
        answer = [0]*l
        if l == 1:
            return nums[0]
        elif l == 2:
            return max(nums[0], nums[1])
        else:
            answer[0] = nums[0]
            answer[1] = max(nums[0], nums[1])
            for i in range(2,l):
                answer[i] = max(answer[i-1], answer[i-2] + nums[i])
        return answer[-1]


S = Solution()
nums = [2,7,9,3,1]
print(S.rob(nums))


# 1,2,3,4,5,6,7,8,9,10,11

