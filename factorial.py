# This is python program to calculate factorial using recursion.


# This is function for computing the factorial of any positive number without using recursion.

def fact(number):
    if number == 0 or number == 1:
        return 1
    else:
        result = 1
        for n in range(1,number+1):
            result = result * n
        return result
    
input_number = 6
result = fact(input_number)
print(f"factorial of {input_number} (without recursion) is {result}.")

# This is function for computing the factorial of any positive number using recursion.

def recursion_fact(number):
    '''
    This is function which factorial of given number by using recursion method.
      example:
           number = 5
           factorial of number 5! is 120.And 5! = 5*(4*(3*(2*(1!)))) = 5*4!
    '''
    if number == 0:
        return 1
    else:
        return recursion_fact(number-1) * number

input_number = 7
r_result = recursion_fact(input_number)
print(f"factorial of {input_number} (with recursion) is {r_result}.")