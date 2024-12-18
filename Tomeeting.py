import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

class MeetingApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jitsi Meeting Clone")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        self.layout = QVBoxLayout()

        # UI Elements
        self.meeting_name_input = QLineEdit(self)
        self.meeting_name_input.setPlaceholderText("Enter meeting name")
        self.layout.addWidget(self.meeting_name_input)

        self.start_button = QPushButton("Start Meeting", self)
        self.start_button.clicked.connect(self.start_meeting)
        self.layout.addWidget(self.start_button)

        self.join_button = QPushButton("Join Meeting", self)
        self.join_button.clicked.connect(self.join_meeting)
        self.layout.addWidget(self.join_button)

        # Web Engine view for Jitsi meeting
        self.web_view = QWebEngineView(self)
        self.layout.addWidget(self.web_view)

        self.setLayout(self.layout)

    def start_meeting(self):
        meeting_name = self.meeting_name_input.text()
        if meeting_name:
            # Redirect to the Jitsi meeting page with the custom room name
            url = f"https://meet.jit.si/{meeting_name}"
            self.web_view.setUrl(QUrl(url))
        else:
            self.show_error("Please enter a meeting name.")

    def join_meeting(self):
        meeting_name = self.meeting_name_input.text()
        if meeting_name:
            # Redirect to the Jitsi meeting page with the specified room name
            url = f"https://meet.jit.si/{meeting_name}"
            self.web_view.setUrl(QUrl(url))
        else:
            self.show_error("Please enter a meeting name to join.")

    def show_error(self, message):
        error_label = QLabel(message, self)
        self.layout.addWidget(error_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MeetingApp()
    window.show()
    sys.exit(app.exec_())
