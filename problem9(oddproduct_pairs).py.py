# This is pyhton program to make function to get list of pairs of number whose products is odd.

def oddproduct_pairs(sequence):
    result = []     # for taking the result list which takes tuples of pairs.
    for n in range(len(sequence)):
        for m in range(n+1,len(sequence)):
            product = sequence[n]*sequence[m]   # product

            if product % 2 != 0:          # if product is odd.
                result.append((sequence[n],sequence[m]))
            else:
                pass
    return result          # returning the result list.

nums = [1,2,3,4,5,6,7,8,9,10]       # given number list

output = oddproduct_pairs(nums)       # output

print(output)