import cv2
import numpy as np
import threading

class DualCamLive:
    def __init__(self):
        self.cap1 = cv2.VideoCapture(0)
        self.cap2 = cv2.VideoCapture(1)
        self.running = False

    def start_streaming(self):
        self.running = True
        thread1 = threading.Thread(target=self.stream_camera, args=(self.cap1, "Camera 1"))
        thread2 = threading.Thread(target=self.stream_camera, args=(self.cap2, "Camera 2"))
        thread1.start()
        thread2.start()

    def stream_camera(self, cap, name):
        while self.running:
            ret, frame = cap.read()
            if ret:
                cv2.imshow(name, frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def stop_streaming(self):
        self.running = False
        self.cap1.release()
        self.cap2.release()
        cv2.destroyAllWindows()

    def capture_frames(self):
        ret1, frame1 = self.cap1.read()
        ret2, frame2 = self.cap2.read()
        if ret1 and ret2:
            cv2.imwrite("capture1.jpg", frame1)
            cv2.imwrite("capture2.jpg", frame2)
            print("Frames captured and saved!")

if __name__ == "__main__":
    dual_cam = DualCamLive()
    dual_cam.start_streaming()
    
    # To stop streaming and capture frames, you can call:
    # dual_cam.stop_streaming()
    # dual_cam.capture_frames()
        