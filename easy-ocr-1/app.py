import easyocr
import cv2
from matplotlib import pyplot as plt
import numpy as np

IMAGE_PATH = 'img/lorem6.png'

reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext(IMAGE_PATH)

text = ''
for result in results:
    text += result[1] + ' '

print(text)

""" result

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread(IMAGE_PATH)
img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
img = cv2.putText(img, text, top_left, font, .5, (0, 0, 0), 2, cv2.LINE_AA)
plt.imshow(img)
plt.show() """
