#Factorial of number
#Input: A positive integer, N
#Output: The Factorial of N
# (1) Factorial <- 1
# (2) for i from 1 to N
# (3)   factorial <- factorial * i
# (4) end FL
# (5) return factorial

def factorial(n):
    result = 1

    for i in range(1,n+1):
        result *= i

    return result

n = 7
print(factorial(n))