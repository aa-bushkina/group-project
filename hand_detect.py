import cv2
import mediapipe as mp


def run_until_hand_detected():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False, model_complexity=1, min_detection_confidence=0.75,
                          min_tracking_confidence=0.75, max_num_hands=2)

    cap = cv2.VideoCapture(0)
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
