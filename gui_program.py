import sys
from PyQt5 import QtWidgets, QtCore

class MyUI(object):
    def setup_ui(self, main_window):
        main_window.setObjectName("What is this?")
        main_window.setGeometry(300, 300, 600, 600)
        self.centralwidget = QtWidgets.QPushButton(main_window)
        self.centralwidget.setObjectName("Start")
        self.centralwidget.setGeometry(250, 250, 100, 50)
        self.label = QtWidgets.QLabel(main_window)
        self.label.setGeometry(0, 0, 100, 100)
        self.label.setObjectName("Label")
        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "What is this?"))
        
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = MyUI()
        self.ui.setup_ui(self)
        self.ui.centralwidget.setText("start")
        self.ui.centralwidget.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        self.ui.label.setText("Wake up, Neo...\nThe matrix has you...")
        self.ui.label.adjustSize()
        self.ui.centralwidget.setText("quit")
        self.ui.centralwidget.clicked.connect(self.close)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    application = MyWindow()
    application.show()
    sys.exit(app.exec_())
