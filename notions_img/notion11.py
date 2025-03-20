import cv2
import matplotlib.pyplot as plt
import numpy as np

# Charger les images
image1 = cv2.imread('../data/images/img1.jpg')
image2 = cv2.imread('../data/images/img2.jpg')

# Convertir les images en noir et blanc
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Affichage des images originales
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')
plt.axis('off')

# Affichage des images en niveaux de gris
plt.subplot(2, 2, 3)
plt.imshow(gray_image1, cmap='gray')
plt.title('Image 1 en niveaux de gris')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(gray_image2, cmap='gray')
plt.title('Image 2 en niveaux de gris')
plt.axis('off')

plt.show()
