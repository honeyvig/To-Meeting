import sys
import cv2
import numpy as np
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class VideoChatApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GoToMeeting Clone (Basic)")
        self.setGeometry(100, 100, 640, 480)
        self.layout = QVBoxLayout()

        # Create a label to display the webcam feed
        self.video_label = QLabel(self)
        self.layout.addWidget(self.video_label)

        # Start the webcam feed
        self.capture = cv2.VideoCapture(0)  # Using the default webcam (0)
        if not self.capture.isOpened():
            print("Error: Could not access the webcam.")
            sys.exit()

        # Create a button to stop the meeting (exit the application)
        self.end_button = QPushButton("End Meeting", self)
        self.end_button.clicked.connect(self.close)
        self.layout.addWidget(self.end_button)

        # Set up a timer to periodically update the webcam feed
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(1000 // 30)  # 30 FPS

        self.setLayout(self.layout)

    def update_frame(self):
        ret, frame = self.capture.read()
        if ret:
            # Convert the frame to RGB (from BGR)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to QImage
            h, w, ch = rgb_frame.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_frame.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Display the frame on the label
            self.video_label.setPixmap(QPixmap.fromImage(q_image))

    def close(self):
        self.capture.release()
        super().close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VideoChatApp()
    window.show()
    sys.exit(app.exec_())
