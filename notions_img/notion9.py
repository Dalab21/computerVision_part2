import cv2


image = cv2.imread('../data/images/img2.jpg')

# Dessin d'une ligne
cv2.line(image, (0, 0), (500, 500), (255, 0, 0), 5)

# Ajout de texte
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'Salut, antilopes!', (50, 50), font, 1, (0, 255, 0), 2)

# Affichage de l'image
cv2.imshow('Image avec dessin', image)

# Attendre l'appui de la touche 0 pour fermer la fenêtre
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
La fonction cv2.line() prend les arguments suivants :

    image : l'image sur laquelle dessiner la ligne.
    pt1 : le point de départ de la ligne (coordonnées x et y).
    pt2 : le point de fin de la ligne (coordonnées x et y).
    color : la couleur de la ligne (en BGR).
    thickness : l'épaisseur du trait (en pixels).

La fonction cv2.putText() prend les arguments suivants :

    image : l'image sur laquelle ajouter le texte.
    text : le texte à ajouter.
    org : le point de départ du texte (coordonnées x et y du coin inférieur gauche).
    font : la police à utiliser.
    fontScale : la taille de la police.
    color : la couleur du texte (en BGR).
    thickness : l'épaisseur du trait (en pixels)
"""
