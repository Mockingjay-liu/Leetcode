class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 1:
            return 1
        answer = 0
        i = 0
        while i < len(s)-1:
            j = i
            length = 0
            while j < len(s):
                if len(set(s[i:j+1])) == len(s[i:j+1]):
                    j += 1
                    length += 1
                else:
                    i += s[i:j+1].index(s[j])+1
                    break
            answer = max(answer, length)
            if j == len(s):
                i += 1
        return answer

S = Solution()
s = "dvdf"
print(S.lengthOfLongestSubstring(s))