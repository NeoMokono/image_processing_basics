from PIL import Image
img = Image.open('image_in\Picture1.jpg').convert('L')
img.save('image_out\pil-greyscale.png')