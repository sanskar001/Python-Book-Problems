# This is python program to find out minimum  and maximum value inside the given list.
# without using the built in min() and max() function.
# So, there is only way to find out min and max value inside list, by using the sorting.

def minmax(number_list):
    number_list.sort()          # This is self sorting function.(built-in).
    return number_list[0],number_list[len(number_list)-1]

nums = [12,34,65,3,56,2387,46,0,-1]
print(minmax(nums))
