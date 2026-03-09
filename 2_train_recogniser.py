import cv2
import os
import numpy as np

dataset_path = "dataset"

faces = []
labels = []
label_map = {}

label_id = 0

for person in os.listdir(dataset_path):

    person_path = os.path.join(dataset_path, person)

    if not os.path.isdir(person_path):
        continue

    label_map[label_id] = person

    for image in os.listdir(person_path):

        img_path = os.path.join(person_path, image)

        face = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        faces.append(face)
        labels.append(label_id)

    label_id += 1


recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.train(faces, np.array(labels))

recognizer.save("face_model.yml")

np.save("labels.npy", label_map)

print("Training complete.")