# This is python program to understand the linear recursion concept.
# LINEAR RECURSION.
##############################################################################

# PROGRAM 1:
# for getting the sum of sequence elements by using concept of linear recursion.

# def seq_sum(seq,num):
#     if num == 0:
#         return 0
#     else:
#         return seq_sum(seq,num-1) + seq[num-1]

# sample_sequence = [11,4,15,23,10,9,3,8]
# result = seq_sum(sample_sequence,len(sample_sequence))
# print(f"sum of given sample sequence is :{result}")

# another_sequence = [12,24,45,23,1,6,7]
# print(f"sum of given another sequence is :{seq_sum(another_sequence,len(another_sequence))}")

######################################################################################

# PROGRAM 2:
# This is python program for reversing the given sequence by using the recursion.
# def reverse_seq(seq,start,stop):
#     if start < stop - 1:
#         seq[start], seq[stop-1] = seq[stop-1], seq[start]
#         reverse_seq(seq,start+1,stop-1)


# sample_sequence = [11,4,15,23,10,9,3,8]
# print(f"Given sample sequence :{sample_sequence}")
# reverse_seq(sample_sequence,0,len(sample_sequence))


# print(f"reverse of given sample sequence is: {sample_sequence}")

####################################################################################################
# This is python program to calculate the any power of any number.
# USING THE RECURSION.
# print(f"example : 2 raise to power 10 is {pow(2,10)}")

# def rpower(num,pnum):
#     '''
#     rpower(number , power_number)
#     '''
#     if pnum == 0:
#         return 1
#     else:
#         return rpower(num,pnum-1) * num

# result = rpower(3,4)
# print(f"3 raise to power 4 is equal to :{result}")

#################################################################################3
# EFFICIENT WAY OF CALCULATING THE POWER USING RECURSION.
# def rpower(num,pnum):
#     if pnum == 0:
#         return 1
#     else:
#         partial = rpower(num,pnum // 2)
#         result = partial * partial
#         if pnum % 2 == 1:
#             result = result * num
#         return result

# result = rpower(3,5)
# print(f"3 raise to power 5 is equal to :{result}")