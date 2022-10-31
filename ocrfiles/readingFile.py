from PIL import Image # to load image
import pytesseract # Image to string library
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
                                     # path of the pytesseract

def imageString(filename):

    text = pytesseract.image_to_string(Image.open(filename))