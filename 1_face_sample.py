import cv2
import mediapipe as mp
import os
import time

person_name = "Avinash"
save_path = f"dataset/{person_name}"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True)

directions = ["CENTER","LEFT","RIGHT","UP","DOWN"]

images_per_direction = 5
img_count = 0


def get_head_direction(landmarks, w, h):

    nose = landmarks[1]
    left_eye = landmarks[33]
    right_eye = landmarks[263]
    chin = landmarks[152]

    nx, ny = int(nose.x*w), int(nose.y*h)
    lx = int(left_eye.x*w)
    rx = int(right_eye.x*w)
    cy = int(chin.y*h)

    # left/right
    if nx < lx:
        return "LEFT"
    if nx > rx:
        return "RIGHT"

    # up/down
    if ny < h*0.35:
        return "UP"
    if cy > h*0.75:
        return "DOWN"

    return "CENTER"


for direction in directions:

    captured = 0

    while captured < images_per_direction:

        ret, frame = cap.read()
        if not ret:
            print("Open camera lid")
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb)

        cv2.putText(frame,
                    f"Turn {direction}",
                    (30,40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,255),
                    2)

        if result.multi_face_landmarks:

            landmarks = result.multi_face_landmarks[0].landmark

            h,w,_ = frame.shape

            orientation = get_head_direction(landmarks,w,h)

            cv2.putText(frame,
                        f"Detected: {orientation}",
                        (30,80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,255,0),
                        2)

            if orientation == direction:

                for i in range(3,0,-1):

                    ret2, frame2 = cap.read()

                    cv2.putText(frame2,
                                f"Capturing in {i}",
                                (200,200),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                2,
                                (0,255,0),
                                4)

                    cv2.imshow("Dataset Capture",frame2)
                    cv2.waitKey(1000)

                face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face = cv2.resize(face,(200,200))

                cv2.imwrite(f"{save_path}/{img_count}.jpg",face)

                img_count += 1
                captured += 1

        else:

            cv2.putText(frame,
                        "Show face to camera",
                        (30,80),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,0,255),
                        2)

        cv2.imshow("Dataset Capture",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
# import mediapipe as mp
# print(mp.__version__)
# print(hasattr(mp, "solutions"))