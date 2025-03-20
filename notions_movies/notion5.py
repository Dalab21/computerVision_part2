import cv2

# Charger une vidéo
video = cv2.VideoCapture('../data/video/video1.mp4')

# Lire la première frame
success, frame = video.read()

# Convertir la première frame en niveaux de gris
gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Détecter les caractéristiques de l'objet à suivre
objet = cv2.selectROI(gray_frame, False)

# Initialiser le tracker
tracker = cv2.TrackerCSRT_create()
tracker.init(frame, objet)

# Boucle de suivi
while True:
    # Lire la frame suivante
    success, frame = video.read()
    if not success:
        break

    # Mettre à jour la position de l'objet
    success, objet = tracker.update(frame)
    if success:
        # Dessiner un rectangle autour de l'objet
        (x, y, w, h) = [int(v) for v in objet]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Afficher la frame avec le rectangle de suivi
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer les ressources
video.release()
cv2.destroyAllWindows()



# import cv2

# # Charger une vidéo
# video = cv2.VideoCapture('../data/video/video1.mp4')

# # Lire la première
# #frame
# success, frame = video.read()
# # Convertir la première frame en niveaux de gris
# gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# # Détecter les caractéristiques de l'objet à suivre
# objet = cv2.selectROI(gray_frame, False)

# # Initialiser le tracker
# tracker = cv2.TrackerMOSSE_create()
# tracker.init(frame, objet)

# # Boucle de suivi
# while True:
#     # Lire la frame suivante
#     success, frame = video.read()
#     if not success:
#         break

#     # Mettre à jour la position de l'objet
#     success, objet = tracker.update(frame)
#     if success:
#         # Dessiner un rectangle autour de l'objet
#         (x, y, w, h) = [int(v) for v in objet]
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     # Afficher la frame avec le rectangle de suivi
#     cv2.imshow('frame', frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Libérer les ressources
# video.release()
# cv2.destroyAllWindows()
