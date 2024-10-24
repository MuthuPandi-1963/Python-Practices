# n=5
# for i in range(n):
#     s=" "
#     for j in range(n-i-1):
#         s+=" "
#     for k in range(2*i+1):
#         s+="*"
#     print(s)
# n=5
# for i in range(n):
#     s=" "
#     for j in range(i):
#         s+=" "
#     for k in range((2*n-1)-(2*i)): 
#         s+="*"
#     print(s)


def Palindrome(s):
    n=len(s)
    count=0
    for i in range(n):
        if s[i]==s[n-1-i] and i<n//2:
            count+=1
        elif n//2==i:
            break
    if count==n//2:
         print("Its a Palindrome") 
    else: 
        print("Its not a Palindrome")

Palindrome("ababa")
Palindrome("abbaabba")
Palindrome("madam")
Palindrome("agshdkf")

