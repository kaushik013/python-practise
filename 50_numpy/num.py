import numpy as np

a = np.array([1, 2, 3,4,5,6,7,8,9,10,11,12,13,14,15])

# 1d array
print(a)
print(type(a))

# 2d array
ab = a.reshape(3, 5)
print(ab)


# 3d array
abc = a.reshape(5,3,1)
print(abc)

i = abc.reshape(-1)
print(i)

print(np.identity(3))


print(np.linspace(1,10))

print(np.linspace(1,10,6))

print(np.identity(5))

print(np.sum(5+5))

print(np.sqrt([10]))

print(np.array([1,2,3,4]))

print(np.max([10,11,12,12,13,13]))

abc = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]],[[16,17,18],[19,20,21],[22,23,24],[25,26,27],[28,29,30]]])

print(abc[::,3::])
