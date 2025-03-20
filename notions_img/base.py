import cv2

# Lecture et affichage d'image
image = cv2.imread('../data/images/img1.jpg')

# Conversion en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Redimensionnement de l'image
resized_image = cv2.resize(image, (300, 300))

# Détection des bords
edges = cv2.Canny(gray_image, 100, 200)

# Seuillage adaptatif
thresh = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Détection des contours
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dessin des contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)

#Erosion dilatation__debut
# Création d'un kernel
kernel = np.ones((5, 5), np.uint8)

# Érosion
erosion = cv2.erode(image, kernel, iterations = 1)

# Dilatation
dilation = cv2.dilate(image, kernel, iterations = 1)
#Erosion dilatation__fin


# Affichage de l'image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
