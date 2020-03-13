# This is python program to understand the concept of recursion and
# To find out HCF of two given numbers.


def recursion_hcf(number1,number2):
    '''
    This is function to find out the HIGHEST COMMAN FACTOR 
     or GREATEST COMMAN FACTOR using recursion.
      example: num1 = 300
         num2 = 45
         num1 ! = num2
         num1 > num2
         so,
         300 = 45 * 6 + 30
         and 
         45 = 30 * 1 + 15
         and 
         30 = 15 * 2 + 0
         because 30 % 15 = 0
         so,
         HCF : 15 
    '''
    if number1 == number2:
        return number1

    elif number1 % number2 == 0:
        return number2

    elif number2 % number1 == 0:
        return number1
    
    elif number1 > number2:
        return recursion_hcf(number2,number1 % number2)
    
    elif number2 > number1:
        return recursion_hcf(number2,number2 % number1)


input_number1 = 2000
input_number2 = 455
hcf_result = recursion_hcf(input_number1,input_number2)
print(f"HCF of {input_number1} and {input_number2} is equal to {hcf_result}")