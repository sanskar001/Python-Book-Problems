# This is python program to examining the element uniqeness inside sequence.
# example: 
    #    seq = [12,3,42,4]
    #    return True           --> unique sequence

    #    seq = [1,2,4,66,2]
    #    return False          --> Non unique sequence.

# NON RECURSIVE METHOD:

# def unique(seq):
#     for n in range(len(seq)-1):
#         for m in range(n+1,len(seq)):
#             if seq[n] == seq[m]:
#                 return False            # for Non unique.
#     return True         # for unique.

# sample_seq = [1,2,3,2,5]        # example 
# print(unique(sample_seq))

##########################################################################

# RECURSIVE METHOD:
def runique(seq):
    if len(seq) == 1:        # number of element is 1 --> UNIQUE
        return True
    else:
        if seq[0] in seq[1:]:
            return False
        else:
            return runique(seq[1:])
            
        
sample_seq = [1,2,3,4,5]

if runique(sample_seq):
    print("UNIQUE")
else:
    print("NON UNIQUE")    