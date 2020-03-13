# This is python program for solving the problem 1.4
# for computing the sum of squares of all the number smaller than given number.

def square_sum(number):        # number is positive number.  
    sum = 0                    # for taking the sum of all square
    for n in range(number):
        sum = sum + n*n
    return sum

result = square_sum(7)          # for taking the result .
print("result:",result)