class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            Sanagram={}
            Tanagram={}
            for i in range(len(s)):
                if s[i] not in Sanagram:
                    Sanagram[s[i]]=1
                else:
                    Sanagram[s[i]]+=1
                if t[i] not in Tanagram:
                    Tanagram[t[i]]=1
                else:
                    Tanagram[t[i]]+=1
            for i in t:
                if i not in s:
                    return False
                if Sanagram[i] != Tanagram[i]:
                    return False
            return True
        return False

sol=Solution()
# print(sol.isAnagram("anagram","nagaram"))
# print(sol.isAnagram("aacc","ccac"))
print(sol.isAnagram("rat","car"))


# for i in range(len(s)):
#                 if t[i] not in anagram:
#                     anagram[t[i]]=1
#                 else:
#                     anagram[t[i]]+=1
#             for i in s:
#                 if (i in t) and s.count(i) != anagram[i]:
#                     return False
#             return True