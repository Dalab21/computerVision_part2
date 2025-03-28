import cv2
import numpy as np
import mediapipe as mp


IMG_PATH = 'C:/Users/Daou/Music/OpenCV/data/images/img1.jpg'

img = cv2.imread(IMG_PATH) 

#detect faces
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDtetction(model_selection=0,min_detection_confidence=0) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    for detection in out.detections:
        location_data = detection.location_data
        bbox = location_data.relative_bounding_box

        x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height