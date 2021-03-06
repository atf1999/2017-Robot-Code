from threading import Thread
import time
import numpy as np
import cv2
 
class WebcamVideoStream:
    
    def __init__(self, src=0):

        self.stream = cv2.VideoCapture(src)
        self.frame = np.zeros((240, 320, 3), np.uint8)
        self.stream.read(self.frame)
        self.stopped = False
        
    def start(self):

        Thread(target=self.update, args=()).start()
        return self
 
    def update(self):
	
        while True:	
            if self.stopped:
                self.stream.release()
                return   
            self.stream.read(self.frame)
	
    def read(self):
    
        return self.frame

    def stop(self):

        self.stopped = True

    def release(self):

        self.stopped = True
        self.stream.release()
