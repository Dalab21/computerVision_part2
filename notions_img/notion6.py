# Détection de contours
import cv2

image = cv2.imread('../data/images/img2.jpg')

#Valeurs données aux seuils
threshold1 = 50
threshold2 = 150


# Convertir l'image en NG(niveaux de gris)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Détection des contours avec le filtre de Canny
edges = cv2.Canny(gray_image, threshold1, threshold2)

# Affichage des contours détectées
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
Le filtre de Canny est un algorithme de détection de contours qui utilise deux seuils : threshold1 et threshold2. 
Les pixels dont l'intensité est supérieure à threshold2 sont considérés comme des contours fortes, tandis que les pixels 
dont l'intensité est inférieure à threshold1 sont considérés comme n'appartenant pas aux contours. 
Les pixels dont l'intensité est comprise entre threshold1 et threshold2 sont considérés comme des contours faibles 
et ne sont conservés que s'ils sont connectés à des contours fortes.
Les valeurs de threshold1 et threshold2 doivent être choisies en fonction de l'image et de l'application. Généralement, 
threshold1 est fixé à une valeur basse pour détecter un maximum de contours, tandis que threshold2 est fixé à une valeur 
plus élevée pour éliminer les fausses détections. Le rapport communément utilisé entre les 2 seuils est de 1:2 ou 1:3
(ce qui implique que threshold2 = 2 * threshold1 ou threshold2 = 3 * threshold1).
"""
