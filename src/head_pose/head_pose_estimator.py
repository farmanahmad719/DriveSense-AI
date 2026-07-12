import cv2
import numpy as np


class HeadPoseEstimator:

    def __init__(self):
        self.face_3d = np.array([
            (0.0, 0.0, 0.0),
            (0.0, -330.0, -65.0),
            (-225.0, 170.0, -135.0),
            (225.0, 170.0, -135.0),
            (-150.0, -150.0, -125.0),
            (150.0, -150.0, -125.0),
        ], dtype=np.float64)

        self.landmark_ids = [1, 199, 33, 263, 61, 291]

        print("HeadPoseEstimator initialized.")

    def estimate_pose(self, frame, face_landmarks):

        h, w, _ = frame.shape

        face_2d = []

        for idx in self.landmark_ids:

            lm = face_landmarks.landmark[idx]

            x = lm.x * w
            y = lm.y * h

            face_2d.append((x, y))

        face_2d = np.array(face_2d, dtype=np.float64)

        focal_length = w

        camera_matrix = np.array(
            [
                [focal_length, 0, w / 2],
                [0, focal_length, h / 2],
                [0, 0, 1],
            ],
            dtype=np.float64,
        )

        dist_coeffs = np.zeros((4, 1))

        success, rotation_vec, translation_vec = cv2.solvePnP(
            self.face_3d,
            face_2d,
            camera_matrix,
            dist_coeffs,
            flags=cv2.SOLVEPNP_ITERATIVE,
        )

        if not success:
            return None

        rotation_matrix, _ = cv2.Rodrigues(rotation_vec)

        projection_matrix = np.hstack((rotation_matrix, translation_vec))

        _, _, _, _, _, _, euler_angles = cv2.decomposeProjectionMatrix(
            projection_matrix
        )

        pitch = euler_angles[0, 0]
        yaw = euler_angles[1, 0]
        roll = euler_angles[2, 0]

        if pitch > 90:
            pitch -= 180
        elif pitch < -90:
            pitch += 180

        if roll > 90:
            roll -= 180
        elif roll < -90:
            roll += 180
        return pitch, yaw, roll