import cv2

# Ouvrir le fichier vidéo
cap = cv2.VideoCapture('video.mp4')

# Définir le temps en secondes pour la capture de l'image
time_to_capture = 3

# Calculer le nombre de frames à sauter pour atteindre le temps désiré
fps = cap.get(cv2.CAP_PROP_FPS)
frames_to_skip = int(time_to_capture * fps)

# Boucle de lecture de la vidéo
while True:
    # Lire une frame de la vidéo
    success, frame = cap.read()
    if not success:
        break

    # Ignorer les frames jusqu'au temps désiré
    frames_to_skip -= 1
    if frames_to_skip > 0:
        continue

    # Enregistrer l'image
    cv2.imwrite('image.jpg', frame)
    break

# Libérer les ressources
cap.release()


"""
ouvre le fichier vidéo video.mp4 en utilisant cv2.VideoCapture() et définit le temps en secondes pour la capture de l'image (time_to_capture). 
Ensuite, il calcule le nombre de frames à sauter pour atteindre le temps désiré en utilisant la propriété cv2.CAP_PROP_FPS. Dans la boucle while, 
il lit chaque frame de la vidéo et ignore les frames jusqu'au temps désiré en utilisant le compteur frames_to_skip. Lorsque le temps désiré est atteint, 
il enregistre l'image en utilisant cv2.imwrite() et quitte la boucle.

Notez que cette méthode utilise le nombre de frames par seconde (FPS) de la vidéo pour calculer le nombre de frames à sauter.
Si la vidéo a un FPS variable, cette méthode peut ne pas fonctionner correctement. Dans ce cas, vous pouvez utiliser la fonction cv2.get() pour obtenir 
le temps actuel de la vidéo et le comparer au temps désiré pour la capture de l'image.



"""