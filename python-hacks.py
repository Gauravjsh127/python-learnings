

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort()
# print vowels
print('Sorted list:', vowels)

# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
# sort the vowels
vowels.sort(reverse=True)
# print vowels
print('Sorted list (in Descending):', vowels)

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

# Sorting list of lists by the second element of each sub-list
lis2 = sorted(lis, key=lambda x: x[1])
print(lis)
print(lis2)


# Python Lambda
# A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.


# lambda arguments : expression


x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))
