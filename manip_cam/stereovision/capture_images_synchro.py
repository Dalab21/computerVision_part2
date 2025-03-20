# Capture des images synchronisées à partir de 2 caméras
import cv2

def capture_images(cam_ids, output_folder):
    cams = [cv2.VideoCapture(cam_id) for cam_id in cam_ids]
    for cam in cams:
        if not cam.isOpened():
            print("Error opening camera")
            return
    
    ret1, frame1 = cams[0].read()
    ret2, frame2 = cams[1].read()

    if ret1 and ret2:
        cv2.imwrite(f'{output_folder}/cam1_frame.jpg', frame1)
        cv2.imwrite(f'{output_folder}/cam2_frame.jpg', frame2)
    
    for cam in cams:
        cam.release()
    cv2.destroyAllWindows()

capture_images([0, 1], 'captured_images')
