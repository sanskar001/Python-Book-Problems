# This is python program to make list which contain the dot products of two given list.

def dot_products(list1,list2):
    result = [i*j for i , j in zip(list1,list2)]
    return result

vector1 = [1,3,5]      # vector --> [x,y,z]
vector2 = [10,2,7]

vector3 = dot_products(vector1,vector2)   # resultant dot products vector.

print(vector3)