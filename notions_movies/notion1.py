import cv2

# Ouvrir le fichier vidéo
cap = cv2.VideoCapture('video.mp4')

# Obtenir le nombre total de frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print('Nombre total de frames :', total_frames)

# Libérer les ressources
cap.release()

"""
Cette méthode ne lit pas réellement les frames de la vidéo.
Elle obtient simplement le nombre total de frames à partir des métadonnées de la vidéo.
"""