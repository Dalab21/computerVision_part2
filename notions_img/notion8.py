# Dessin de figures géometriques sur image
import cv2


image = cv2.imread('../data/images/img1.jpg')

# Dessin d'un rectangle
cv2.rectangle(image, (10, 10), (100, 100), (0, 255, 0), 2)

# Dessin d'un cercle
cv2.circle(image, (50, 50), 25, (255, 0, 0), 2)

# Affichage de l'image
cv2.imshow('Image avec forme', image)

# Attente de l'appui sur touche 0 pour fermer la fenêtre
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
La fonction cv2.rectangle() prend les arguments suivants :

    image : l'image sur laquelle dessiner le rectangle.
    pt1 : le point de départ du rectangle (coordonnées x et y du coin supérieur gauche).
    pt2 : le point de fin du rectangle (coordonnées x et y du coin inférieur droit).
    color : la couleur du rectangle (en BGR).
    thickness : l'épaisseur du trait (en pixels).

La fonction cv2.circle() prend les arguments suivants :

    image : l'image sur laquelle dessiner le cercle.
    center : le centre du cercle (coordonnées x et y).
    radius : le rayon du cercle.
    color : la couleur du cercle (en BGR).
    thickness : l'épaisseur du trait (en pixels).
"""
