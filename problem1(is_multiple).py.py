# this is python program to make function to find the number is multiple or not.

# This is  function for finding the multiple.
def is_multiple(n,m):
    if n % m == 0:
        return True
    else:
        return False

number1 = 200     # number for testing the nultiple.
number2 = 10      # number for which multiple is checking.

if is_multiple(number1,number2):

    print(number1,"is  multiple of",number2)
else:
    
    print(number1,"is not multiple of",number2)
