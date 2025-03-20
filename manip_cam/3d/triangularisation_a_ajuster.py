import cv2
import numpy as np

# Calibration data (replace with your own calibration results)
mtx1 = ... # Camera matrix for camera 1
dist1 = ... # Distortion coefficients for camera 1
mtx2 = ... # Camera matrix for camera 2
dist2 = ... # Distortion coefficients for camera 2

# Load images
img1 = cv2.imread('path/to/image1.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('path/to/image2.jpg', cv2.IMREAD_GRAYSCALE)

# Initialize SIFT detector
sift = cv2.SIFT_create()

# Find keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Use FLANN based matcher for matching descriptors
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1, des2, k=2)

# Apply ratio test to select good matches
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Extract location of good matches
pts1 = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 2)
pts2 = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 2)

# Find the essential matrix
E, mask = cv2.findEssentialMat(pts1, pts2, mtx1, method=cv2.RANSAC, prob=0.999, threshold=1.0)

# Recover pose from the essential matrix
_, R, T, mask = cv2.recoverPose(E, pts1, pts2, mtx1)

# Triangulate points
pts1 = pts1[mask.ravel() == 1]
pts2 = pts2[mask.ravel() == 1]

pts1_undist = cv2.undistortPoints(np.expand_dims(pts1, axis=1), mtx1, dist1)
pts2_undist = cv2.undistortPoints(np.expand_dims(pts2, axis=1), mtx2, dist2)

P1 = np.dot(mtx1, np.hstack((np.eye(3), np.zeros((3, 1)))))
P2 = np.dot(mtx2, np.hstack((R, T)))

points_4d = cv2.triangulatePoints(P1, P2, pts1_undist, pts2_undist)
points_3d = points_4d[:3] / points_4d[3]

print("3D Points:\n", points_3d.T)
