# This is python program to make function to find that is any list has distinct elements or not.

def is_distinct(sequence):
    sample_list = list(set(sequence))   # sample list for checking .
    if sequence == sample_list:
        return True
    else:
        return False

original_list = [1,2,3,4,5]        # taking the sequence list.

if is_distinct(original_list):
    print("Distinct.")
else:
    print("Not distinct.")