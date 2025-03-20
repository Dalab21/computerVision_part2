# Rectification et Génération de la Carte de Disparité

import cv2
import numpy as np

def rectify_and_compute_disparity(img1_path, img2_path, mtx1, dist1, mtx2, dist2):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

    # Find the essential matrix
    E, _ = cv2.findEssentialMat(img1, img2, mtx1)
    _, R, T, _ = cv2.recoverPose(E, img1, img2, mtx1)

    R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(mtx1, dist1, mtx2, dist2, img1.shape[::-1], R, T)
    map1x, map1y = cv2.initUndistortRectifyMap(mtx1, dist1, R1, P1, img1.shape[::-1], cv2.CV_32FC1)
    map2x, map2y = cv2.initUndistortRectifyMap(mtx2, dist2, R2, P2, img2.shape[::-1], cv2.CV_32FC1)

    img1_rectified = cv2.remap(img1, map1x, map1y, cv2.INTER_LINEAR)
    img2_rectified = cv2.remap(img2, map2x, map2y, cv2.INTER_LINEAR)

    # Compute disparity map
    stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
    disparity = stereo.compute(img1_rectified, img2_rectified)
    
    # Normalize the disparity for visualization
    disparity_normalized = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    disparity_normalized = np.uint8(disparity_normalized)
    
    cv2.imshow('Disparity Map', disparity_normalized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return disparity, Q

disparity, Q = rectify_and_compute_disparity('captured_images/cam1_frame.jpg', 'captured_images/cam2_frame.jpg', mtx1, dist1, mtx2, dist2)
