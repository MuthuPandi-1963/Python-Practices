# def majorityElement(nums:list):
#     max={}
#     majority=0
#     value=[]
#     for i in nums:
#         if i not in max:
#             max[i]=1
#         else:
#             max[i]+=1
#     print(max)
#     for key in max.keys():
#         if max[key]>=majority:
#             value.append(key)
#             majority=max[key]
#     print(value)

# majorityElement([3,2,3])
# majorityElement([1])
# majorityElement([1,2])

def palindrome(s):
    n=len(s)
    start=0
    end=n-1
    while(start<=end):
        if s[start]==s[end]:
            start+=1
            end-=1
        else:
            return False
    return True
print(palindrome("abba"))
print(palindrome("abca"))
print(palindrome("abbaba"))
print(palindrome("abcbcba"))