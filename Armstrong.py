# def arm(n):
#     total = 0 
#     digits = str(n)
#     power = len(n)
#     for d in digits:
#         total += int(d)**power

#         return total == n 
# print(arm(153)) # True

'''with the math and while loop '''

def arm(n):
  orignal_variable = n 
  total = 0 
  temp = n 
  power = 0 
  while temp > 0 :
    temp //= 10
    power += 1 

  while temp > 0 :
    digit = temp % 10 
    total += digit ** power 
    temp //= 10 #remove the last digit 

    return total == orignal_variable
print(arm(153)) # True
