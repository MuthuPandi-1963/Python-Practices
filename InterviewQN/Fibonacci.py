def Fibonacci(n):
    if n==0:
        return n
    elif n==1:
        return n
    else:
        print(Fibonacci(n-1)+Fibonacci(n-2))
        return Fibonacci(n-1)+Fibonacci(n-2)
  
# print(Fibonacci(5))
# print(Fibonacci(6))
# print(Fibonacci(7))
# print(Fibonacci(8))
# print(Fibonacci(9))
# print(Fibonacci(15))
Fibonacci(4)

# def add(x,y):
#     # print(x+y)
#     # return x+y
#     return 0

# sum=0
# for i in range(5):
#     sum+=add(1,2)
#     print(sum)
