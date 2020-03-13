# This is python program to compute the sum of squares of numbers less than given number.
# By using single list comprehension.

number = 3                       # taking the input number.

result = sum([n*n for n in range(number)])       # single line command to compute sum.

print("result:",result)