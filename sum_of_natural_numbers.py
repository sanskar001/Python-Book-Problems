# This is first recursion problem for computing the sum of n natural number.


def recursion_sum(number):
    '''
    This is recursive function for calculating the sum of n natural numbers.
      example:
         number = 5
         sum = ((((1 )+ 2 )+ 3 )+ 4 )+ 5 = 15
    '''
    if number == 1:
        return 1
    else:
        return recursion_sum(number-1) + number

input_number = 10                         # sample input number
result = recursion_sum(input_number)      # result for taking the sum of given natural number.

print("sum of {0} natural number is {1}.".format(input_number,result))