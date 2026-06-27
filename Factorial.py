def factorial(n):
    fact = 1 
    for i in range (1,n+1):
        fact *= i 
    return fact

# n = int(input("Enter the Number : "))
# print("The Factorial of " , n , "is",factorial(n))



# RECURSIVE FACTORIAL

def Fact(n):
    if n == 0 or n ==1 :
        return 1 
    return n * factorial(n-1)

print(factorial(5))

