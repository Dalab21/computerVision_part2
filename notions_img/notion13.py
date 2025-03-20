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

# Créer une grille de sous-tracés
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Afficher les images originales
axs[0, 0].imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Image 1')
axs[0, 0].axis('off')

axs[0, 1].imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Image 2')
axs[0, 1].axis('off')

# Afficher les histogrammes
axs[1, 0].plot(hist1, color='gray')
axs[1, 0].set_title('Histogramme de l\'image 1')
axs[1, 0].set_xlabel('Niveaux de gris')
axs[1, 0].set_ylabel('Nombre de pixels')
axs[1, 0].set_xlim([0, 256])
axs[1, 0].grid()
axs[1, 0].legend(['Histogramme'])

axs[1, 1].plot(hist2, color='gray')
axs[1, 1].set_title('Histogramme de l\'image 2')
axs[1, 1].set_xlabel('Niveaux de gris')
axs[1, 1].set_ylabel('Nombre de pixels')
axs[1, 1].set_xlim([0, 256])
axs[1, 1].grid()
axs[1, 1].legend(['Histogramme'])

# Ajouter des statistiques aux histogrammes
mean1 = np.mean(gray_image1)
median1 = np.median(gray_image1)
std1 = np.std(gray_image1)
axs[1, 0].text(0.05, 0.9, f'Moyenne : {mean1:.2f}\nMédiane : {median1:.2f}\nÉcart-type : {std1:.2f}', transform=axs[1, 0].transAxes)

mean2 = np.mean(gray_image2)
median2 = np.median(gray_image2)
std2 = np.std(gray_image2)
axs[1, 1].text(0.05, 0.9, f'Moyenne : {mean2:.2f}\nMédiane : {median2:.2f}\nÉcart-type : {std2:.2f}', transform=axs[1, 1].transAxes)

plt.show()
