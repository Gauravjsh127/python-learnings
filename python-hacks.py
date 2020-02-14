# initialize array

# 1D
lis_1D = [1 for i in range(0,10)]
print(lis_1D)

# 2D
cols = 2
rows = 4
lis_2D = [[1 for i in range(0,cols)] for i in range(0,rows)]
print(lis_2D)

# ASCII Value to charcters and Vice versa
ch = 'a'
print(ch)
print(ord(ch))
num = 98
print(num)
print(chr(num))

# Sorting list of lists by the first element of each sub-list
lis = [[1, 4, 7], [3, 6, 9], [2, 59, 8]]
print(lis)
lis.sort()
print(lis)
lis2 = sorted(lis, key=lambda x: x[1])
print(lis)
print(lis2)

