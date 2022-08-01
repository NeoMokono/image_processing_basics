from skimage import color
from skimage import io
read_image = io.imread('image_in\Picture1.jpg')
img = color.rgb2gray(read_image)
io.imsave("image_out\skimage-greyscale.png",img)


print("skimage successfuly completed conversion ----------")