# #arrays using numpy
# import numpy as np
# numbers=[1, 2, 3, 4, 5]
# result = []
# for i in numbers:
#     result.append(i*1000)
# print(result)

# #1d array
# a=np.array([[1, 2, 3, 4, 5]])
# print(a)
# print(a*100)

# #2d array
# b=np.array([[1,2,3],[4,5,6]])
# print(b)
# # rows and columns
# c=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(c)

# #3d array
# d = np.array([
#     [[1,2,3],[4,5,6]],
#     [[7,8,9],[10,11,12]]
# ])
# print(d.shape)   
# print(d)
# # access elements in 3d array
# d.shape
# [2,3,3]
# #3 layers 4 rows 5 columns
# d=np.ones((3,4,5))
# print(d)
# # create 2x2x3 array of ones
# e=np.ones((2,2,3))
# print(e)

# # array[[layer],[row],[column]]
# f=d[1,0,2]
# print(f)
# #slicing 1d array
# v=d[0,0]
# print(v)
# # slicing 1d array to get all first elements from each layer
# z=d[:,0,0]
# print(z)

# # slicing 2d array
# w=d[:,0,:]
# print(w)
# #slicing 2d array to get all first rows from each layer
# s = np.arange(24)
# s = s.reshape(2,3,4)
# print(s.shape)
# print(s)

# # math operations in 3d array
# print(d+10)
# print(d*2)
# print(d**2)
# #sum of all elements in 3d array
# m=np.sum(d)
# m=np.sum(d,axis=0)
# m=np.sum(d,axis=1)
# m=np.sum(d,axis=2)
# print(m)

# # image data
# image=np.random.randint(0,255,(64,64,3))
# # 64*64 image with 3 color channels (RGB)
# r=image[:,:,0] #red channel
# g=image[:,:,1] #green channel
# b=image[:,:,2] #blue channel
# print(r)
# print(g)
# print(b)


