import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage

class CameraThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self, cam_num):
        QThread.__init__(self)
        self.cam_num = cam_num

    def run(self):
        cap = cv2.VideoCapture(self.cam_num)
        while True:
            ret, frame = cap.read()
            if ret:
                self.change_pixmap_signal.emit(frame)
            else:
                break

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Créer un widget central et définir une disposition horizontale
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Layouts pour chaque caméra
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()

        self.thread1 = CameraThread(0)
        self.thread2 = CameraThread(1)

        self.thread1.change_pixmap_signal.connect(self.update_image1)
        self.thread2.change_pixmap_signal.connect(self.update_image2)

        self.label1 = QLabel(self)
        self.label2 = QLabel(self)

        self.button_start1 = QPushButton('Start Camera 1', self)
        self.button_start2 = QPushButton('Start Camera 2', self)
        self.button_stop1 = QPushButton('Stop Camera 1', self)
        self.button_stop2 = QPushButton('Stop Camera 2', self)
        self.button_capture1 = QPushButton('Capture Camera 1', self)
        self.button_capture2 = QPushButton('Capture Camera 2', self)

        self.button_start1.clicked.connect(self.thread1.start)
        self.button_start2.clicked.connect(self.thread2.start)
        self.button_stop1.clicked.connect(self.thread1.terminate)
        self.button_stop2.clicked.connect(self.thread2.terminate)
        self.button_capture1.clicked.connect(self.capture_image1)
        self.button_capture2.clicked.connect(self.capture_image2)

        layout1.addWidget(self.label1)
        layout1.addWidget(self.button_start1)
        layout1.addWidget(self.button_stop1)
        layout1.addWidget(self.button_capture1)

        layout2.addWidget(self.label2)
        layout2.addWidget(self.button_start2)
        layout2.addWidget(self.button_stop2)
        layout2.addWidget(self.button_capture2)

        main_layout.addLayout(layout1)
        main_layout.addLayout(layout2)

    def update_image1(self, frame):
        """Updates the label with a new video frame"""
        self.frame1 = frame
        qimg = self.convert_cv_qt(frame)
        self.label1.setPixmap(qimg)

    def update_image2(self, frame):
        """Updates the label with a new video frame"""
        self.frame2 = frame
        qimg = self.convert_cv_qt(frame)
        self.label2.setPixmap(qimg)

    def convert_cv_qt(self, frame):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def capture_image1(self):
        """Capture image from camera 1"""
        if hasattr(self, 'frame1'):
            cv2.imwrite('capture_camera1.png', self.frame1)

    def capture_image2(self):
        """Capture image from camera 2"""
        if hasattr(self, 'frame2'):
            cv2.imwrite('capture_camera2.png', self.frame2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())





# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt, QThread, pyqtSignal
# import cv2
# import numpy as np
# from PyQt5.QtGui import QPixmap, QImage, QGuiApplication  # Import QtGui here

# class CameraThread(QThread):
#     change_pixmap_signal = pyqtSignal(np.ndarray)

#     def __init__(self, cam_num):
#         QThread.__init__(self)
#         self.cam_num = cam_num

#     def run(self):
#         cap = cv2.VideoCapture(self.cam_num)
#         while True:
#             ret, frame = cap.read()
#             if ret:
#                 self.change_pixmap_signal.emit(frame)
#             else:
#                 break

# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)

#         # Créer un widget central et définir une disposition verticale
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#         layout = QVBoxLayout(central_widget)

#         self.thread1 = CameraThread(0)
#         self.thread2 = CameraThread(1)

#         self.thread1.change_pixmap_signal.connect(self.update_image1)
#         self.thread2.change_pixmap_signal.connect(self.update_image2)

#         self.label1 = QLabel(self)
#         self.label2 = QLabel(self)

#         self.button_start1 = QPushButton('Start Camera 1', self)
#         self.button_start2 = QPushButton('Start Camera 2', self)
#         self.button_stop1 = QPushButton('Stop Camera 1', self)
#         self.button_stop2 = QPushButton('Stop Camera 2', self)

#         self.button_start1.clicked.connect(self.thread1.start)
#         self.button_start2.clicked.connect(self.thread2.start)
#         self.button_stop1.clicked.connect(self.thread1.terminate)
#         self.button_stop2.clicked.connect(self.thread2.terminate)

#         layout.addWidget(self.label1)
#         layout.addWidget(self.label2)
#         layout.addWidget(self.button_start1)
#         layout.addWidget(self.button_start2)
#         layout.addWidget(self.button_stop1)
#         layout.addWidget(self.button_stop2)

#     def update_image1(self, frame):
#         """Updates the label with a new video frame"""
#         qimg = self.convert_cv_qt(frame)
#         self.label1.setPixmap(qimg)

#     def update_image2(self, frame):
#         """Updates the label with a new video frame"""
#         qimg = self.convert_cv_qt(frame)
#         self.label2.setPixmap(qimg)

#     def convert_cv_qt(self, frame):
#         """Convert from an opencv image to QPixmap"""
#         rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb_image.shape
#         bytes_per_line = ch * w
#         convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
#         return QPixmap.fromImage(p)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())
