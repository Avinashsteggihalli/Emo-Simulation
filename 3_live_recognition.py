import cv2
import numpy as np
from face_animation import FaceAnimation

# Load trained recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face_model.yml')

# Haarcascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Names mapped to trained IDs
names = ["Unknown", "Avinash"]   # add more if needed

# Start camera
cam = cv2.VideoCapture(0)

# Initialize robot face animation
face = FaceAnimation()

# Prevent repeating animation continuously
last_person = None

while True:

    ret, frame = cam.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(80, 80)
    )

    for (x, y, w, h) in faces:

        # Draw rectangle around face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        # Recognize face
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Determine person name
        if confidence < 80:
            name = names[id]
        else:
            name = "Unknown"

        # Show name on camera window
        cv2.putText(
            frame,
            name,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,255,0),
            2
        )

        # ===== ROBOT REACTION LOGIC =====
        if name != last_person:

            if name != "Unknown":
                print("Recognized:", name)
                face.happy()

            else:
                print("Unknown person")
                face.neutral()

            last_person = name
        # ================================

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)

    if key == 27:  # ESC key to exit
        break


cam.release()
cv2.destroyAllWindows()