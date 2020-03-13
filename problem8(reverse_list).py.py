def reverse(list_data):
    reverse_list = []
    for n in range(len(list_data)):
        reverse_list.append(list_data[-(n+1)])
    return reverse_list

nums = [1,2,3,4,5]
print("nums list:",nums)
print("reverse list:",reverse(nums))