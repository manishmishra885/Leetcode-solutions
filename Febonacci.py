n = 10
a=0 
b=1

for i in range (n):
    print(a, end = " ")
    c = a+b 
    a = b 
    b = c 


# RECURSIVE 
def febo (n):
    if n <= 1 :
        return n 
    
    return febo(n-1) + febo (n-2)
# for i in range (7):
    # print(febo(i), end = " ")