import cv2
import time

# Ouvrir le flux vidéo
cap = cv2.VideoCapture('../data/video/video3.mp4')

# Définir la police pour le texte
font = cv2.FONT_HERSHEY_SIMPLEX

# Boucle de lecture de la vidéo
while True:
    # Lire une frame de la vidéo
    success, frame = cap.read()
    if not success:
        break

    # Enregistrer le temps de début du traitement de la frame
    t_start = time.time()

    # Effectuer le traitement de la frame (par exemple, appliquer un filtre)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Calculer le temps de fin du traitement de la frame
    t_fin = time.time()

     # Vérifier si le temps de traitement de la frame est supérieur à zéro
    if t_fin - t_start > 0:
        # Calculer le FPS
        fps = 1 / (t_fin - t_start)

        # Afficher le FPS sur l'image
        text = 'FPS: {:.2f}'.format(fps)
        cv2.putText(frame, text, (10, 30), font, 1, (255, 255, 255), 2)

    # Afficher l'image
    cv2.imshow('frame', frame)

    # Vérifier si l'utilisateur a appuyé sur la touche 'q' pour quitter
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Libérer les ressources
cap.release()
cv2.destroyAllWindows()



"""
Cet exemple utilise la fonction time.time() pour mesurer le temps de début et de fin du traitement de chaque frame. 
Le FPS est calculé en utilisant la formule fps = 1 / (t_fin - t_start) et affiché sur l'image en utilisant cv2.putText(). 
Notez que dans cet exemple, le traitement de la frame consiste simplement à convertir l'image en niveaux de gris en utilisant cv2.cvtColor().


FPS
La notion de "frames per second" (fps) ou "images par seconde" 
est une mesure de la fréquence à laquelle les images d'une vidéo sont affichées à l'écran. Elle est généralement exprimée en nombre d'images par seconde.

Par exemple, si une vidéo a un taux de rafraîchissement de 30 fps, cela signifie que 30 images distinctes sont affichées à l'écran chaque seconde. Plus le taux de rafraîchissement est élevé, plus la vidéo apparaîtra fluide et naturelle. Cependant, un taux de rafraîchissement plus élevé nécessite également une bande passante plus élevée pour stocker et lire la vidéo.

Dans le contexte du traitement d'images et de vidéos, le FPS est une mesure importante de la performance du système. Par exemple, si vous appliquez un filtre à une vidéo, vous voudrez peut-être mesurer le temps nécessaire pour traiter chaque frame et calculer le FPS résultant pour évaluer l'impact du filtre sur les performances. En général, plus le FPS est élevé, meilleures sont les performances du système. Cependant, il est important de trouver un équilibre entre les performances et la qualité de la vidéo, car un traitement excessif peut dégrader la qualité de la vidéo ou introduire des artefacts indésirables.
"""





# import cv2
# import time

# # Ouvrir le flux vidéo
# cap = cv2.VideoCapture('../data/video/video3.mp4')

# # Définir la police pour le texte
# font = cv2.FONT_HERSHEY_SIMPLEX

# # Boucle de lecture de la vidéo
# while True:
#     # Lire une frame de la vidéo
#     success, frame = cap.read()
#     if not success:
#         break

#     # Calculer le FPS
#     fps = cap.get(cv2.CAP_PROP_FPS)

#     # Afficher le FPS sur l'image
#     text = 'FPS: {:.2f}'.format(fps)
#     cv2.putText(frame, text, (10, 30), font, 1, (255, 255, 255), 2)

#     # Afficher l'image
#     cv2.imshow('frame', frame)

#     # Vérifier si l'utilisateur a appuyé sur la touche 'q' pour quitter
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Libérer les ressources
# cap.release()
# cv2.destroyAllWindows()

# """
# le flux vidéo video.mp4 en utilisant cv2.VideoCapture() et définit la police pour le texte en utilisant cv2.FONT_HERSHEY_SIMPLEX. Dans la boucle while,
# il lit chaque frame de la vidéo et calcule le FPS en utilisant la propriété cv2.CAP_PROP_FPS. 
# Ensuite, il affiche le FPS sur l'image en utilisant cv2.putText() et affiche l'image en utilisant cv2.imshow(). La boucle se termine lorsque l'utilisateur appuie sur la touche 'q'.

# Notez que le FPS affiché sur l'image peut ne pas être précis à 100%, car le temps nécessaire pour traiter chaque frame peut varier en fonction de la complexité du traitement effectué. 
# Si vous avez besoin d'une mesure plus précise du FPS, vous pouvez utiliser la fonction time.time() pour mesurer le temps entre les frames et calculer le FPS en conséquence.
# """