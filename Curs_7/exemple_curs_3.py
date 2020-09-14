class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "Vector2D ({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        # resultx = self.x + other.x
        # resulty = self.y + other.y
        # result = Vector2D(resultx, resulty)
        # return result
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        # resultx = self.x - other.x
        # resulty = self.y - other.y
        # result = Vector2D(resultx, resulty)
        # return result
        return Vector2D(self.x - other.x, self.y - other.y)
        
    def __mul__(self, other):
        return (self.x + other.x)*(self.y + other.y)
        
if __name__ == "__main__":
    v1 = Vector2D(10, 78)
    v2 = Vector2D(14, 56)
    print(v1)
    print(v2)
    v_sum = v1 + v2
    print(v_sum)
    v_sub = v1 - v2
    print(v_sub)
    v_mul = v1 * v2
    print(v_mul)