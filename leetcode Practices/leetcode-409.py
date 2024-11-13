def longestPalindrome(s):
    hashValue={}
    count=0
    odd=[]
    for i in s:
        if i not in hashValue:
            hashValue[i]=1
        else:
            hashValue[i]+=1
    for key in hashValue.keys():
        if hashValue[key]%2==0:
            count+=hashValue[key]
        else:
            odd.append(hashValue[key])
    lenODD=len(odd)
    if lenODD!=0:
        count+=(sum(odd)-lenODD)+1
    print(count)

longestPalindrome("aAAaAAbbccc")
longestPalindrome("AaBbBbCcDdEeEe")
longestPalindrome("aabbccdde")
longestPalindrome("bb")