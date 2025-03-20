# La reconstruction 3D peut être réalisée en utilisant la triangulation après la détection des points clés.
# possible d'utiliser des méthodes comme SIFT ou ORB pour détecter les points clés et FLANN ou BFMatcher pour correspondre les points
# Exemple de triangulation basique:


def triangulate_points(pts1, pts2, mtx1, dist1, mtx2, dist2, R, T):
    pts1 = cv2.undistortPoints(np.expand_dims(pts1, axis=1), mtx1, dist1)
    pts2 = cv2.undistortPoints(np.expand_dims(pts2, axis=1), mtx2, dist2)
    
    P1 = np.hstack((np.eye(3, 3), np.zeros((3, 1))))
    P2 = np.hstack((R, T))
    
    P1 = np.dot(mtx1, P1)
    P2 = np.dot(mtx2, P2)
    
    points_4d = cv2.triangulatePoints(P1, P2, pts1, pts2)
    points_3d = points_4d[:3] / points_4d[3]
    
    return points_3d.T

# Example points (replace with actual matched points)
pts1 = np.array([[100, 150], [200, 250]], dtype=np.float32)
pts2 = np.array([[102, 152], [202, 252]], dtype=np.float32)

# Rotation matrix and translation vector between cameras
R = np.eye(3)  # Placeholder, should be calculated or provided
T = np.array([0.1, 0, 0])  # Placeholder, should be calculated or provided

points_3d = triangulate_points(pts1, pts2, mtx1, dist1, mtx2, dist2, R, T)
print("3D Points:\n", points_3d)
