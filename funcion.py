
def summation(whole_Number):
  add_Digit = 0
  while True:
# we get the last digit of the number 
    extNum = whole_Number % 10
# we remove the last figure 
    whole_Number //= 10
#is stored
    add_Digit += extNum
    if whole_Number == 0:      
     return add_Digit
  
  
 