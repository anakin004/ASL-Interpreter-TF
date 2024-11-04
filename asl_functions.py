# this file is for easier accessability to simply have a baseline for other models
# these are the primary functions used to detect, display, and extract the keypoints.
# These essentially be constant in any related models, besides if you choose not to track face and/or postures


import cv2
import mediapipe as mp
import numpy as np


mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def mediapipe_detection(image,model):
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #converting color
    image.flags.writeable = False
    results = model.process(image)  #detection, prediction
    image.flags.writeable = True 
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR) #converting back
    return image, results

# we are grabbing image, converting its format for model, changing write access for memory saving

def draw_landmarks(image, results):

    if results.left_hand_landmarks:
        mp_drawing.draw_landmarks(image,results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(60,10,10), thickness=1, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(210,206,121), thickness=1, circle_radius=2)
                                    )

    if results.right_hand_landmarks:
        mp_drawing.draw_landmarks(image,results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                        mp_drawing.DrawingSpec(color=(210,200,60), thickness=1, circle_radius=2),
                                        mp_drawing.DrawingSpec(color=(10,256,121), thickness=1, circle_radius=2)
                                        )
    
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(image,results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(98,13,49), thickness=1, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(109,201,0), thickness=1, circle_radius=2)
                                    )
    if results.face_landmarks:   
        mp_drawing.draw_landmarks(image,results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                                    mp_drawing.DrawingSpec(color=(98,13,49), thickness=1, circle_radius=2),
                                    mp_drawing.DrawingSpec(color=(109,201,0), thickness=1, circle_radius=2)
                                    )

def extract_keypoints(result):
    pose = []
    
    if result.pose_landmarks:
        for res in result.pose_landmarks.landmark:
            pose.append(np.array([res.x, res.y, res.z, res.visibility]))
        pose = np.array(pose).flatten()
    else:
        pose = np.zeros(33*4)

    rh = []

    if result.right_hand_landmarks:
        for res in result.right_hand_landmarks.landmark:
            rh.append(np.array([res.x, res.y, res.z]))
        rh = np.array(rh).flatten()
    else:
        rh = np.zeros(21*3)

    lh = []

    if result.left_hand_landmarks:
        for res in result.left_hand_landmarks.landmark:
            lh.append(np.array([res.x, res.y, res.z]))
        lh = np.array(lh).flatten()
    else:
        lh = np.zeros(21*3)

    face = []

    if result.face_landmarks:
        for res in result.face_landmarks.landmark:
            face.append(np.array([res.x, res.y, res.z]))
        face = np.array(face).flatten()
    else:
        face = np.zeros(468*3)

    res = np.concatenate([pose, face, lh, rh])
    return res  # Return the final array
