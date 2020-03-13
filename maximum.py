# This is python program to find the maximum number inside any sequence using recursion.
# example:
    #    seq = [2,4,2,63,673,77,8]
    #    maximum number = 673
import time 

# NON RECURSIVE WAY:
# i1 = time.clock()            # START

# def maximum(seq):
#     max = seq[0]
#     for n in range(1,len(seq)):
#         if max < seq[n]:
#             max = seq[n]
#     return max

# l1 = time.clock()            # STOP
sample_seq = [2,5,1,7,855,45,7,23,89]            # SAMPLE SEQUENCE.

# result = maximum(sample_seq)

# print(f"(simple method) maximum number inside given sample sequence:{result}")
# print(f"(simple method) Time elapsed: {l1-i1}")
#####################################################################################

# RECURSIVE WAY:
i2 = time.clock()           # START
def rmaximum(seq,stop):
    if stop-1 == 0:
        return seq[0]
    else:
        if rmaximum(seq,stop-1) < seq[stop-1]:
            return seq[stop-1]
        else:
            return rmaximum(seq,stop-1)

l2 = time.clock()
result_2 = rmaximum(sample_seq,len(sample_seq))

print(f"(recursive method) maximum number inside sample sequence is: {result_2}")
print(f"(recursive method) Time elapsed:{l2-i2}")