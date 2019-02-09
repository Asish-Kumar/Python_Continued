import cv2
import face_recognition_models

img1 = cv2.imread("C:\\Users\\Asish.LENOVO-IDEAPAD-\\Pictures\\python_use\\face.jpg", -1)  # reading file as grayscale
# 0: grayscale, 1: rgb, -1: rgba

cv2.imshow('Image_Show', img1)


img2 = cv2.imread("C:\\Users\\Asish.LENOVO-IDEAPAD-\\Pictures\\python_use\\face.jpg", -1)  # reading file as grayscale
cv2.imshow("Img2_show", img2)
cv2.waitKey(0)