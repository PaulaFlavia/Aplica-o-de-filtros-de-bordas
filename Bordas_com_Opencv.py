import cv2
from matplotlib import pyplot as plt
import numpy as np
import requests
url = "https://cdn.pixabay.com/photo/2017/07/24/19/57/tiger-2535888_1280.jpg"
r = requests.get(url)
with open('test.jpg', 'wb') as f:
  f.write(r.content)
  

img = cv2.imread('test.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray, (3,3), 0)

sobelx = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
plt.figure(figsize=(18,19))
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('original')
plt.axis('off')

plt.figure(figsize=(18,19))
plt.subplot(222)
plt.imshow(sobelxy, cmap='gray')
plt.title('Sobel X Y')
plt.axis('off')

plt.figure(figsize=(18,19))
plt.subplot(223)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X ')
plt.axis('off')

plt.figure(figsize=(18,19))
plt.subplot(224)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.axis('off')

