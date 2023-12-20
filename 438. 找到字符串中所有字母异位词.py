class Solution:
    def findAnagrams(self, s, p):
        answer = []
        p_dict = {}
        for i in set(p):
            p_dict[i] = p.count(i)
        l = len(p)
        for i in range(len(s) - l + 1):
            s_sub = s[i:i+l]
            flag = 0
            for j in set(s_sub):
                if j not in p_dict:
                    break
                elif s_sub.count(j) != p_dict[j]:
                    break
                flag += 1
            if flag == len(p_dict):
                answer.append(i)
        return answer

S = Solution()
s = "cbaebabacd"
p = "abc"
print(S.findAnagrams(s, p))