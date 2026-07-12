import cv2
from scipy.spatial import distance
"""
Utility functions and constants for eye landmark processing.
"""

# Left eye landmark indices
LEFT_EYE = [33, 160, 158, 133, 153, 144]

# Right eye landmark indices
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
def get_eye_landmarks(face_landmarks, eye_indices):
    """
    Extract the landmarks corresponding to one eye.

    Parameters
    ----------
    face_landmarks : MediaPipe landmarks
        All facial landmarks detected by MediaPipe.

    eye_indices : list
        Landmark indices for the eye.

    Returns
    -------
    list
        List of six eye landmarks.
    """

    eye_points = []

    for index in eye_indices:
        eye_points.append(face_landmarks.landmark[index])

    return eye_points
def landmarks_to_pixels(landmarks, frame_width, frame_height):
    """
    Convert normalized MediaPipe landmarks
    into pixel coordinates.
    """

    pixel_points = []

    for landmark in landmarks:

        x = int(landmark.x * frame_width)
        y = int(landmark.y * frame_height)

        pixel_points.append((x, y))

    return pixel_points
def draw_eye_points(frame, eye_points):
    """
    Draw eye landmark points on the frame.

    Parameters
    ----------
    frame : numpy.ndarray
        Image frame.

    eye_points : list
        List of (x, y) pixel coordinates.
    """

    for point in eye_points:
        cv2.circle(
            frame,            #imaage
            point,            #center
            3,                #radius 
            (0, 255, 0),      #green 
            -1,               #filled circle
        )

    return frame
def calculate_ear(eye_points):
    """
    Calculate the Eye Aspect Ratio (EAR).

    Parameters
    ----------
    eye_points : list
        Six eye landmark pixel coordinates.

    Returns
    -------
    float
        Eye Aspect Ratio.
    """

    p1, p2, p3, p4, p5, p6 = eye_points

    vertical1 = distance.euclidean(p2, p6)
    vertical2 = distance.euclidean(p3, p5)

    horizontal = distance.euclidean(p1, p4)

    ear = (vertical1 + vertical2) / (2.0 * horizontal)

    return ear
MOUTH = [
    61,
    291,
    13,
    14,
    78,
    308,
    81,
    311,
]
def get_mouth_landmarks(face_landmarks):
    return get_eye_landmarks(face_landmarks, MOUTH)
def calculate_mar(mouth_points):

    if len(mouth_points) < 8:
        return 0.0

    left = mouth_points[0]
    right = mouth_points[1]

    top1 = mouth_points[2]
    bottom1 = mouth_points[3]

    top2 = mouth_points[6]
    bottom2 = mouth_points[7]

    horizontal = distance.euclidean(left, right)

    vertical1 = distance.euclidean(top1, bottom1)
    vertical2 = distance.euclidean(top2, bottom2)

    mar = (vertical1 + vertical2) / (2.0 * horizontal)

    return mar