import mediapipe as mp   # pip install mediapipe==0.10.8
import cv2

# Initialiser MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Ouvrir la caméra
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir l'image en RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Effectuer la détection des mains
    result = hands.process(rgb_frame)

    # Afficher les résultats
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('MediaPipe Hands', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
