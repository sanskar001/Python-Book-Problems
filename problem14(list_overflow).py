# This is python program to understand exception handling for list data type.

data_list = [1,2,3,4,5]    # given list.
index_number = 5           # index value 
value = 15                 # value at index place of list.

try:
    data_list[index_number] = value
    print(data_list)

except Exception as e:
    print("Don't try buffer oerflow attacks in python.")
    print("Error:",e)