words = ["Hello","Alaska","Dad","Peace"]
# words = ["adsdf","sfd"]
# words =["asdfghjkl","qwertyuiop","zxcvbnm"]
keys = ["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"]
wordMap = {}
ans = []
countLetter = 0
for word in words:
    for i in word :
        if i in keys[0]:
            if word not in wordMap:
                wordMap[word] = 0 
                countLetter+=1
            elif wordMap[word] == 0:
                wordMap[word] = 0
                countLetter+=1
            else:
                break
        elif i in keys[1]:
            if word not in wordMap:
                wordMap[word] = 1 
                countLetter+=1
            elif wordMap[word] == 1:
                wordMap[word] = 1
                countLetter+=1
            else:
                break
        elif i in keys[2]:
            if word not in wordMap:
                wordMap[word] = 2
                countLetter+=1
            elif wordMap[word] == 2:
                wordMap[word] = 2
                countLetter+=1
            else:
                break
    if countLetter == len(word):
        ans.append(word)
    countLetter=0
print(ans)