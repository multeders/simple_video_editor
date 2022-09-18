from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
from base import Base

class Player(Base):

    def run(self):
        if self.file is not None:
            Capture = cv2.VideoCapture(self.file)
            while Capture.isOpened():
                if self.video_stop:
                    self.video_stop = False
                    break

                ret, frame = Capture.read()
                if ret:
                    frame = self._add_filters(frame)
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    ConvertToQtFormat = QImage(Image.data, Image.shape[1], Image.shape[0],
                                               QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
