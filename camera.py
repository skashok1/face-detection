#import face_recognition
from os import path
import cv2
#from db import Database
#from face import Face

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

class VideoCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, image = self.video.read()


		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
		faces_detected= face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

		for (x, y, w, h) in faces_detected:
			cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
        
		frame_flip = cv2.flip(image,1)
		ret, jpeg = cv2.imencode('.jpg', frame_flip)
		return jpeg.tobytes()
