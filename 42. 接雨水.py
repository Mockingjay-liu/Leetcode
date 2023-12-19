import numpy as np
import time
class Solution:
    # def trap(self, height):
    #     answer = 0
    #     highest = max(height)
    #     matrix = []
    #     for i in height:
    #         matrix.append([1]*i+[0]*(highest-i))
    #     matrix = np.transpose(matrix)
    #     for i in range(matrix.shape[0]):
    #         left = 0
    #         while matrix[i][left] != 1:
    #             left += 1
    #         right = len(height) - 1
    #         while matrix[i][right] != 1:
    #             right -= 1
    #         answer += right - left + 1 - int(sum(matrix[i][left:right+1]))
    #     return answer

    # def trap(self, height):
    #     left_height = height.copy()
    #     right_height = height.copy()
    #     for i in range(len(left_height)-1):
    #         if left_height[i] > 0:
    #             j = i+1
    #             while j < len(left_height) and left_height[j] <= left_height[i]:
    #                 left_height[j] = left_height[i]
    #                 j += 1
    #     i = len(right_height)-1
    #     while i > 0:
    #         if right_height[i] > 0:
    #             j = i-1
    #             while j >= 0 and right_height[j] <= right_height[i]:
    #                 right_height[j] = right_height[i]
    #                 j -= 1
    #         i -= 1
    #     answer = sum([min(left_height[i], right_height[i]) for i in range(len(left_height))]) - sum(height)
    #     return answer

    def trap(self, height):
        left_height = np.array(height)
        i = 0
        while i < len(left_height) - 1:
            m = np.argmax(left_height[i + 1:])
            if left_height[i] > 0:
                if left_height[i+1+m] > left_height[i]:
                    j = i+1
                    while j < len(left_height) and left_height[j] < left_height[i]:
                        j += 1
                    for k in range(i+1, j):
                        left_height[k] = left_height[i]
                    i = j
                else:
                    if m > 0:
                        for k in range(i+1, i+2+m):
                            left_height[k] = max(left_height[i+1:i+2+m])
                    i = i+1+m
            else:
                i += 1
        answer = int(sum(left_height)) - sum(height)
        return answer

S = Solution()
start = time.time()
height = []
print(S.trap(height))
print(start, time.time(), time.time()-start)
print()