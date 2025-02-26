class Solution:
    def checkTwoStrings(self,a,b):
        count = 0
        for i in a :
            if i in b:
                count+=1
                
        return True if len(a)==count else False

    def groupAnagrams(self, strs):
        wordMapping ={}
        ans = []
        outIndex =0 
        sol =Solution()
        for word in strs:
            wordList = (list(map(lambda x : sol.UniqueKey(ord(x)-97),word)))
            res = 1
            for i in wordList: res*=i
            if(res not in wordMapping):
                wordMapping[res] = outIndex
                ans.append([word])
                outIndex+=1
            else:
                if sol.checkTwoStrings(ans[wordMapping[res]][0],word):
                    ans[wordMapping[res]].append(word)
                else:
                    ans.append([word])
                    outIndex+=1
        return ans
    
    def UniqueKey(self,s):
        letterArray = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 
                       31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 
                       73, 79, 83, 89, 97, 101 ]
        return letterArray[s]
