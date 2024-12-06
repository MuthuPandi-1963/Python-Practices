class Solution:
    def clearDigits(self, s: str) -> str:
        s=list(s)
        n=len(s)
        left =0
        right=n-1
        order=0
        while(order <= right):
            if s[order].isdigit():
                left=order-1
                while(left>=0):
                    if(s[left].isalpha()):
                        s[left]=s[order]
                        order+=1
                        break
                    else:
                        left-=1
            else:
                order+=1
                
        m=""
        for i in s:
            if(i.isalpha()):
                m+=i
        print(m)
        return (m)
            
        
        
sol = Solution()
sol.clearDigits("cd34")
sol.clearDigits("abc")
sol.clearDigits("c5c")
sol.clearDigits("gbysb5")

# s= "1234"
# print(list(s))

