class Matrix:
    def __init__(self, row, col):
        self.data = [[0 for _ in range(col)] for _ in range(row)]
        self.row = row
        self.col = col
    def __str__(self):
        line = ''
        for i in range(self.row):
            for j in range(self.col):
                line +=f'{self.data[i][j]} '
            line += '\n'
        return line
    def add(self, other):
        res = Matrix(self.row,self.col)
        for i_row in enumerate(other.data):
            for i_col in enumerate(i_row[1]):
                res.data[i_row[0]][i_col[0]] = i_col[1] + self.data[i_row[0]][i_col[0]]
        return res
    def subtract(self, other):
        res = Matrix(self.row,self.col)
        for i_row in enumerate(other.data):
            for i_col in enumerate(i_row[1]):
                res.data[i_row[0]][i_col[0]] =self.data[i_row[0]][i_col[0]] - i_col[1]
        return res
    def multiply(self, other):
        res = Matrix(self.row,other.col)
        count = 0
        for i_row in range(self.row):
            for i in range(other.col):
                for j in range(other.row):
                    count += self.data[i_row][j] * other.data[j][i]
                res.data[i_row][i] = count
                count = 0
        return res
    def transpose(self):
        res = Matrix(self.col,self.row)
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                res.data[j][i] = self.data[i][j]
        return res
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1.add(m2))

print("Вычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
print(m1.multiply(m3))

print("Транспонирование матрицы 1:")
print(m1.transpose())
