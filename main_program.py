import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.user_hands
user_hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
)
mp_draw = mp.solutions.drawing_utils

video_capture = cv2.VideoCapture(0)

prev_action_time = 0
cooldown_time = 1.0
status_text = "Waiting for gesture..."

def count_fingers(hand_landmarks):

    finger_tips = [8, 12, 16, 20]
    raised_fingers = 0

    for tip in finger_tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip -2].y:
            raised_fingers += 1

    if hand_landmarks.landmarks[4].x < hand_landmarks.landmarks[3].x:
        raised_fingers += 1

    return raised_fingers

while True:

    ret, frame = video_capture.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = user_hands.process(rgb_image)
    current_time = time.time()




