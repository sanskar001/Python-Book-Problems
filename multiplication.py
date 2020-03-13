# This is python program to find multiplication between two numbers UNSING RECUSION.

# SIMPLE METHOD:

def mul(m,n):
    '''
    mul(num1,num2)
    return num1 * num2
    '''
    result = 0
    if m != 0:
        for i in range(n):
            result = result + m
    
    return result


print(f"SIMPLE METHOD result: {mul(0,4)}")

#######################################################################

# METHOD 2:
# FIRST RECURSIVE METHOD:

def rmul(m,n):
    if n == 0 or m == 0:
        return 0
    else:
        return rmul(m,n-1) + m

print(f"(RECURSIVE METHOD) result:{rmul(15,6)}")

####################################################################

# METHOD 3:
# MORE EFFICIENT RECURSIVE METHOD:
def rmultiplication(m,n):
    if n == 0 or m == 0:
        return 0
    elif n == 1:
        return m
    else:
        factor = n//2
        if n % 2 == 0:
            return rmultiplication(m,factor) * 2
        else:
            return rmultiplication(m,factor) + rmultiplication(m,n-factor)

print(f"(MORE EFFICIENT RECURSIVE METHOD) result: {rmultiplication(10,3)}")

