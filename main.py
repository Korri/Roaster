import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from views.main import Ui_MainWindow

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

window.showFullScreen()
window.show()
window.setCursor(Qt.BlankCursor)
sys.exit(app.exec_())
