import cv2
import os

cap = cv2.VideoCapture("https://192.168.1.47:8080/video")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

os.makedirs("dataset/avinash", exist_ok=True)

count = 0

while count < 30:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        cv2.imwrite(f"dataset/avinash/{count}.jpg", face)
        count += 1

    cv2.imshow("Capturing Faces", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
