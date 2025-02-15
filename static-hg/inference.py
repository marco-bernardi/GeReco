import cv2 as cv
import numpy as np
import time
import mediapipe as mp
import argparse
from huggingface_hub import hf_hub_download
import os

STATIC_MODEL = "static_gesture_recognizer.task"
REPO_ID = "Seba213/rgb-dhgr-dataset"

recognized_gesture = ""
landmark_list = []

def get_model_path(model_path):
    """Check if the model file exists locally; if not, download it."""
    if model_path and os.path.exists(model_path):
        print(f"Using provided model: {model_path}")
        return os.path.abspath(model_path)  # Usa il percorso assoluto

    default_model_path = os.path.join(os.getcwd(), STATIC_MODEL)

    if os.path.exists(default_model_path):
        print(f"Model already exists: {default_model_path}")
        return os.path.abspath(default_model_path)  # Usa il percorso assoluto

    print("No model path provided. Downloading the model from Hugging Face...")
    downloaded_model = hf_hub_download(repo_id=REPO_ID, filename=STATIC_MODEL, repo_type="dataset")
    print(f"Model downloaded to: {downloaded_model}")
    return os.path.abspath(downloaded_model)  # Usa il percorso assoluto

def gesture_recognition_callback(results: mp.tasks.vision.GestureRecognizerResult,
                                 output_image: mp.Image,
                                 timestamp_ms: int):
    """Callback function that processes gesture recognition results."""
    global recognized_gesture
    global landmark_list

    if results.gestures:
        recognized_gesture = ""
        for gesture in results.gestures:
            recognized_gesture += f"{gesture[0].category_name} ({gesture[0].score:.2f}), "
    else:
        recognized_gesture = "No gesture recognized."

    if results.hand_landmarks:
        landmark_list = results.hand_landmarks

def main(args):
    cap_device = args.device
    cap_width = 960
    cap_height = 540
    
    model_path = get_model_path(args.model)
    print(f"Using model: {model_path}")

    cap = cv.VideoCapture(cap_device)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, cap_height)

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    hands = mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5,
        max_num_hands=2,
    )

    options = mp.tasks.vision.GestureRecognizerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
        running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
        num_hands=2,
        result_callback=gesture_recognition_callback
    )

    with mp.tasks.vision.GestureRecognizer.create_from_options(options) as gesture_recognizer:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            start_time = time.time()

            numpy_frame = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            mp_image_object = mp.Image(
                image_format=mp.ImageFormat.SRGB,
                data=numpy_frame
            )

            frame_timestamp_ms = int((time.time() - start_time) * 1000)

            gesture_recognizer.recognize_async(mp_image_object, timestamp_ms=frame_timestamp_ms)

            results = hands.process(image)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style(),
                    )

            image = cv.flip(image, 1)

            cv.putText(image, f"Gesture: {recognized_gesture}", (10, 700),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv.LINE_AA)

            cv.imshow("Hand Gesture Recognition", image)

            # Exit if the ESC key is pressed.
            if cv.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Hand Gesture Recognition using MediaPipe.')
    parser.add_argument(
        '--model',
        type=str,
        default='',
        help='Path to the gesture recognizer model file.'
    )
    parser.add_argument(
        '--device',
        type=int,
        default=0,
        help='OpenCV device for the webcam (default is 0).'
    )
    args = parser.parse_args()
    main(args)
