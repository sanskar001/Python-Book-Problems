# This is python program to REVERSE THE STRING BY USING RECURSION.

# SIMPLE METHOD:
# def reverse_string(string):
#     result = list(string)

#     for n in range(len(string) // 2):

#         result[n], result[len(string)-(n+1)] = result[len(string)-(n+1)], result[n]
    
#     return "".join(result)


#########################################################################

# RECURSIVE METHOD:

def reverse_string(string_list,start,stop):
    
    if start < stop-1:
        string_list[start], string_list[stop-1] = string_list[stop-1], string_list[start]
        reverse_string(string_list,start+1,stop-1)
    

input_string = "HELLO"

input_string_list = list(input_string)
reverse_string(input_string_list,0,len(input_string))
output_string = "".join(input_string_list)

print(f"Reverse of given input string is \"{output_string}\".")

