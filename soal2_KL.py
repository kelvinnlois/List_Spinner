# Soal 2
# Kelvin Lois

A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print("\n")
print('List_awal = ')
print(A)
print("\n")

# Fungsi counterClockwise
def counterClockwise(A):
    B = [[0]*4, [0]*4, [0]*4, [0]*4]
    for i in range(4):
        for j in range(4):
            B[3-i][j] = A[j][i]
    return B

# Penggunaan Fungsi counterClockwise
print('Output :')
print(counterClockwise(A))
