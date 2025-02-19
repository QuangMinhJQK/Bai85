import functools
from PyQt6.QtWidgets import QMessageBox, QPushButton

from Baitap.Bai85.ui.Login.MainWindow85 import Ui_MainWindow


class MainWindow85Ext(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def hienthi_sanpham_len_giaodien(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.dssp.list)):
            sp = self.dssp.list[i]
            btn = QPushButton(text=str(sp))
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet, sp))

    def xem_chi_tiet(self, sp):
        pass

    def setupSignalAndSlot(self):
        self.pushButtonRemove.clicked.connect(self.xuly_xoa)
        self.pushButtonSave.clicked.connect(self.xuly_luu)

    def xuly_xoa(self):
        msp=self.lineEditId.text()
        dlg=QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xóa")
        dlg.setText(f"Muốn xóa sản phẩm [{msp}] ư?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button=dlg.exec()
        if button == QMessageBox.StandardButton.No:
            return
        self.dssp.xoa_sanpham_theo_ma(msp)
        self.hienthi_sanpham_len_giaodien()

    def xuly_luu(self):
        pass