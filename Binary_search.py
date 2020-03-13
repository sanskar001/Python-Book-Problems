# This is python program to understand the concept of recursion.
# This is python program to build binary search.

number = [12,5,2,78,6,9,44,3,54,45,23,11,1]
print("normal number sequence:",number)
sorted_number = sorted(number)
print("sorted number sequence:",sorted_number)

# This is function defination for making the binary searching.

def binary_search(sequence,target,start,end): 
    # here sequence should contains elements of number type.
    mid = (start + end) // 2

    if sequence[mid] == target:
        return mid
        
    elif target < sequence[mid]:
        return binary_search(sequence,target,start,mid-1)
    
    elif target > sequence[mid]:
        return binary_search(sequence,target,mid+1,end)
    

index = binary_search(sorted_number,54,0,len(sorted_number)-1)
print("index value(sorted sequence):",index)
print("index value(normal sequence):",number.index(sorted_number[index]))