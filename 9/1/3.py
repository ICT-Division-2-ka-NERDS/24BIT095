def matrix():
    def create_array(x, y, z, value):
        return [[[value] * z for _ in range(y)] for _ in range(x)]
    
    array = create_array(6, 4, 3, 0)
    print(array)

matrix()
