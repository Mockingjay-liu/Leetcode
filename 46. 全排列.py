class Solution:
    def permute(self, nums):
        if len(nums) == 1:
            return [[nums[0]]]
        else:
            x = []
            for i in self.permute(nums[:-1]):
                for j in range(len(i)+1):
                    x.append(i[:j]+[nums[-1]]+i[j:])
            return x

S = Solution()
nums = [1]
print(S.permute(nums))