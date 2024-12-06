def longestPalindrome(s):
    n=len(s)
    left =0
    right =n-1
    
    while(left<=right):
        if(s[left] == s[right]):
            left+=1
            right-=1
        else:
            
    
longestPalindrome(s = "babad")