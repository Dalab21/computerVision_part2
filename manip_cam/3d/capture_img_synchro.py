# Capture d'images synchronisées


import cv2

def capture_images(cam_ids, output_folder):
    cams = [cv2.VideoCapture(cam_id) for cam_id in cam_ids]

    for i, cam in enumerate(cams):
        if not cam.isOpened():
            print(f"Camera {cam_ids[i]} not accessible")
            return
    
    while True:
        frames = []
        for cam in cams:
            ret, frame = cam.read()
            if not ret:
                print("Failed to grab frame")
                break
            frames.append(frame)

        if len(frames) == len(cams):
            for i, frame in enumerate(frames):
                cv2.imshow(f'Camera {i}', frame)
                cv2.imwrite(f'{output_folder}/cam{i}_frame.jpg', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for cam in cams:
        cam.release()
    cv2.destroyAllWindows()

# Example usage
capture_images([0, 1, 2], 'captured_images')
