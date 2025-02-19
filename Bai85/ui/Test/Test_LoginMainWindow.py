from PyQt6.QtWidgets import QApplication, QMainWindow

from Baitap.Bai85.ui.Login.Login_MainWindow85Ext import LoginMainWindowExt

app=QApplication([])
MainWindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(MainWindow)
myui.showWindow()
app.exec()