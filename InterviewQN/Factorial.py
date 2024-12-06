def Factorial(x):
    if x==1:
        return x
    else:
        return x * Factorial(x-1)
Result = Factorial(6)
print(Result)