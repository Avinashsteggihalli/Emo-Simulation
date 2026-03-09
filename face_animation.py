import cv2
import numpy as np
import time


class FaceAnimation:

    def __init__(self, width=480, height=480):
        self.width = width
        self.height = height

    def _create_screen(self):
        return np.zeros((self.height, self.width, 3), dtype=np.uint8)

    def _draw_eyes(self, screen, blink=False):

        eye_y = int(self.height * 0.35)

        left_eye = (int(self.width * 0.3), eye_y)
        right_eye = (int(self.width * 0.7), eye_y)

        if blink:
            cv2.line(screen,(left_eye[0]-30,eye_y),(left_eye[0]+30,eye_y),(255,255,255),4)
            cv2.line(screen,(right_eye[0]-30,eye_y),(right_eye[0]+30,eye_y),(255,255,255),4)
        else:
            cv2.circle(screen,left_eye,25,(255,255,255),-1)
            cv2.circle(screen,right_eye,25,(255,255,255),-1)

    def _draw_mouth(self, screen, smile=True):

        center = (self.width//2, int(self.height*0.65))

        if smile:
            cv2.ellipse(screen, center,(80,40),0,0,180,(255,255,255),4)
        else:
            cv2.line(screen,(center[0]-60,center[1]),(center[0]+60,center[1]),(255,255,255),4)

    def happy(self):

        for i in range(12):

            screen = self._create_screen()
            blink = (i % 5 == 0)

            self._draw_eyes(screen, blink)
            self._draw_mouth(screen, True)

            cv2.imshow("Robot Face", screen)
            cv2.waitKey(1)

            time.sleep(0.15)

    def neutral(self):

        screen = self._create_screen()

        self._draw_eyes(screen)
        self._draw_mouth(screen, False)

        cv2.imshow("Robot Face", screen)
        cv2.waitKey(1)