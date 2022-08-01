import cv2
img = cv2.imread("image_in\Picture1.jpg")
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("image_out\opencv-greyscale.png",gray_image)

print("cv2 successfuly completed conversion ----------")
