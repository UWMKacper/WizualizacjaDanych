import numpy as np

# def wrapper()


# a = np.array([0, 1])
# print(a)
#
# b = np.arange(1,5,1,dtype='float64')
# print(b)
#
# print(type(a))
# print(type(b))
#
# print(a.dtype)
# print(b.dtype)
#
# c = b.astype('int64')
# print(c)
#
# print(c.shape)
#
# d = np.array([np.arange(2), np.arange(2)])
# print(d)
# print(d.shape)
# print(d.ndim)
#
# zera = np.zeros((5,5), dtype='int64')
# print(zera)
#
# jedynka = np.ones((3,3), dtype='int64')
# print(jedynka)
#
# pusta = np.empty((2,2))
# print(pusta)
# print(pusta[1][1])
#
# a = np.arange(1,5,0.5)
# print(a)
#
# b = np.linspace(1, 5, 5, endpoint=False)
# print(b)
#
# c, d = np.indices((5,5))
# print("-"*10)
# print(c)
# print("-"*10)
# print(d)
# print("-"*10)
# e=np.indices((5,3))
# print(e)
# print("-"*10)
# print(e[0][1][1])
#
# f,g = np.mgrid[0:5, 0:5]
# print(f)
# print("-"*10)
# print(g)
# print("-"*10)
# h = np.diag([a for a in range(5)],-1)
# print(h)
# h = np.diag([a for a in range(5)])
# print(h)
#
# i = np.fromiter(range(5), dtype='int32')
# print(i)
#
# marcin = b'Marcin'
# mar = np.frombuffer(marcin, dtype='S6')
# print(mar)
# marcin2 = 'Marcin'
# mar_1 = np.array(list(marcin))
# print(mar_1)
# mar_2 = np.array(list(marcin2))
# print(mar_2)
# print(mar_1.dtype)
# print(mar_2.dtype)
#
# mar_4 = np.fromiter(marcin, dtype='U1')
# print(mar_4)
#
# a = np.ones((2,2))
# b = np.ones((2,2))
#
# c = a + b
#
# print(c)

# a = np.arange(10)
# print(a)

# s = slice(2,7,2)
# print(a[s])
# s = range(2, 7, 2)
# print(a[s])
# print(a[2:7:2])

# print(a[1:5])
b = np.arange(25)
# print(b)
mat = b.reshape((5,5))
print(mat)
# print(mat[1:2])
#
# print(mat[1,0:5])
# print(mat[:,0:5])
print("\n")
print(mat[2:5, 1:3])
print("\n")
print(mat[2:4, 0:5])
#
# a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
# print(a)
# rows = np.array([[0, 0], [3, 3]])
# cols = np.array([[0, 2], [0, 2]])
# y = a[rows, cols]
# print(y)
