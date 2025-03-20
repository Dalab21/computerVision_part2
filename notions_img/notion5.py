# Filtre de flou gaussien sur une image
import cv2

image = cv2.imread('../data/images/img1.jpg')

# exemple de filtre de flou gaussien
ksize_width = 5
ksize_height = 5
sigmaX = 0

# Application d'un filtre de flou gaussien
blurred_image = cv2.GaussianBlur(image, (ksize_width, ksize_height), sigmaX)

# Affichage de l'image floutée
cv2.imshow('blurred_image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
Le filtre de Canny est un algorithme de détection de bordures largement utilisé en traitement d'images. 
Il permet de détecter les contours d'objets dans une image en utilisant une approche à plusieurs étapes. 
Les principales étapes du filtre de Canny :

    Réduction du bruit : Comme le filtre de Canny est sensible au bruit, il est important de réduire le bruit présent dans l'image avant de détecter les bordures. 
                        Pour cela, on utilise généralement un filtre de flou gaussien (comme dans le code que vous avez fourni).
    Calcul du gradient : Pour chaque pixel de l'image, on calcule la dérivée horizontale et verticale de l'intensité lumineuse.
                         À partir de ces dérivées, on calcule la magnitude et l'orientation du gradient.
    Suppression des non-maxima : Cette étape consiste à supprimer les pixels qui ne correspondent pas à un maximum local du gradient. 
                                Pour chaque pixel, on compare la magnitude du gradient avec celle des pixels voisins dans la direction du gradient. 
                                Si la magnitude du pixel courant est inférieure à celle des pixels voisins, le pixel est supprimé.
    Seuillage par hystérésis : Cette étape permet de sélectionner les pixels qui correspondent effectivement à des bordures. 
                               On utilise 2 seuils : 1 seuil inférieur (threshold1) et 1 seuil supérieur (threshold2). 
                               Les pixels dont la magnitude du gradient est supérieure au seuil supérieur sont considérés comme des bordures. 
                               Les pixels dont la magnitude du gradient est inférieure au seuil inférieur sont rejetés. 
                               Les pixels dont la magnitude du gradient est comprise entre les 2 seuils sont conservés s'ils sont connectés à des pixels de bordure.
"""