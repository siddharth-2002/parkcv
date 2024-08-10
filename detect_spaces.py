import cv2
import numpy as np

# Load pre-trained model for space detection
def detect_spaces(frame):
    # Dummy implementation for space detection
    # In practice, you would use a trained model or algorithm here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    spaces_detected = len(contours)  # Simple count of detected spaces
    return spaces_detected

# Capture video from camera
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    spaces = detect_spaces(frame)
    print(f'Available Spaces: {spaces}')
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
