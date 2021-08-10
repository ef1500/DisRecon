# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QLineEdit,QPushButton,QLabel
import InviteEngine

qtCreatorFile = "mainwindow.ui"


class Frontend(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi("mainwindow.ui")
        self.ui.show()
        self.ui.pushButton.clicked.connect(self.RunRecon)
    def RunRecon(self):
        info = InviteEngine.InvRecon(str(self.ui.lineEdit.text()))
        if info == 0:
            self.ui.lineEdit.setText("INVALID INVITE")
            return 0
        self.ui.server_id.setText(str(info[0]))
        self.ui.server_name.setText(str(info[1]))
        self.ui.server_veri_level.setText(str(info[2]))
        self.ui.nsfw_level.setText(str(info[3]))
        self.ui.server_vanity.setText(str(info[4]))
        self.ui.server_welcome_msg.setText(str(info[5]))
        if str(info[7]) == "None":
            self.ui.inviter.setText("None")
            self.ui.inviter_id.setText("None")
            self.ui.inviter_avatar.setText("None")
        else:
            self.ui.inviter.setText(str(info[7])+'#'+str(info[8]))
            self.ui.inviter_id.setText(str(info[6]))
            self.ui.inviter_avatar.setText("https://cdn.discordapp.com/avatars/"+str(info[6])+"/"+str(info[9]))


if __name__ == "__main__":
    app = QApplication([])
    window = Frontend()
    sys.exit(app.exec_())
