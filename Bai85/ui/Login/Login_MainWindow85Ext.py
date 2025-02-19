from PyQt6.QtWidgets import QMainWindow, QMessageBox

from Baitap.Bai85.Libs.DataConnector import DataConnector
from Baitap.Bai85.ui.Login.MainWindow85 import Ui_MainWindow
from Baitap.Bai85.ui.Login.MainWindow85Ext import MainWindow85Ext


class LoginMainWindowExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButton_save.clicked.connect(self.process_login)
    def process_login(self):
        dc=DataConnector()
        uid = self.lineEdit_Username.text()
        pwd = self.lineEdit_Password.text()
        emp = dc.login(uid,pwd)
        if emp != None:
            self.MainWindow.close()#close login window
            self.mainwindow = QMainWindow()
            self.myui = MainWindow85Ext()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()
