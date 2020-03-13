# This is python program to make list comprahension syntax to  produce the list: [0,6,12,20,30,42,56,72,90]

number = 9 # input number.
output_list = [(n*n)+n for n in range(number)]  # single line list comprehrension.
print("output list:",output_list)