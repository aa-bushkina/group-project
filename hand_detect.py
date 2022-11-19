import mediapipe as mp


def run_until_hand_detected():
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(min_detection_confidence=0.75, min_tracking_confidence=0.75, max_num_hands=2)
