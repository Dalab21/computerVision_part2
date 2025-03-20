import cv2 as c

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)
    return c.resize(frame, dimensions, interpolation=c.INTER_AREA)

# vidéo
capture = c.VideoCapture('./data/video/video1.mp4')

# Vérification de l'ouverture de la vidéo avec succès
if not capture.isOpened():
    print("Erreur lors de l'ouverture du fichier vidéo")
    exit()

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    c.imshow('Video Resized', frame_resized)
    if c.waitKey(20) & 0xFF == ord ('d'):
        break

capture.release()
c.destroyAllWindows()




# import cv2 as c

# def rescaleFrame(frame, scale=0.75):
#     width = int(frame.shape[1]*scale)
#     height = int(frame.shape[0]*scale)

#     dimensions =(width, height)

#     return c.resize(frame, dimensions, interpolation=c.INTER_AREA)

# capture = c.VideoCapture('./data/video/video1.mp4')

# while True:
#     isTrue, frame = capture.read()
#     frame_resized = rescaleFrame(frame)
#     c.imshow('Video Resized', frame_resized)
#     if c.waitKey(20) & 0xFF == ord ('d'):
#         break
# capture.release()
# c.destroyAllWindows()