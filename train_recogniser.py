import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

recognizer = cv2.face.LBPHFaceRecognizer_create()

faces = []
labels = []

label_id = 0

for filename in os.listdir("dataset/avinash"):
    img = cv2.imread(f"dataset/avinash/{filename}", cv2.IMREAD_GRAYSCALE)
    faces.append(img)
    labels.append(label_id)

recognizer.train(faces, np.array(labels))
recognizer.save("trainer.yml")

print("Training complete.")
