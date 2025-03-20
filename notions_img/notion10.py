import cv2

# Charger l'image
image = cv2.imread('../data/images/img1.jpg')

# Conversion de l'image en noir blanc
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Affichage de l'image originale et de l'image en noir et blanc
cv2.imshow('Image originale', image)
cv2.imshow('Image en noir et blanc', gray_image)

# Attendre qu'une touche soit pressée et fermer les fenêtres
cv2.waitKey(0)
cv2.destroyAllWindows()
