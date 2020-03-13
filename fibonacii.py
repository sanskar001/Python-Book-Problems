# This is python program to make fibonacci series using recursion method.

def fib(number):
    if number <= 0:
        raise ValueError("Number must be greater than zero.")
    elif number == 1 or number == 2:
        return 1
    else:
        return fib(number-1) + fib(number-2)

# for making the list of fibonacci series given number of length.        
result = [fib(n) for n in range(1,11)] 
 
print(str(result)[1:-1])

#############################################################

#  Without using the recursion.

# def fib(number):
#     if number == 1:
#         print(0)
#     else:
#         print(0)
#         prev = 0
#         current = 1
#         for n in range(1,number):
#             print(current)
#             prev, current = current, current + prev