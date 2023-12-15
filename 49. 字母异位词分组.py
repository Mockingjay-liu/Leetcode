# 20:27

class Solution:
    def groupAnagrams(self, strs):
        r = []
        d = {}
        for i in strs:
            if ''.join(sorted(i)) not in d:
                d[''.join(sorted(i))] = [i]
            else:
                d[''.join(sorted(i))].append(i)
        for k in d:
            r.append(d[k])
        return r

S = Solution()
input = ["a"]
x = S.groupAnagrams(input)
print()

# 20:40