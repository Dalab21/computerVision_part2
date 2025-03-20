import cv2

# Chargement de la video
cap = cv2.VideoCapture('../data/video/video2.mp4')

# Initialisation du compteur de frames
frame_count = 0

# Boucle de lecture de la vidéo
while True:
    # Lecture de la frame de la vidéo
    success, frame = cap.read()
    if not success:
        break

    # Incrémentation du compteur de frames
    frame_count += 1

# Affichage du nombre total de frames
print('Nombre total de frames :', frame_count)

# Libération des ressources
cap.release()


"""
Comptage du nombre de frames en lisant réellement chacune d'elles à travers une boucle while. La frame lue est ensuite incrémentée à un compteur à chaque incrémentation.
Le nombre total de frames est rétourné à la fin de la boucle. Cette méthode peut prendre plus de temps mais elle lit réellement chaque frame de la vidéo.
"""
