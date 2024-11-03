import cv2
import mediapipe as mp
import numpy as np


mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def mediapipe_detection(image, holistic):
    """ Perform MediaPipe detection on an image. """
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
    image.flags.writeable = False
    results = holistic.process(image)  
    image.flags.writeable = True  
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  
    return image, results  

def draw_landmarks(image, results):
    """ Draw the landmarks on the image. """
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)
    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

def extract_keypoints(results):
    """ Extract keypoints from the results. """
    keypoints = []

    if results.pose_landmarks:
        for landmark in results.pose_landmarks.landmark:
            keypoints.append([landmark.x, landmark.y, landmark.z]) 
   
    if results.left_hand_landmarks:
        for landmark in results.left_hand_landmarks.landmark:
            keypoints.append([landmark.x, landmark.y, landmark.z])
 
    if results.right_hand_landmarks:
        for landmark in results.right_hand_landmarks.landmark:
            keypoints.append([landmark.x, landmark.y, landmark.z])
    return np.array(keypoints).flatten()  