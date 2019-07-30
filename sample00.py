"""app with opencv."""

# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time


def main():
    """This is a main function for program."""
    # define the lower and upper boundaries of the "green"
    # ball in the HSV color space
    greenLower = (29, 86, 6)
    greenUpper = (64, 255, 255)

    # initialize the list of tracked points, the frame counter,
    # and the coordinate deltas
    pts = deque(maxlen=64)
    counter = 0
    (dX, dY) = (0, 0)
    direction = ""

    # if a video path was not supplied, grab the reference
    # to the webcam
    vs = cv2.VideoCapture("data/ball_tracking_example.mp4")
    cnt = 0

    time.sleep(2.0)

    frame_count = int(vs.get(cv2.CAP_PROP_FRAME_COUNT))
    print('Frame count:', frame_count)

    while True:
        # cnt = cnt + 1
        vs.set(cv2.CAP_PROP_POS_FRAMES, cnt % frame_count)
        _, frame = vs.read()
        # frame = frame[1]

        if frame is None:
            break

        frame = imutils.resize(frame, width=600)
        blurred = cv2.GaussianBlur(frame, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, greenLower, greenUpper)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)

        center = None
        
            

        cv2.imshow("hsv", hsv)
        cv2.imshow("mask", mask)


        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

        if key == ord('l'):
            cnt = cnt + 1

        if key == ord('j'):
            cnt = cnt - 1


if __name__ == "__main__":
    main()
