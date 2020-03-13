# This is python program to make vector class.

class vector:
    def __init__(self,dimension):
        self.v = [0]*dimension
    
    def __len__(self):
        return len(self.v)
    
    def __getitem__(self,index):
        return self.v[index]
    
    def __setitem__(self,index,value):
        self.v[index] = value
    
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError("Dimension must be same!")
        else:
            result = vector(len(self))
            for n in range(len(self)):
                result[n] = self[n] + other[n]
            return result
    
    def __sub__(self,other):
        if len(self) != len(other):
            raise ValueError("Dimension must be same!")
        else:
            result = vector(len(self))
            for n in range(len(self)):
                result[n] = self[n] - other[n]
            return result
    
    def __mul__(self,other):
        if len(self) != len(other):
            raise ValueError("Dimension must be same!")
        else:
            result = 0
            for n in range(len(self)):
                result = result + (self[n] * other[n])
            return result

    def __neg__(self):
        result = vector(len(self))
        for n in range(len(self)):
            result[n] = -self[n]
        return result
    

    def __eq__(self,other):
        return self.v == other.v
    
    def __ne__(self,other):
        return self.v != other.v
    
    def __str__(self):
        return f"< {str(self.v)[1:-1]} >"
    

# outside world of class vector.
v1 = vector(3)
v2 = vector(3)
v1[0] = 10
v1[1] = 11
v1[2] = 20
# and 
v2[0] = 11
v2[1] = 33
v2[2] = 55

print("v1:",v1)
print("v2:",v2)
v3 = v1 + v2
print("v1 + v2:",v3)
v4 = v1 - v2
print("v1 - v2:",v4)
v5 = -v1
print("negative v1:",-v2)
v6 = v1*v2                      # dot product between the vector v1 and v2
print("v1.v2:",v6)