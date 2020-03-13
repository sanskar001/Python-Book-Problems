# This is python program to compute sum of squares of all the odd numbert smaller than given number.
# By using single line list comprehension and builtin sum() function.

number = 10                      # taking the input number.

result = sum([n*n for n in range(number) if n%2!=0])       # single line command to compute sum.

print("result:",result)