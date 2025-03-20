#Rédimensionnement de l'image
import cv2

# Chargement de l'image
image = cv2.imread("../data/images/img1.jpg")

# nouvelles tailles
new_width = 210
new_height = 210

# Redimensionnement de l'image
resized_image = cv2.resize(image, (new_width, new_height))

# Affichage de l'image redimensionnée
cv2.imshow('resized_image', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
