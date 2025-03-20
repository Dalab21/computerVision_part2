#Rotation de l'image
import cv2
import numpy as np


image = cv2.imread('../data/images/img2.jpg')

# La matrice de rotation
angle = 45  # angle de rotation en degrés
scale = 1.0  # échelle de l'image
center = (image.shape[1] // 2, image.shape[0] // 2)  # centre de rotation
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Application de la rotation à l'image
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Affichage de l'image rotatée
cv2.imshow('rotated_image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
