# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\marci\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\wtyczka_projekt_gk_lp\wtyczka_projekt_gk_lp_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WtyczkaProjektGKLPDialogBase(object):
    def setupUi(self, WtyczkaProjektGKLPDialogBase):
        WtyczkaProjektGKLPDialogBase.setObjectName("WtyczkaProjektGKLPDialogBase")
        WtyczkaProjektGKLPDialogBase.resize(645, 505)
        self.button_box = QtWidgets.QDialogButtonBox(WtyczkaProjektGKLPDialogBase)
        self.button_box.setGeometry(QtCore.QRect(110, 410, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.label_h = QtWidgets.QLabel(WtyczkaProjektGKLPDialogBase)
        self.label_h.setGeometry(QtCore.QRect(60, 150, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_h.setFont(font)
        self.label_h.setObjectName("label_h")
        self.pushButton_h = QtWidgets.QPushButton(WtyczkaProjektGKLPDialogBase)
        self.pushButton_h.setGeometry(QtCore.QRect(350, 160, 101, 31))
        self.pushButton_h.setObjectName("pushButton_h")
        self.pushButton_p = QtWidgets.QPushButton(WtyczkaProjektGKLPDialogBase)
        self.pushButton_p.setGeometry(QtCore.QRect(350, 270, 101, 31))
        self.pushButton_p.setObjectName("pushButton_p")
        self.label_p = QtWidgets.QLabel(WtyczkaProjektGKLPDialogBase)
        self.label_p.setGeometry(QtCore.QRect(60, 260, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_p.setFont(font)
        self.label_p.setObjectName("label_p")
        self.wybierz_warstwy = QgsMapLayerComboBox(WtyczkaProjektGKLPDialogBase)
        self.wybierz_warstwy.setGeometry(QtCore.QRect(150, 80, 371, 31))
        self.wybierz_warstwy.setObjectName("wybierz_warstwy")
        self.label_w = QtWidgets.QLabel(WtyczkaProjektGKLPDialogBase)
        self.label_w.setGeometry(QtCore.QRect(150, 40, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label_w.setFont(font)
        self.label_w.setObjectName("label_w")
        self.label_wyn_h = QtWidgets.QLabel(WtyczkaProjektGKLPDialogBase)
        self.label_wyn_h.setGeometry(QtCore.QRect(50, 220, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.label_wyn_h.setFont(font)
        self.label_wyn_h.setText("")
        self.label_wyn_h.setObjectName("label_wyn_h")
        self.label_wyn_p = QtWidgets.QLabel(WtyczkaProjektGKLPDialogBase)
        self.label_wyn_p.setGeometry(QtCore.QRect(70, 320, 531, 51))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.label_wyn_p.setFont(font)
        self.label_wyn_p.setText("")
        self.label_wyn_p.setWordWrap(True)
        self.label_wyn_p.setObjectName("label_wyn_p")

        self.retranslateUi(WtyczkaProjektGKLPDialogBase)
        self.button_box.accepted.connect(WtyczkaProjektGKLPDialogBase.accept) # type: ignore
        self.button_box.rejected.connect(WtyczkaProjektGKLPDialogBase.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(WtyczkaProjektGKLPDialogBase)

    def retranslateUi(self, WtyczkaProjektGKLPDialogBase):
        _translate = QtCore.QCoreApplication.translate
        WtyczkaProjektGKLPDialogBase.setWindowTitle(_translate("WtyczkaProjektGKLPDialogBase", "Wtyczka GK LP"))
        self.label_h.setText(_translate("WtyczkaProjektGKLPDialogBase", "Uzyskane przewyzszenie"))
        self.pushButton_h.setText(_translate("WtyczkaProjektGKLPDialogBase", "Oblicz"))
        self.pushButton_p.setText(_translate("WtyczkaProjektGKLPDialogBase", "Oblicz"))
        self.label_p.setText(_translate("WtyczkaProjektGKLPDialogBase", "Uzyskane pole powierzchni"))
        self.label_w.setText(_translate("WtyczkaProjektGKLPDialogBase", "Wybierz warstwe z własciwymi punktami"))
from qgsmaplayercombobox import QgsMapLayerComboBox


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WtyczkaProjektGKLPDialogBase = QtWidgets.QDialog()
    ui = Ui_WtyczkaProjektGKLPDialogBase()
    ui.setupUi(WtyczkaProjektGKLPDialogBase)
    WtyczkaProjektGKLPDialogBase.show()
    sys.exit(app.exec_())
