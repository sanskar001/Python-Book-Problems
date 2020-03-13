# This is python program to understand the Euclidean norm fot computing the length of vector.

def norm(vector_list):
    sum = 0
    for n in vector:
       sum = sum + n*n
    result = sum**(0.5)
    return result

vector = [3,4,5,6]       # v = [v1,v2,v3,v4,.......]    
output = norm(vector)
print(f"output:{output:.2f}")      # printing the output.