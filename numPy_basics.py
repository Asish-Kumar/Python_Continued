import numpy as np

a =  np.array([[1,2,3],[4,5,6]])
print(a)
print(np.vstack(a))
np.random.normal
# print(np.sum(a,axis=1))
# b = np.array([1,2,3,4,4,7,5,5,66,54])
# np.split(b,5)
print(a[0,2])
# ==================================================================================

# import numpy as np
# from matplotlib import pyplot as plt
#
# # numpy arrays have more functionalities than typical lists in python
#
# face_img = plt.imread("face.jpg")
#
# print(type(face_img))
# # print(repr(face_img))
# print(np.shape(face_img))
# print(face_img)
# half_face_left = face_img[:,:211,:]
# plt.imshow(face_img)
# plt.show()
# plt.imshow(half_face_left)
# plt.show()

# ====================================================================================

# try:
#     np.arange(10)
# except ValueError:
#     print("Except")
# else:
#     print("Other errors")
# finally:
#     print("Something")

# ====================================================================================

# array1 = np.array((1, 2, 3, 4, 5), dtype=np.int16)  # specify datatype of elements of the array
# print(type(array1))
# print(array1)
# print(repr(array1))
#
# no_of_row = 2
# no_of_column = 3
# array2 = np.zeros((no_of_row, no_of_column))  # create an 2-D array of all elements as zeros
# array3 = np.ones((no_of_row, no_of_column, 2))  # create a 3-D array of all elements as ones
# print(array2, "\n\n\n", array3)
#
# # shape of an array is the number of elements in each dimension of an array
