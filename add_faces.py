import cv2

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()