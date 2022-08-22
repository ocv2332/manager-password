# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 325)
        MainWindow.setStyleSheet("QWidget[objectName=\"centralwidget\"],\n"
"QWidget[objectName=\"main_page\"],\n"
"QWidget[objectName=\"view_page\"],\n"
"QWidget[objectName=\"choice_change_page\"],\n"
"QWidget[objectName=\"change_page\"],\n"
"QWidget[objectName=\"append_page\"],\n"
"QWidget[objectName=\"delete_page\"] { background-color: #16161A }\n"
"\n"
"\n"
"QLabel[objectName=\"choice\"],\n"
"QLabel[objectName=\"viewing_title\"],\n"
"QLabel[objectName=\"user_text\"],\n"
"QLabel[objectName=\"user_name\"],\n"
"QLabel[objectName=\"password_text\"],\n"
"QLabel[objectName=\"user_change_text\"],\n"
"QLabel[objectName=\"add_password_text\"],\n"
"QLabel[objectName=\"add_user_text\"],\n"
"QLabel[objectName=\"add_url_text\"],\n"
"QLabel[objectName=\"update_text\"] {padding: 4px; color: #ffffff }\n"
"\n"
"\n"
"QFrame[objectName=\"check_user\"],\n"
"QFrame[objectName=\"check_password\"], \n"
"QFrame[objectName=\"change_user\"],\n"
"QFrame[objectName=\"change_password\"],\n"
"QFrame[objectName=\"add_user\"],\n"
"QFrame[objectName=\"add_password\"],\n"
"QFrame[objectName=\"add_url\"],\n"
"QFrame[objectName=\"update\"] { border: 2px solid #72757E; border-radius: 10px; }\n"
"\n"
"\n"
"QTextEdit[objectName=\"password_name\"],\n"
"QTextEdit[objectName=\"change_name\"],\n"
"QTextEdit[objectName=\"user_change_name\"] {\n"
"    color: #FFFFFF;\n"
"    padding-top: 10px;\n"
"    border-radius: 2px;\n"
"    border-top: 2px solid #72757E ;\n"
"    border-bottom: 2px solid #72757E;\n"
"    background-color: #16161A \n"
"}\n"
"\n"
"\n"
"QLineEdit[objectName=\"add_password_name\"],\n"
"QLineEdit[objectName=\"add_user_name\"],\n"
"QLineEdit[objectName=\"add_url_name\"],\n"
"QLineEdit[objectName=\"update_name\"] {\n"
"    color: #FFFFFF;\n"
"    padding-right: 10px;\n"
"    border-radius: 2px;\n"
"    border-top: 2px solid #72757E ;\n"
"    border-bottom: 2px solid #72757E;\n"
"    background-color: #16161A \n"
"}\n"
"\n"
"\n"
"QPushButton[objectName=\"add_push\"],\n"
"QPushButton[objectName=\"add_push_2\"],\n"
"QPushButton[objectName=\"change_push\"],\n"
"QPushButton[objectName=\"delete_push\"],\n"
"QPushButton[objectName=\"delete_push_2\"],\n"
"QPushButton[objectName=\"view_push\"],\n"
"QPushButton[objectName=\"further_push\"],\n"
"QPushButton[objectName=\"generation_push\"],\n"
"QPushButton[objectName=\"update_push\"],\n"
"QPushButton[objectName=\"back_push\"],\n"
"QPushButton[objectName=\"back_push_2\"],\n"
"QPushButton[objectName=\"back_push_3\"],\n"
"QPushButton[objectName=\"back_push_4\"],\n"
"QPushButton[objectName=\"refresh_push\"] {\n"
"    background-color: transparent;    \n"
"\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 491, 321))
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.main_tittle = QtWidgets.QLabel(self.main_page)
        self.main_tittle.setGeometry(QtCore.QRect(10, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.main_tittle.setFont(font)
        self.main_tittle.setAlignment(QtCore.Qt.AlignCenter)
        self.main_tittle.setObjectName("main_tittle")
        self.choice_combo = QtWidgets.QComboBox(self.main_page)
        self.choice_combo.setGeometry(QtCore.QRect(140, 100, 181, 31))
        self.choice_combo.setObjectName("choice_combo")
        self.choice_combo.addItem("")
        self.add_push = QtWidgets.QPushButton(self.main_page)
        self.add_push.setGeometry(QtCore.QRect(140, 200, 31, 31))
        self.add_push.setMinimumSize(QtCore.QSize(31, 31))
        self.add_push.setMaximumSize(QtCore.QSize(31, 31))
        self.add_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_push.setText("")
        self.add_push.setObjectName("add_push")
        self.change_push = QtWidgets.QPushButton(self.main_page)
        self.change_push.setGeometry(QtCore.QRect(220, 200, 31, 31))
        self.change_push.setMinimumSize(QtCore.QSize(31, 31))
        self.change_push.setMaximumSize(QtCore.QSize(31, 31))
        self.change_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.change_push.setObjectName("change_push")
        self.delete_push = QtWidgets.QPushButton(self.main_page)
        self.delete_push.setGeometry(QtCore.QRect(300, 200, 31, 31))
        self.delete_push.setMinimumSize(QtCore.QSize(31, 31))
        self.delete_push.setMaximumSize(QtCore.QSize(31, 31))
        self.delete_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_push.setObjectName("delete_push")
        self.view_push = QtWidgets.QPushButton(self.main_page)
        self.view_push.setGeometry(QtCore.QRect(220, 150, 31, 31))
        self.view_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.view_push.setText("")
        self.view_push.setObjectName("view_push")
        self.view_icon = QtWidgets.QLabel(self.main_page)
        self.view_icon.setGeometry(QtCore.QRect(220, 150, 31, 31))
        self.view_icon.setMinimumSize(QtCore.QSize(31, 31))
        self.view_icon.setMaximumSize(QtCore.QSize(31, 31))
        self.view_icon.setText("")
        self.view_icon.setPixmap(QtGui.QPixmap("../icons/view_push.png"))
        self.view_icon.setScaledContents(True)
        self.view_icon.setObjectName("view_icon")
        self.add_icon = QtWidgets.QLabel(self.main_page)
        self.add_icon.setGeometry(QtCore.QRect(140, 200, 31, 31))
        self.add_icon.setMinimumSize(QtCore.QSize(31, 31))
        self.add_icon.setMaximumSize(QtCore.QSize(31, 31))
        self.add_icon.setText("")
        self.add_icon.setPixmap(QtGui.QPixmap("../icons/add_push.png"))
        self.add_icon.setScaledContents(True)
        self.add_icon.setObjectName("add_icon")
        self.change_icon = QtWidgets.QLabel(self.main_page)
        self.change_icon.setGeometry(QtCore.QRect(220, 200, 31, 31))
        self.change_icon.setMinimumSize(QtCore.QSize(31, 31))
        self.change_icon.setMaximumSize(QtCore.QSize(31, 31))
        self.change_icon.setText("")
        self.change_icon.setPixmap(QtGui.QPixmap("../icons/change_push.png"))
        self.change_icon.setScaledContents(True)
        self.change_icon.setObjectName("change_icon")
        self.delete_icon = QtWidgets.QLabel(self.main_page)
        self.delete_icon.setGeometry(QtCore.QRect(300, 200, 31, 31))
        self.delete_icon.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.delete_icon.setPixmap(QtGui.QPixmap("../icons/delete_push.png"))
        self.delete_icon.setScaledContents(True)
        self.delete_icon.setObjectName("delete_icon")
        self.refresh_push = QtWidgets.QPushButton(self.main_page)
        self.refresh_push.setGeometry(QtCore.QRect(340, 100, 31, 31))
        self.refresh_push.setMinimumSize(QtCore.QSize(31, 31))
        self.refresh_push.setMaximumSize(QtCore.QSize(31, 31))
        self.refresh_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_push.setObjectName("refresh_push")
        self.refresh_icon = QtWidgets.QLabel(self.main_page)
        self.refresh_icon.setGeometry(QtCore.QRect(340, 100, 31, 31))
        self.refresh_icon.setMinimumSize(QtCore.QSize(31, 31))
        self.refresh_icon.setMaximumSize(QtCore.QSize(31, 31))
        self.refresh_icon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.refresh_icon.setPixmap(QtGui.QPixmap("../icons/refresh_push.png"))
        self.refresh_icon.setScaledContents(True)
        self.refresh_icon.setObjectName("refresh_icon")
        self.delete_icon.raise_()
        self.change_icon.raise_()
        self.view_icon.raise_()
        self.add_icon.raise_()
        self.main_tittle.raise_()
        self.choice_combo.raise_()
        self.add_push.raise_()
        self.change_push.raise_()
        self.delete_push.raise_()
        self.view_push.raise_()
        self.refresh_icon.raise_()
        self.refresh_push.raise_()
        self.stackedWidget.addWidget(self.main_page)
        self.view_page = QtWidgets.QWidget()
        self.view_page.setObjectName("view_page")
        self.check_user = QtWidgets.QFrame(self.view_page)
        self.check_user.setGeometry(QtCore.QRect(10, 90, 481, 41))
        self.check_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.check_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.check_user.setObjectName("check_user")
        self.user_text = QtWidgets.QLabel(self.check_user)
        self.user_text.setGeometry(QtCore.QRect(0, 0, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_text.setFont(font)
        self.user_text.setObjectName("user_text")
        self.user_name = QtWidgets.QLabel(self.check_user)
        self.user_name.setGeometry(QtCore.QRect(180, 0, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_name.setFont(font)
        self.user_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.user_name.setObjectName("user_name")
        self.viewing_title = QtWidgets.QLabel(self.view_page)
        self.viewing_title.setGeometry(QtCore.QRect(0, 20, 491, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.viewing_title.setFont(font)
        self.viewing_title.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.viewing_title.setObjectName("viewing_title")
        self.check_password = QtWidgets.QFrame(self.view_page)
        self.check_password.setGeometry(QtCore.QRect(10, 160, 481, 51))
        self.check_password.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.check_password.setFrameShadow(QtWidgets.QFrame.Raised)
        self.check_password.setObjectName("check_password")
        self.password_text = QtWidgets.QLabel(self.check_password)
        self.password_text.setGeometry(QtCore.QRect(0, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password_text.setFont(font)
        self.password_text.setObjectName("password_text")
        self.password_name = QtWidgets.QTextEdit(self.check_password)
        self.password_name.setGeometry(QtCore.QRect(130, 0, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.password_name.setFont(font)
        self.password_name.setReadOnly(True)
        self.password_name.setObjectName("password_name")
        self.back_push = QtWidgets.QPushButton(self.view_page)
        self.back_push.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_push.setMinimumSize(QtCore.QSize(31, 31))
        self.back_push.setMaximumSize(QtCore.QSize(31, 31))
        self.back_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_push.setText("")
        self.back_push.setObjectName("back_push")
        self.back_icon = QtWidgets.QLabel(self.view_page)
        self.back_icon.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_icon.setMinimumSize(QtCore.QSize(31, 31))
        self.back_icon.setMaximumSize(QtCore.QSize(31, 31))
        self.back_icon.setPixmap(QtGui.QPixmap("../icons/back_push.png"))
        self.back_icon.setScaledContents(True)
        self.back_icon.setObjectName("back_icon")
        self.back_icon.raise_()
        self.check_user.raise_()
        self.viewing_title.raise_()
        self.check_password.raise_()
        self.back_push.raise_()
        self.stackedWidget.addWidget(self.view_page)
        self.append_page = QtWidgets.QWidget()
        self.append_page.setObjectName("append_page")
        self.add_user = QtWidgets.QFrame(self.append_page)
        self.add_user.setGeometry(QtCore.QRect(10, 150, 481, 51))
        self.add_user.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_user.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_user.setObjectName("add_user")
        self.add_user_text = QtWidgets.QLabel(self.add_user)
        self.add_user_text.setGeometry(QtCore.QRect(0, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_user_text.setFont(font)
        self.add_user_text.setObjectName("add_user_text")
        self.add_user_name = QtWidgets.QLineEdit(self.add_user)
        self.add_user_name.setGeometry(QtCore.QRect(160, 0, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_user_name.setFont(font)
        self.add_user_name.setObjectName("add_user_name")
        self.add_password = QtWidgets.QFrame(self.append_page)
        self.add_password.setGeometry(QtCore.QRect(10, 220, 481, 51))
        self.add_password.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_password.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_password.setObjectName("add_password")
        self.add_password_text = QtWidgets.QLabel(self.add_password)
        self.add_password_text.setGeometry(QtCore.QRect(0, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_password_text.setFont(font)
        self.add_password_text.setObjectName("add_password_text")
        self.add_password_name = QtWidgets.QLineEdit(self.add_password)
        self.add_password_name.setGeometry(QtCore.QRect(130, 0, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_password_name.setFont(font)
        self.add_password_name.setObjectName("add_password_name")
        self.generation_push = QtWidgets.QPushButton(self.add_password)
        self.generation_push.setGeometry(QtCore.QRect(440, 10, 31, 31))
        self.generation_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generation_push.setObjectName("generation_push")
        self.generation_icon = QtWidgets.QLabel(self.add_password)
        self.generation_icon.setGeometry(QtCore.QRect(440, 10, 31, 31))
        self.generation_icon.setMinimumSize(QtCore.QSize(31, 31))
        self.generation_icon.setMaximumSize(QtCore.QSize(31, 31))
        self.generation_icon.setPixmap(QtGui.QPixmap("../icons/generation_push.png"))
        self.generation_icon.setScaledContents(True)
        self.generation_icon.setObjectName("generation_icon")
        self.generation_icon.raise_()
        self.add_password_text.raise_()
        self.add_password_name.raise_()
        self.generation_push.raise_()
        self.add_url = QtWidgets.QFrame(self.append_page)
        self.add_url.setGeometry(QtCore.QRect(10, 90, 481, 51))
        self.add_url.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.add_url.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_url.setObjectName("add_url")
        self.add_url_text = QtWidgets.QLabel(self.add_url)
        self.add_url_text.setGeometry(QtCore.QRect(0, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.add_url_text.setFont(font)
        self.add_url_text.setObjectName("add_url_text")
        self.add_url_name = QtWidgets.QLineEdit(self.add_url)
        self.add_url_name.setGeometry(QtCore.QRect(160, 0, 311, 51))
        self.add_url_name.setObjectName("add_url_name")
        self.add_push_2 = QtWidgets.QPushButton(self.append_page)
        self.add_push_2.setGeometry(QtCore.QRect(230, 280, 31, 31))
        self.add_push_2.setMinimumSize(QtCore.QSize(31, 31))
        self.add_push_2.setMaximumSize(QtCore.QSize(31, 31))
        self.add_push_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_push_2.setObjectName("add_push_2")
        self.add_icon_2 = QtWidgets.QLabel(self.append_page)
        self.add_icon_2.setGeometry(QtCore.QRect(230, 280, 31, 31))
        self.add_icon_2.setMinimumSize(QtCore.QSize(31, 31))
        self.add_icon_2.setMaximumSize(QtCore.QSize(31, 31))
        self.add_icon_2.setPixmap(QtGui.QPixmap("../icons/add_push_2.png"))
        self.add_icon_2.setScaledContents(True)
        self.add_icon_2.setObjectName("add_icon_2")
        self.back_push_2 = QtWidgets.QPushButton(self.append_page)
        self.back_push_2.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_push_2.setMinimumSize(QtCore.QSize(31, 31))
        self.back_push_2.setMaximumSize(QtCore.QSize(31, 31))
        self.back_push_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_push_2.setObjectName("back_push_2")
        self.back_icon_2 = QtWidgets.QLabel(self.append_page)
        self.back_icon_2.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_icon_2.setMinimumSize(QtCore.QSize(31, 31))
        self.back_icon_2.setMaximumSize(QtCore.QSize(30, 31))
        self.back_icon_2.setPixmap(QtGui.QPixmap("../icons/back_push.png"))
        self.back_icon_2.setScaledContents(True)
        self.back_icon_2.setObjectName("back_icon_2")
        self.add_icon_2.raise_()
        self.back_icon_2.raise_()
        self.add_user.raise_()
        self.add_password.raise_()
        self.add_url.raise_()
        self.add_push_2.raise_()
        self.back_push_2.raise_()
        self.stackedWidget.addWidget(self.append_page)
        self.choice_change_page = QtWidgets.QWidget()
        self.choice_change_page.setObjectName("choice_change_page")
        self.back_icon_3 = QtWidgets.QLabel(self.choice_change_page)
        self.back_icon_3.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_icon_3.setMinimumSize(QtCore.QSize(31, 31))
        self.back_icon_3.setMaximumSize(QtCore.QSize(31, 31))
        self.back_icon_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_icon_3.setPixmap(QtGui.QPixmap("../icons/back_push.png"))
        self.back_icon_3.setScaledContents(True)
        self.back_icon_3.setObjectName("back_icon_3")
        self.back_push_3 = QtWidgets.QPushButton(self.choice_change_page)
        self.back_push_3.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_push_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_push_3.setObjectName("back_push_3")
        self.choice_type = QtWidgets.QComboBox(self.choice_change_page)
        self.choice_type.setGeometry(QtCore.QRect(140, 120, 211, 31))
        self.choice_type.setObjectName("choice_type")
        self.choice_type.addItem("")
        self.choice_type.addItem("")
        self.choice_type.addItem("")
        self.choice_type.addItem("")
        self.further_push = QtWidgets.QPushButton(self.choice_change_page)
        self.further_push.setGeometry(QtCore.QRect(220, 220, 31, 31))
        self.further_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.further_push.setObjectName("further_push")
        self.further_icon = QtWidgets.QLabel(self.choice_change_page)
        self.further_icon.setGeometry(QtCore.QRect(220, 220, 31, 31))
        self.further_icon.setPixmap(QtGui.QPixmap("../icons/further_push.png"))
        self.further_icon.setScaledContents(True)
        self.further_icon.setObjectName("further_icon")
        self.further_icon.raise_()
        self.back_icon_3.raise_()
        self.back_push_3.raise_()
        self.choice_type.raise_()
        self.further_push.raise_()
        self.stackedWidget.addWidget(self.choice_change_page)
        self.change_page = QtWidgets.QWidget()
        self.change_page.setObjectName("change_page")
        self.back_push_4 = QtWidgets.QPushButton(self.change_page)
        self.back_push_4.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_push_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_push_4.setObjectName("back_push_4")
        self.back_icon_4 = QtWidgets.QLabel(self.change_page)
        self.back_icon_4.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.back_icon_4.setMinimumSize(QtCore.QSize(31, 31))
        self.back_icon_4.setMaximumSize(QtCore.QSize(31, 31))
        self.back_icon_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.back_icon_4.setPixmap(QtGui.QPixmap("../icons/back_push.png"))
        self.back_icon_4.setScaledContents(True)
        self.back_icon_4.setObjectName("back_icon_4")
        self.update = QtWidgets.QFrame(self.change_page)
        self.update.setGeometry(QtCore.QRect(10, 140, 481, 51))
        self.update.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.update.setFrameShadow(QtWidgets.QFrame.Raised)
        self.update.setObjectName("update")
        self.update_text = QtWidgets.QLabel(self.update)
        self.update_text.setGeometry(QtCore.QRect(0, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.update_text.setFont(font)
        self.update_text.setObjectName("update_text")
        self.update_name = QtWidgets.QLineEdit(self.update)
        self.update_name.setGeometry(QtCore.QRect(160, 0, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.update_name.setFont(font)
        self.update_name.setObjectName("update_name")
        self.update_push = QtWidgets.QPushButton(self.change_page)
        self.update_push.setGeometry(QtCore.QRect(230, 260, 31, 31))
        self.update_push.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.update_push.setObjectName("update_push")
        self.update_icon = QtWidgets.QLabel(self.change_page)
        self.update_icon.setGeometry(QtCore.QRect(230, 260, 31, 31))
        self.update_icon.setPixmap(QtGui.QPixmap("../icons/update_push.png"))
        self.update_icon.setScaledContents(True)
        self.update_icon.setObjectName("update_icon")
        self.back_icon_4.raise_()
        self.update_icon.raise_()
        self.back_push_4.raise_()
        self.update.raise_()
        self.update_push.raise_()
        self.stackedWidget.addWidget(self.change_page)
        self.delete_page = QtWidgets.QWidget()
        self.delete_page.setObjectName("delete_page")
        self.choice_delete = QtWidgets.QComboBox(self.delete_page)
        self.choice_delete.setGeometry(QtCore.QRect(120, 120, 221, 31))
        self.choice_delete.setObjectName("choice_delete")
        self.choice_delete.addItem("")
        self.delete_push_2 = QtWidgets.QPushButton(self.delete_page)
        self.delete_push_2.setGeometry(QtCore.QRect(220, 180, 31, 31))
        self.delete_push_2.setMinimumSize(QtCore.QSize(31, 31))
        self.delete_push_2.setMaximumSize(QtCore.QSize(31, 31))
        self.delete_push_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_push_2.setObjectName("delete_push_2")
        self.delete_icon_2 = QtWidgets.QLabel(self.delete_page)
        self.delete_icon_2.setGeometry(QtCore.QRect(220, 180, 31, 31))
        self.delete_icon_2.setMinimumSize(QtCore.QSize(31, 31))
        self.delete_icon_2.setMaximumSize(QtCore.QSize(31, 31))
        self.delete_icon_2.setPixmap(QtGui.QPixmap("../icons/delete_push_2.png"))
        self.delete_icon_2.setScaledContents(True)
        self.delete_icon_2.setObjectName("delete_icon_2")
        self.delete_icon_2.raise_()
        self.choice_delete.raise_()
        self.delete_push_2.raise_()
        self.stackedWidget.addWidget(self.delete_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_tittle.setText(_translate("MainWindow", "Выбор:"))
        self.choice_combo.setItemText(0, _translate("MainWindow", "Сайты"))
        self.user_text.setText(_translate("MainWindow", "User Name:"))
        self.user_name.setText(_translate("MainWindow", "denis170.170@yandex.ru"))
        self.viewing_title.setText(_translate("MainWindow", "nike.com"))
        self.password_text.setText(_translate("MainWindow", "Password:"))
        self.password_name.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tBGFSYGB2@JNhbvgvg@</p></body></html>"))
        self.add_user_text.setText(_translate("MainWindow", "LOGIN:"))
        self.add_password_text.setText(_translate("MainWindow", "PASSWORD:"))
        self.add_url_text.setText(_translate("MainWindow", "URL:"))
        self.add_push_2.setShortcut(_translate("MainWindow", "Return"))
        self.choice_type.setItemText(0, _translate("MainWindow", "Выберите изменяемый тип"))
        self.choice_type.setItemText(1, _translate("MainWindow", "URL - Ссылку на сайт"))
        self.choice_type.setItemText(2, _translate("MainWindow", "LOGIN - Логин"))
        self.choice_type.setItemText(3, _translate("MainWindow", "PASSWORD - Пароль"))
        self.update_text.setText(_translate("MainWindow", "URL:"))
        self.choice_delete.setItemText(0, _translate("MainWindow", "Выберите сайт"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
