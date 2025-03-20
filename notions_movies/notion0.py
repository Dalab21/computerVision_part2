import cv2

# Ouvrir le fichier vidéo
cap = cv2.VideoCapture('../data/video/video2.mp4')

# Boucle de lecture de la vidéo
while True:
    # Lire une frame de la vidéo
    success, frame = cap.read()
    if not success:
        break

    # Afficher la frame
    cv2.imshow('frame', frame)

    # Vérifier si l'utilisateur a appuyé sur la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()
