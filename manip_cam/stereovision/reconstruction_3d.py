# utilisation de la carte de disparité pour reconstruire la scène en 3D



def reconstruct_3d(disparity, Q):
    points_3d = cv2.reprojectImageTo3D(disparity, Q)
    return points_3d

points_3d = reconstruct_3d(disparity, Q)
print("3D Points:", points_3d)
