from PIL import Image # to load image
import pytesseract # Image to string library
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
                                     # path of the pytesseract

filter = 0

img = cv2.imread("image.png") # Image load
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # color change

if filter == 0:
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1] # Image quality made b etter for detection

else:
    gray = cv2.medianBlur(gray, 3) # to medium blur

filename = "{}.png".format(os.getpid()) # to save a temporary file
cv2.imwrite(filename, gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)

print(text)

cv2.imshow("Image", img)
cv2.imshow("Gray", gray)
cv2.waitKey(0)