# Récadrage de l'image
import cv2

image = cv2.imread('../data/images/img2.jpg')

height=100
width=100
y=50
x=50
# Recadrage de l'image
cropped_image = image[y:y+height, x:x+width]

# Affichage de l'image recadrée
cv2.imshow('cropped_image', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
