# This is python problem to find out number is even or odd .

# Method 1
def is_even1(number):
    flag = True
    for n in range(number):
        if flag == True:
            flag = False
        else:
            flag = True
    return flag


# Method 2
def is_even2(number):
    if number % 2 ==0:
        return True
    else:
        return False

# Method 3
def is_even3(number):
    if int(number / 2) * 2 == number:
        return True
    else:
        return False

# Method 4
# By using the bitwise operation.
# number is 5.
# 5 --> 00000101 and we alerady know that 1 is odd number.
# 1 --> 00000001
# (00000101) & (00000001) == 00000001 (odd)
# 6 --> 00001100
# (00000110) & (00000001) == 00000000 (even)
# Here the bit_number is in bytes eg. 101(5), 111(7) etc.
def is_even4(bit_number):
    if number & 1 == 0:
        return True
    else:
        return False


# Checking
num = 101
if is_even3(num):
    print(num,"is even.")
else:
    print(num,"is odd.")
