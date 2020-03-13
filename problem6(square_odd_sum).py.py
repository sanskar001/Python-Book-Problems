# This is python program for solving the problem 1.6
# for computing the sum of squares of alll the odd number smaller than given number.

def square_sum(number):        # number is positive number.  
    sum = 0                    # for taking the sum of all square.
    for n in range(number):
        if n%2!=0:
            sum = sum + n*n
        else:
            pass
    return sum

number = 10
result = square_sum(number)          # for taking the result.
print("result:",result)