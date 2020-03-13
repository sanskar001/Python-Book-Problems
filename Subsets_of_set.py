# This is python program to find ALL THE SUBSETS of given sets or POWER OF SETS.

###################################################################

# SIMPLE METHOD:

# sample_list = [1,2,3,4]

# for a in range(len(sample_list)):        # LOOP 1
#     print(sample_list[a])
    
#     for b in range(a+1,len(sample_list)):      # LOOP 2
#         print(sample_list[a],",",sample_list[b])
        
#         for c in range(b+1,len(sample_list)):         # LOOP 3
#             print(sample_list[a],",",sample_list[b],",",sample_list[c])
            
#             for d in range(c+1,len(sample_list)):                 # LOOP 4
#                 print(sample_list[a],",",sample_list[b],",",sample_list[c],",",sample_list[d])
                

# print("NULL")

# print(f"Number of all subsets of set {1,2,3,4} is {2 ** 4}")

#########################################################################################

# RECURSIVE METHOD:

# import time

# i = time.clock()                  # CLOCK START.

def power_set(seq,other):

    if len(seq) == 1:            # if size of sequence is 1 

        other.append(seq[0])      # then first element append to list
        print(set(other))         # printing the list as set.

        other.remove(seq[0])       # removing currently appended value from list.

    else:                          # otherwise  -->
         for n in range(len(seq)):

             other.append(seq[n])         # element are appending into list.
             print(set(other))

             power_set(seq[n+1:],other)   # calling function for next part of list.

             other.remove(seq[n])         # removing the currentlty added element from list.


# l = time.clock()               # CLOCK STOP.


sample_set = {1,2,3,4}
power_set(list(sample_set),[])
print("{Null} \n")

print(f"Number of SUBSETS of given set is: {2**len(sample_set)}.")
# print(f"Elapsed time:{l-i}")