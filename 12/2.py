class Matrix:
    def __init__(self, data):
        if len(data) != 3 or any(len(row) != 3 for row in data):
            raise ValueError("Only 3x3 matrices are supported.")
        self.data = data

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only add another Matrix.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only multiply with another Matrix.")
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        return Matrix(result)

    def transpose(self):
        result = [[self.data[j][i] for j in range(3)] for i in range(3)]
        return Matrix(result)

    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.data])


if __name__ == "__main__":
    matrix1 = Matrix([[8, 2, 5], [3, 4, 2], [0, 6, 9]])
    matrix2 = Matrix([[9, 5, 7], [4, 5, 4], [3, 4, 3]])

    print("Matrix 1:")
    print(matrix1)

    print("\nMatrix 2:")
    print(matrix2)

    print("\nMatrix Addition:")
    print(matrix1 + matrix2)

    print("\nMatrix Multiplication:")
    print(matrix1 * matrix2)

    print("\nTranspose of Matrix 1:")
    print(matrix1.transpose())