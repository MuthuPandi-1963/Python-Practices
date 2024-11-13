# def FirstUniqueStr(s):
#     for i in range(len(s)):
#         if s[i] not in s[i+1::]:
#             return(s[i])       
# FirstUniqueStr("loveleetcode")

def StudentGrade():
    subjects=["Tamil","English","Maths","Science","Social"]
    marks=[int(input(f"Enter a {subjects[i]} Mark : ")) for i in range(len(subjects))]
    print(marks)
    total=sum(marks)
    percentage=total/5
    print(total)
    if ((total>=0) and (total<=500)):
        if(500>=total>=400):
            print("Your Grade is A")
        elif(399>=total>=300):
            print("Your Grade is B")
        elif(299>=total>=200):
            print("Your Grade is C")
        elif(199>=total>=0):
            print("Your Grade is D")
    else:
        print("Invalid Mark Please Check the Mark")
# StudentGrade()

# from random import randint
import random


def generateOTP(n):
    otp=""
    for i in range(n):
        s=random.randint(0,9)
        otp+=str(s)
    print(otp)

generateOTP(4)
generateOTP(6)