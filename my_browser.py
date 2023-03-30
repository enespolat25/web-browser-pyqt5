from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

class Browser(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.url_edit = QLineEdit()
        self.url_edit.setStyleSheet('QLineEdit {background-color: #A3C1DA; color: red;}')
        self.url_edit.setPlaceholderText('Enter URL or search term...')
        self.back_button = QPushButton('<')
        self.back_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.forward_button = QPushButton('>')
        self.forward_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.reload_button = QPushButton('Reload')
        self.reload_button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')
        self.web_view = QWebEngineView()

    def create_layout(self):
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.back_button)
        top_layout.addWidget(self.forward_button)
        top_layout.addWidget(self.reload_button)
        top_layout.addWidget(self.url_edit)
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.web_view)
        self.setLayout(main_layout)

    def create_connections(self):
        self.back_button.clicked.connect(self.web_view.back)
        self.forward_button.clicked.connect(self.web_view.forward)
        self.reload_button.clicked.connect(self.web_view.reload)
        self.url_edit.returnPressed.connect(self.load_url)
        self.web_view.urlChanged.connect(self.update_url_edit)
    
    def load_url(self):
        url = self.url_edit.text()
        if '://' not in url:
            url = 'http://' + url
        self.web_view.load(QUrl(url))

    def update_url_edit(self, url):
        self.url_edit.setText(url.toString())

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())
