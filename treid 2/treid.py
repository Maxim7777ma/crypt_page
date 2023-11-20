from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWebApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Web App")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

    def init_ui(self):
        web_view = QWebEngineView(self)
        web_view.setUrl(QUrl.fromLocalFile("/Users/pk/Desktop/treid/start.html"))  # Замените на путь к вашей веб-странице

        # Включаем поддержку полноэкранного режима
        settings = web_view.settings()
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.setCentralWidget(web_view)

if __name__ == '__main__':
    app = QApplication([])
    mainWin = MyWebApp()
    mainWin.show()
    app.exec()
