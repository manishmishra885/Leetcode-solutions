def Reverse_int(n):
    n =  235
    temp = n 
    rev = 0
    while n > 0 :
        digit = n % 10 
        rev = rev * 10 + digit 
        n //= 10 
    if temp == rev :
       return True
    return False

def CheckReverseString(n):
    if n == n[::-1]:
        return True
    return False

print(CheckReverseString("manish"))


# RECURSIVE PALINDROME  STRING: 
def palindrome(n):
    #base case :
    if len(n) <= 1 :
        return True 
    #now checking first and last character 

    if n[0] != n[-1]:
        return False
    
    return palindrome(n[1:-1]) # string slicing used , iteratring character from index 1 to -1 , means 2nd char to 2nd last char
    
print(palindrome("madam"))