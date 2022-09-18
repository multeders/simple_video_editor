from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from player import Player
from export import Export
from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self._generate_ui(self)
        self.player_thread = None
        self.export_thread = None
        self.player = None
        self.export = None
        self.export_running = False

    # START GUI
    def _generate_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(915, 500)

        # Create skillet
        self._create_body(MainWindow)

        # Create sliders with labels
        self.label = self._create_label(self.groupBox, QtCore.QRect(10, 60, 101, 17), "label")
        self.brightness_slider = self._create_slider(self.groupBox, QtCore.QRect(10, 90, 241, 16), "brightness_slider")

        self.label_2 = self._create_label(self.groupBox, QtCore.QRect(10, 140, 101, 17), "label_2")
        self.saturation_slider = self._create_slider(self.groupBox, QtCore.QRect(10, 170, 241, 16), "saturation_slider")

        self.label_3 = self._create_label(self.groupBox, QtCore.QRect(10, 220, 101, 17), "label_3")
        self.blur_slider = self._create_slider(self.groupBox, QtCore.QRect(10, 250, 241, 16), "blur_slider")

        self.label_4 = self._create_label(self.groupBox, QtCore.QRect(10, 300, 101, 17), "label_4")
        self.sepia_slider = self._create_slider(self.groupBox, QtCore.QRect(10, 330, 241, 16), "sepia_slider")

        self.label_5 = self._create_label(self.groupBox, QtCore.QRect(10, 390, 101, 17), "label_5")
        self.sharpen_slider = self._create_slider(self.groupBox, QtCore.QRect(10, 420, 241, 16), "sharpen_slider")
        self.sharpen_slider.setMaximum(3)

        # Creating player box
        self.side_scroll_area.setWidget(self.scrollAreaWidgetContents_2)
        self.main_scroll_area = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.main_scroll_area.setGeometry(QtCore.QRect(0, 0, 561, 481))
        self.main_scroll_area.setWidgetResizable(True)
        self.main_scroll_area.setObjectName("main_scroll_area")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 559, 479))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")

        # Creating player buttons
        self.import_butt = self._create_button(self.scrollAreaWidgetContents_3, QtCore.QRect(10, 10, 89, 25), "import_butt")
        self.import_butt.clicked.connect(self._import_file)

        self.export_butt = self._create_button(self.scrollAreaWidgetContents_3, QtCore.QRect(120, 10, 89, 25), "export_butt")
        self.export_butt.clicked.connect(self._export_file)

        self.play_butt = self._create_button(self.scrollAreaWidgetContents_3, QtCore.QRect(10, 430, 101, 25), "play_butt")
        self.play_butt.clicked.connect(self._play)

        self.stop_butt = self._create_button(self.scrollAreaWidgetContents_3, QtCore.QRect(120, 430, 71, 25), "stop_butt")
        self.stop_butt.clicked.connect(self._stop)

        # Create video player
        self.main_player = self._create_label(self.scrollAreaWidgetContents_3, QtCore.QRect(10, 70, 541, 361), "main_player")
        self.main_player.setText("Please import MP4 file")
        self.main_player.setAlignment(QtCore.Qt.AlignCenter)

        self.main_scroll_area.setWidget(self.scrollAreaWidgetContents_3)
        self.main_area.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.main_area)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def _create_slider(self, groupBox, rect, title):
        slider = QtWidgets.QSlider(groupBox)
        slider.setGeometry(rect)
        slider.setOrientation(QtCore.Qt.Horizontal)
        slider.setObjectName(title)
        return slider

    def _create_label(self, groupBox, rect, title):
        label = QtWidgets.QLabel(groupBox)
        label.setGeometry(rect)
        label.setObjectName(title)
        return label

    def _create_button(self, groupBox, rect, title):
        button = QtWidgets.QPushButton(groupBox)
        button.setGeometry(rect)
        button.setObjectName(title)
        return button

    def _create_body(self, MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 891, 481))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_area = QtWidgets.QScrollArea(self.horizontalLayoutWidget)
        self.main_area.setWidgetResizable(True)
        self.main_area.setObjectName("main_area")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 887, 477))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.side_scroll_area = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.side_scroll_area.setGeometry(QtCore.QRect(620, 0, 271, 481))
        self.side_scroll_area.setWidgetResizable(True)
        self.side_scroll_area.setObjectName("side_scroll_area")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 269, 479))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 271, 481))
        self.groupBox.setObjectName("groupBox")
    # END GUI

    # START FUNCTIONALITY
    def _import_file(self):
        path = QFileDialog.getOpenFileName(self, caption='Open a file', filter="MP4 files (*.mp4)")
        if path != ('', ''):
            self.player = Player(self.brightness_slider, self.saturation_slider, self.blur_slider,
                                 self.sepia_slider, self.sharpen_slider)
            self.player.set_path(path[0])
            self.player_thread = QtCore.QThread()
            self.player.moveToThread(self.player_thread)
            self.player_thread.started.connect(self.player.run)
            self.player.ImageUpdate.connect(self.ImageUpdateSlot)
            if not self.player_thread.isRunning():
                self.player_thread.start()

    def _export_file(self):
        if not self.export_running:
            path = QFileDialog.getSaveFileName(self, caption='Save a file', filter="MP4 files (*.mp4)")
            if path != ('', ''):

                if self.player_thread.isRunning():
                    self._stop()

                self.export = Export(self.brightness_slider, self.saturation_slider, self.blur_slider,
                                     self.sepia_slider, self.sharpen_slider)
                self.export.set_save_path(path[0])
                self.export.set_path(self.player.get_path())
                self.export_thread = QtCore.QThread()
                self.export.moveToThread(self.export_thread)
                self.export_thread.started.connect(self.export.run)
                self.export.ExportProcessing.connect(self.ExportProcessingSlot)
                self.export.EndExporting.connect(self.EndExportingSlot)
                if not self.export_thread.isRunning():
                    self.export_thread.start()
                    self.DisableButtons()
                    self.export_running = True
        else:
            if self.export is not None:
                self.export.stop_export()
            self.EnableButtons()

    def _play(self):
        if self.player is None or self.player_thread is None:
            return
        if not self.player_thread.isRunning():
            self.player_thread.start()

    def _stop(self):
        if self.player is None or self.player_thread is None:
            return
        if self.player_thread.isRunning():
            self.player.stop_video()
            self.player_thread.quit()

    def DisableButtons(self):
        self.import_butt.setEnabled(False)
        self.play_butt.setEnabled(False)
        self.stop_butt.setEnabled(False)
        self.export_butt.setText("Stop export")

    def EnableButtons(self):
        self.import_butt.setEnabled(True)
        self.play_butt.setEnabled(True)
        self.stop_butt.setEnabled(True)
        self.export_butt.setText("Export")
        self.export_running = False
        self.main_player.setText("Please import MP4 file")
        if self.export_thread is not None and self.export_thread.isRunning():
            self.export_thread.quit()

    # END FUNCTIONALITY

    # START SLOTS
    def ImageUpdateSlot(self, Image):
        self.main_player.setPixmap(QPixmap.fromImage(Image))

    def ExportProcessingSlot(self, text):
        self.main_player.setText(text)

    def EndExportingSlot(self):
        self.EnableButtons()
    # END SLOTS

    # TRANSLATE
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Effects"))
        self.label.setText(_translate("MainWindow", "Brightness"))
        self.label_2.setText(_translate("MainWindow", "Saturation"))
        self.label_3.setText(_translate("MainWindow", "Blur"))
        self.label_4.setText(_translate("MainWindow", "Sepia"))
        self.label_5.setText(_translate("MainWindow", "Sharpen"))
        self.import_butt.setText(_translate("MainWindow", "Import"))
        self.export_butt.setText(_translate("MainWindow", "Export"))
        self.play_butt.setText(_translate("MainWindow", "Play"))
        self.stop_butt.setText(_translate("MainWindow", "Stop"))
