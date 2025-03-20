import cv2
import matplotlib.pyplot as plt
import numpy as np

# Charger les images
image1 = cv2.imread('../data/images/img1.jpg')
image2 = cv2.imread('../data/images/img2.jpg')

# Convertir les images en noir et blanc
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Calculer les histogrammes
hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])

# Affichage des images originales
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title('Image 1')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title('Image 2')
plt.axis('off')

# Affichage des histogrammes
plt.subplot(2, 2, 3)
plt.plot(hist1, color='gray')
plt.title('Histogramme de l\'image 1')
plt.xlim([0, 256])
plt.axis('off')

plt.subplot(2, 2, 4)
plt.plot(hist2, color='gray')
plt.title('Histogramme de l\'image 2')
plt.xlim([0, 256])
plt.axis('off')

plt.show()
