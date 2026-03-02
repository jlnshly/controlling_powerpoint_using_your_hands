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


