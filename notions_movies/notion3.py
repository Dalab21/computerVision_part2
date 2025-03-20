import cv2

# Ouvrir la caméra
cap = cv2.VideoCapture(0)

# Boucle de traitement de la vidéo
while True:
    # Lire une frame de la vidéo
    success, frame = cap.read()
    if not success:
        break

    # Appliquer un filtre de flou gaussien
    blurred_frame = cv2.GaussianBlur(frame, (15, 15), 0)

    # Afficher la frame originale et la frame floutée côte à côte
    result = cv2.hconcat([frame, blurred_frame])
    cv2.imshow('result', result)

    # Vérifier si l'utilisateur a appuyé sur la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
cap.release()
cv2.destroyAllWindows()