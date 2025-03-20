import cv2

# Chargement de l'image
image = cv2.imread('../data/images/img2.jpg')

# Écrire du texte sur l'image
font = cv2.FONT_HERSHEY_SIMPLEX
text = 'Bonjour, OpenCV!'
position = (50, 50)
font_scale = 1
color = (255, 0, 0)  # BGR
thickness = 2

cv2.putText(image, text, position, font, font_scale, color, thickness, cv2.LINE_AA)

# Affichage de l'image avec texte
cv2.imshow('image_with_text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
