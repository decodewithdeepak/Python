# Image manipulation refers to the process of altering the visual appearance of an image. 
# Python offers several libraries for image manipulation and processing, including:
# 1. PIL (Python Imaging Library)
# 2. OpenCV (Open Source Computer Vision)
# 3. Scikit-image 
# 4. Matplotlib
# 5. Scipy 

# Image Manipulation using PIL
# PIL is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats.
# To install PIL, use the following command:
# pip install Pillow

# To use PIL, import the Image module from the PIL library:
from PIL import Image

# Opening an image
img = Image.open("image.jpg")

# Saving an image
img.save("new_image.jpg")

# Displaying an image
img.show()

# Creating a new image
new_img = Image.new("RGB", (200, 200), "white")
new_img.save("blank_image.jpg")

# Image properties
# 1. Format: To get the format of an image, use the format attribute.
# 2. Size: To get the size of an image, use the size attribute.
# 3. Mode: To get the mode of an image, use the mode attribute.

img = Image.open("image.jpg")
print("Image format:", img.format)
print("Image size:", img.size)
print("Image mode:", img.mode)


# Image manipulation operations
# 1. Resize: To resize an image, use the resize() method:
img = Image.open("image.jpg")
img = img.resize((400, 400)) # 400x400 pixels
img.save("resized_image.jpg")

# 2. Rotate: To rotate an image, use the rotate() method:
img = Image.open("image.jpg")
img = img.rotate(90)
img.save("rotated_image.jpg")

# 3. Crop: To crop an image, use the crop() method:
img = Image.open("image.jpg")
img = img.crop((100, 100, 400, 400))
img.save("cropped_image.jpg")

# 4. Flip: To flip an image, use the transpose() method:
img = Image.open("image.jpg")
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.save("flipped_image.jpg")

# 5. Convert: To convert an image to grayscale, use the convert() method:
img = Image.open("image.jpg")
img = img.convert("L") # L stands for Luminance
img.save("grayscale_image.jpg")

# 6. Filter: To apply a filter to an image, use the filter() method:
from PIL import ImageFilter

img = Image.open("image.jpg")
img = img.filter(ImageFilter.GaussianBlur(15))
img.save("blurred_image.jpg")

# 7. Thumbnail: To create a thumbnail of an image, use the thumbnail() method:
img = Image.open("image.jpg")
img.thumbnail((200, 200))
img.save("thumbnail_image.jpg")

# 8. Composite: To composite an image, use the composite() method:
img1 = Image.open("image1.jpg")
img2 = Image.open("image2.jpg")
img1 = img1.resize((400, 400))
img2 = img2.resize((400, 400))
img = Image.composite(img1, img2, img1) # img1 is the mask
img.save("composite_image.jpg")

# 9. Blend: To blend two images, use the blend() method:
img1 = Image.open("image1.jpg")
img2 = Image.open("image2.jpg")
img1 = img1.resize((400, 400))
img2 = img2.resize((400, 400))
img = Image.blend(img1, img2, 0.5) # 0.5 is the alpha value (transparency)
img.save("blended_image.jpg")

# 10. Paste: To paste an image on another image, use the paste() method:
img1 = Image.open("image1.jpg")
img2 = Image.open("image2.jpg")
img1 = img1.resize((400, 400))
img2 = img2.resize((400, 400))
img1.paste(img2, (0, 0))
img1.save("pasted_image.jpg")

# 11. Text: To add text to an image, use the text() method:
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open("image.jpg")
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 16)
draw.text((0, 0), "Hello World", (255, 255, 255), font=font)
img.save("text_image.jpg")

# 12. Histogram: To create a histogram of an image, use the histogram() method:
img = Image.open("image.jpg")
histogram = img.histogram()
print(histogram)

# 13. Copy: To copy an image, use the copy() method:
img = Image.open("image.jpg")
img_copy = img.copy()
img_copy.save("copied_image.jpg")


# Image Manipulation using OpenCV
# OpenCV is a library of programming functions mainly aimed at real-time computer vision.
# To install OpenCV, use the following command:
# pip install opencv-python

# To use OpenCV, import the cv2 module:
import cv2

# Opening an image
img = cv2.imread("image.jpg")

# Saving an image
cv2.imwrite("new_image.jpg", img)

# Displaying an image
cv2.imshow("Image", img)
cv2.waitKey(0) # waits for a key to be pressed before closing the image
cv2.destroyAllWindows() # closes all the opened windows

# Creating a new image
import numpy as np

img = np.zeros((200, 200, 3), np.uint8)
cv2.imwrite("blank_image.jpg", img)

# Image properties
# 1. Shape: To get the shape of an image, use the shape attribute.
# 2. Size: To get the size of an image, use the size attribute.
# 3. Type: To get the type of an image, use the dtype attribute.

img = cv2.imread("image.jpg")
print("Image shape:", img.shape)
print("Image size:", img.size)
print("Image type:", img.dtype)


# Image manipulation operations
# 1. Resize: To resize an image, use the resize() method:
img = cv2.imread("image.jpg")
img = cv2.resize(img, (400, 400))
cv2.imwrite("resized_image.jpg", img)

# 2. Rotate: To rotate an image, use the rotate() method:
img = cv2.imread("image.jpg")
height, width = img.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
img = cv2.warpAffine(img, rotation_matrix, (width, height))
cv2.imwrite("rotated_image.jpg", img)

# 3. Crop: To crop an image, use the crop() method:
img = cv2.imread("image.jpg")
img = img[100:400, 100:400]
cv2.imwrite("cropped_image.jpg", img)

# 4. Flip: To flip an image, use the flip() method:
img = cv2.imread("image.jpg")
img = cv2.flip(img, 1)
cv2.imwrite("flipped_image.jpg", img)

