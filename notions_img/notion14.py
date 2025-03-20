import cv2
import matplotlib.pyplot as plt
import numpy as np

# Charger les images
image1 = cv2.imread('../data/images/img1.jpg')
image2 = cv2.imread('../data/images/img2.jpg')
image3 = cv2.imread('../data/images/img3.jpg')

# Convertir les images en noir et blanc
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

# Calculer les histogrammes
hist1 = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([gray_image2], [0], None, [256], [0, 256])
hist3 = cv2.calcHist([gray_image3], [0], None, [256], [0, 256])

# Créer une grille de sous-tracés
fig, axs = plt.subplots(3, 2, figsize=(10, 15))

# Afficher les images en niveaux de gris
axs[0, 0].imshow(gray_image1, cmap='gray')
axs[0, 0].set_title('Image 1')
axs[0, 0].axis('off')

axs[1, 0].imshow(gray_image2, cmap='gray')
axs[1, 0].set_title('Image 2')
axs[1, 0].axis('off')

axs[2, 0].imshow(gray_image3, cmap='gray')
axs[2, 0].set_title('Image 3')
axs[2, 0].axis('off')

# Afficher les histogrammes
axs[0, 1].plot(hist1, color='gray')
axs[0, 1].set_title('Histogramme de l\'image 1')
axs[0, 1].set_xlabel('Niveaux de gris')
axs[0, 1].set_ylabel('Nombre de pixels')
axs[0, 1].set_xlim([0, 256])
axs[0, 1].grid()
axs[0, 1].legend(['Histogramme'])

axs[1, 1].plot(hist2, color='gray')
axs[1, 1].set_title('Histogramme de l\'image 2')
axs[1, 1].set_xlabel('Niveaux de gris')
axs[1, 1].set_ylabel('Nombre de pixels')
axs[1, 1].set_xlim([0, 256])
axs[1, 1].grid()
axs[1, 1].legend(['Histogramme'])

axs[2, 1].plot(hist3, color='gray')
axs[2, 1].set_title('Histogramme de l\'image 3')
axs[2, 1].set_xlabel('Niveaux de gris')
axs[2, 1].set_ylabel('Nombre de pixels')
axs[2, 1].set_xlim([0, 256])
axs[2, 1].grid()
axs[2, 1].legend(['Histogramme'])

plt.show()
