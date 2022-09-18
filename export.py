from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import numpy as np
import math
from base import Base

class Export(Base):

    def run(self):
        if self.save_file is not None and self.file is not None:
            Capture = cv2.VideoCapture(self.file)
            frame_width = int(Capture.get(3))
            frame_height = int(Capture.get(4))
            size = (frame_width, frame_height)
            fps = Capture.get(cv2.CAP_PROP_FPS)
            frame_count = int(Capture.get(cv2.CAP_PROP_FRAME_COUNT))
            if Capture is not None:
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(self.save_file, fourcc, fps, size)
                frame_it, percent = 0, 0
                while Capture.isOpened():
                    if self.export_stop:
                        self.export_stop = False
                        self.EndExporting.emit()
                        break

                    ret, frame = Capture.read()
                    if ret:
                        frame = self._add_filters(frame)
                        out.write(frame)
                        if percent != math.floor(frame_it * 100 / frame_count):
                            percent = math.floor(frame_it * 100 / frame_count)
                            self.ExportProcessing.emit("Exporting " + str(percent) + "%")
                    else:
                        self.ExportProcessing.emit("Done !!!")
                        out.release()
                        Capture.release()
                        self.EndExporting.emit()
                        break
                    frame_it += 1
                out.release()
                Capture.release()
