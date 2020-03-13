# This is python program to find out whether given string is palindrome or non palindrome.

# SIMPLE METHOD:

# def string_palindrome(string):

#     for n in range(len(string) // 2):
#         if string[n] != string[len(string)-(n+1)]:
#             return False

#     return True

##############################################################################

# RECURSIVE METHOD:

def string_palindrome(string, start, stop):

    if start < stop-1:               

        if string[start] != string[stop-1]:         # CHECKING FOR PALINDROME.

            return False                         # NOT PALINDROME

        string_palindrome(string,start+1,stop-1)

    return True                                       # PALINDROME.

   
input_string = "racecar"

print(string_palindrome(input_string,0,len(input_string)))