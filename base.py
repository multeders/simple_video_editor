from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2
import numpy as np

class Base(QObject):
    ImageUpdate = pyqtSignal(QImage)
    ExportProcessing = pyqtSignal(str)
    EndExporting = pyqtSignal()

    def __init__(self, brightness_slider, saturation_slider, blur_slider, sepia_slider, sharpen_slider):
        super().__init__()
        self.file = None
        self.save_file = None
        self.video_stop = False
        self.export_stop = False
        self.brightness_slider = brightness_slider
        self.saturation_slider = saturation_slider
        self.blur_slider = blur_slider
        self.sepia_slider = sepia_slider
        self.sharpen_slider = sharpen_slider

    # START GETTERS/SETTERS
    def set_path(self, file):
        self.file = file

    def get_path(self):
        return self.file

    def set_save_path(self, file):
        self.save_file = file
    # END GETTERS/SETTERS

    # START FUNCTIONALITY
    def stop(self):
        self.quit()

    def stop_video(self):
        self.video_stop = True

    def stop_export(self):
        self.export_stop = True
    # END FUNCTIONALITY

    # START FILTERS
    def _add_filters(self, frame):
        frame = self._change_brightness(frame, self.brightness_slider.value())
        frame = self._change_saturation(frame, self.saturation_slider.value())
        frame = self._change_blur(frame, self.blur_slider.value())
        frame = self._change_sepia(frame, self.sepia_slider.value())
        frame = self._change_sharpen(frame, self.sharpen_slider.value())
        return frame

    def _change_brightness(self, img, value):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - value
        v[v > lim] = 255
        v[v <= lim] += value

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    def _change_saturation(self, img, value):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        lim = 255 - value
        s[s > lim] = 255
        s[s <= lim] += value

        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img

    def _change_blur(self, img, value):
        return img if value == 0 else cv2.blur(img, (value, value))

    def _change_sepia(self, src_image, value):
        if value == 0:
            return src_image
        gray = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
        normalized_gray = np.array(gray, np.float32) / 255
        # solid color
        sepia = np.ones(src_image.shape)
        sepia[:, :, 0] *= 155 + value  # B
        sepia[:, :, 1] *= 255 - value  # G
        sepia[:, :, 2] *= 100 + value  # R
        # hadamard
        sepia[:, :, 0] *= normalized_gray  # B
        sepia[:, :, 1] *= normalized_gray  # G
        sepia[:, :, 2] *= normalized_gray  # R
        return np.array(sepia, np.uint8)

    def _change_sharpen(self, img, value):
        if value == 1:
            return cv2.filter2D(src=img, ddepth=-1, kernel=np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
        elif value == 2:
            return cv2.filter2D(src=img, ddepth=-1, kernel=np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]))
        elif value == 2:
            return cv2.filter2D(src=img, ddepth=-1, kernel=np.array([[4, -1, 4], [1, 5, -1], [2, -1, 0]]))

        return img
