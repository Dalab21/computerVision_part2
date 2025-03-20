# Segmentation d'images
import cv2
import numpy as np

# Charger l'image
image = cv2.imread('../data/images/img3.jpg')

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer le seuillage
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Afficher l'image seuillée
cv2.imshow('Image seuillée', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
La méthode cv2.threshold() prend trois arguments : 
l'image en niveaux de gris, la valeur de seuil et la valeur maximale.
Dans cet exemple, nous utilisons une valeur de seuil de 127 et 
une valeur maximale de 255. 
La méthode renvoie deux valeurs : l'image seuillée et 
la valeur de seuil réelle utilisée pour le seuillage.
"""