from sys import stdin


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, mt=[]):
        self.mt = mt[:]

    def __str__(self):
        result = self.mt[:]
        for i in range(len(result)):
            c = '\t'.join(str(result[i]).strip("[]").split(', '))
            result[i] = c
        return '\n'.join(result)

    def __add__(self, other):
        if (len(self.mt) == len(other.mt))\
                and (len(self.mt[0]) == len(other.mt[0])):
            result = Matrix()
            for i in range(len(self.mt)):
                temp = []
                for j in range(len(self.mt[0])):
                    temp.append(self.mt[i][j] + other.mt[i][j])
                result.mt.append(temp)
            return result
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        result = Matrix()
        for i in range(len(self.mt)):
            temp = []
            for j in range(len(self.mt)):
                temp.append(other * self.mt[i][j])
            result.mt.append(temp)
        return result

    __rmul__ = __mul__

    def size(self):
        return len(self.mt), len(self.mt[0])

    def transpose(self):
        result = Matrix()
        for i in range(len(self.mt[0])):
            result.mt.append([])
        for i in range(len(self.mt)):
            for j in range(len(self.mt[0])):
                result.mt[j].append(self.mt[i][j])
        self.mt = result.mt
        return self

    @staticmethod
    def transposed(other):
        result = Matrix()
        for i in range(len(other.mt[0])):
            result.mt.append([])
        for i in range(len(other.mt)):
            for j in range(len(other.mt[0])):
                result.mt[j].append(other.mt[i][j])
        return result


exec(stdin.read())
