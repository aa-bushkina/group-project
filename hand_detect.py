import threading

import cv2
import mediapipe as mp


def run_until_hand_detected(func):
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False, model_complexity=1, min_detection_confidence=0.75,
                          min_tracking_confidence=0.75, max_num_hands=2)

    cap = cv2.VideoCapture(0)

    print(f"Запустили функцию, которая выключается по обнаружению руки")
    threading.Thread(target=func, daemon=True).start()

    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            # make some signal
            break
        cv2.imshow('Image', img)
        cv2.waitKey(1)
