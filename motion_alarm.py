import cv2
import numpy as np
import RPi.GPIO as GPIO
from datetime import datetime
import time

# GPIO Setup
LED_PIN = 18
BUZZER_PIN = 23
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
GPIO.output(BUZZER_PIN, GPIO.LOW)

# Camera Setup
cap = cv2.VideoCapture(0)

# Initialize first frame
ret, frame1 = cap.read()
if not ret:
    print("Camera not detected!")
    exit()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

motion_active = False  # Prevent continuous retrigger

try:
    while True:
        ret, frame2 = cap.read()
        if not ret:
            continue

        gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        delta = cv2.absdiff(frame1_gray, gray)
        thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion = any(cv2.contourArea(c) > 800 for c in contours)

        if motion and not motion_active:
            motion_active = True
            print("Motion Detected!")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            cv2.imwrite(f"motion_{timestamp}.jpg", frame2)

            with open("motion_log.txt", "a") as f:
                f.write(f"Motion detected at {timestamp}\n")

            # LED blink and buzzer ON for 1 sec
            GPIO.output(LED_PIN, GPIO.HIGH)
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_PIN, GPIO.LOW)
            GPIO.output(BUZZER_PIN, GPIO.LOW)

        if not motion:
            motion_active = False  # Reset for next detection

        cv2.imshow("Security Camera", frame2)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        frame1_gray = gray

except KeyboardInterrupt:
    print("Stopped by User")

finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
