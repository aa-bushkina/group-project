import threading

import cv2
import mediapipe as mp


# Run it in a separate thread
def run_until_hand_detected(func):
    # Initializing the Model
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(static_image_mode=False, model_complexity=1, min_detection_confidence=0.75,
                          min_tracking_confidence=0.75, max_num_hands=2)

    # Start capturing video from webcam
    cap = cv2.VideoCapture(0)

    print(f"Запустили функцию, которая выключается по обнаружению руки")
    threading.Thread(target=func, daemon=True).start()

    while True:
        # Read video frame by frame
        success, img = cap.read()

        # Flip the image(frame)
        img = cv2.flip(img, 1)

        # If hands are present in image(frame)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            # make some signal TODO
            break
        # cv2.imshow('Image', img)
        cv2.waitKey(1)
