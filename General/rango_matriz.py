import numpy
A = numpy.array([[1, -4, 2, -5],
                 [1, -1, 0, 1],
                 [1, 8, -6, 19],
                 [3, 1, 2, 1]])
result = numpy.linalg.matrix_rank(A)

print(f"rank({A}) -> {result}")exit
