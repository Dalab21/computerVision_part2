# calibrage des caméras pour obtenir les matrices de calibration 
# #et les coefficients de distorsion.

import cv2
import numpy as np
import glob

def calibrate_camera(images):
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    objp = np.zeros((6*9, 3), np.float32)
    objp[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)

    objpoints = []
    imgpoints = []

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)
        if ret:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            imgpoints.append(corners2)

    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
    return mtx, dist

images_cam1 = glob.glob('calibration_images/cam1/*.jpg')
images_cam2 = glob.glob('calibration_images/cam2/*.jpg')

mtx1, dist1 = calibrate_camera(images_cam1)
mtx2, dist2 = calibrate_camera(images_cam2)
