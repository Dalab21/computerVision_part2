import cv2
import numpy as np
from matplotlib import pyplot as plt

# Étape 1: Lecture de l'image
image = cv2.imread('../data/images/img2.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Erreur: l'image n'a pas été chargée correctement.")
    exit()

# Étape 2: Calcul de l'histogramme
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Étape 3: Égalisation de l'histogramme
equalized_image = cv2.equalizeHist(image)

# Étape 4: Application de CLAHE
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_image = clahe.apply(image)

# Affichage des résultats
cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.imshow('CLAHE Image', clahe_image)

# Plot de l'histogramme
plt.figure()
plt.title("Histogramme de l'image originale")
plt.xlabel("Intensité des pixels")
plt.ylabel("Nombre de pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

# Histogrammes des images égalisées
hist_equalized = cv2.calcHist([equalized_image], [0], None, [256], [0, 256])
hist_clahe = cv2.calcHist([clahe_image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Histogrammes des images égalisées")
plt.xlabel("Intensité des pixels")
plt.ylabel("Nombre de pixels")
plt.plot(hist_equalized, label='Equalized Histogram')
plt.plot(hist_clahe, label='CLAHE Histogram')
plt.legend()
plt.xlim([0, 256])
plt.show()

# Attendre une touche pour fermer les fenêtres
cv2.waitKey(0)
cv2.destroyAllWindows()
