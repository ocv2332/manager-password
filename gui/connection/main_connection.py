from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from database import models
from gui.windows import main_window

from secrets import token_urlsafe


class MainWindow(QtWidgets.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, database, config):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.database = database
        self.config = config

        self.view_icon.setPixmap(QtGui.QPixmap(f"gui/icons/view_push.png"))

        self.refresh_icon.setPixmap(QtGui.QPixmap(f"gui/icons/refresh_push.png"))

        self.add_icon.setPixmap(QtGui.QPixmap(f"gui/icons/add_push.png"))
        self.add_icon_2.setPixmap(QtGui.QPixmap(f"gui/icons/add_push_2.png"))
        self.generation_icon.setPixmap(QtGui.QPixmap(f"gui/icons/generation_push.png"))

        self.change_icon.setPixmap(QtGui.QPixmap(f"gui/icons/change_push.png"))
        self.further_icon.setPixmap(QtGui.QPixmap(f"gui/icons/further_push.png"))
        self.update_icon.setPixmap(QtGui.QPixmap(f"gui/icons/update_push.png"))

        self.delete_icon.setPixmap(QtGui.QPixmap(f"gui/icons/delete_push.png"))
        self.delete_icon_2.setPixmap(QtGui.QPixmap(f"gui/icons/delete_push_2.png"))

        self.back_icon.setPixmap(QtGui.QPixmap(f"gui/icons/back_push.png"))
        self.back_icon_2.setPixmap(QtGui.QPixmap(f"gui/icons/back_push.png"))
        self.back_icon_3.setPixmap(QtGui.QPixmap(f"gui/icons/back_push.png"))
        self.back_icon_4.setPixmap(QtGui.QPixmap(f"gui/icons/back_push.png"))

        self.back_push.clicked.connect(self.to_back_page)
        self.back_push_2.clicked.connect(self.to_back_page)
        self.back_push_3.clicked.connect(self.to_back_page)
        self.back_push_4.clicked.connect(self.to_back_page)

        self.view_push.clicked.connect(self.show_view_page)

        self.refresh_push.clicked.connect(self.refresh_choice)

        self.generation_push.clicked.connect(self.generation_password)

        self.add_push.clicked.connect(self.show_add_page)
        self.add_push_2.clicked.connect(self.add_elements)

        self.change_push.clicked.connect(self.show_choice_page)
        self.further_push.clicked.connect(self.show_update_page)
        self.update_push.clicked.connect(self.update_element)

        self.delete_push.clicked.connect(self.show_delete_page)
        self.delete_push_2.clicked.connect(self.delete_element)

        self.choice_combo.addItems(self.database.select_query(select(models.Password.url), 1))

    def refresh_choice(self):
        self.choice_combo.clear()
        return self.choice_combo.addItems(['Сайты'] + self.database.select_query(select(models.Password.url), 1))

    def to_back_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def generation_password(self):
        return self.add_password_name.setText(token_urlsafe(21))

    def show_view_page(self):
        self.viewing_title.clear()
        self.user_name.clear()
        self.password_name.clear()

        self.viewing_title.setText(self.choice_combo.currentText())

        self.user_name.setText(self.database.select_query(select(models.Password.login
                                                                 ).where(
            models.Password.url == self.choice_combo.currentText()), 2))

        self.password_name.setText(self.database.select_query(select(models.Password.password
                                                                     ).where(
            models.Password.url == self.choice_combo.currentText()), 2))

        self.stackedWidget.setCurrentIndex(1)

    def show_add_page(self):
        self.add_url_name.clear()
        self.add_user_name.clear()
        self.add_password_name.clear()

        self.stackedWidget.setCurrentIndex(2)

    def add_elements(self):
        try:
            add_id = self.database.get_last_index(models.Password.id)
            url = self.add_url_name.text()
            user = self.add_user_name.text()
            password = self.add_password_name.text()

            self.database.insert_query(models.Password, add_id, url, user, password)
            self.stackedWidget.setCurrentIndex(0)
        except TypeError:
            QMessageBox.warning(self, "ОШИБКА", "Заполните все поля!")

    def show_choice_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def show_update_page(self):
        if self.choice_type.currentText() == "URL - Ссылку на сайт":
            self.update_text.clear()
            self.update_name.clear()

            self.update_text.setText("URL: ")
            self.update_name.setText(self.database.select_query(select(models.Password.url
                                                                       ).where(
                models.Password.url == self.choice_combo.currentText()), 2))

            self.stackedWidget.setCurrentIndex(4)
        elif self.choice_type.currentText() == "LOGIN - Логин":
            self.update_text.clear()
            self.update_name.clear()

            self.update_text.setText("LOGIN: ")
            self.update_name.setText(self.database.select_query(select(models.Password.login
                                                                       ).where(
                models.Password.url == self.choice_combo.currentText()), 2))

            self.stackedWidget.setCurrentIndex(4)
        elif self.choice_type.currentText() == "PASSWORD - Пароль":
            self.update_text.clear()
            self.update_name.clear()

            self.update_text.setText("PASSWORD: ")
            self.update_name.setText(self.database.select_query(select(models.Password.password
                                                                       ).where(
                models.Password.url == self.choice_combo.currentText()), 2))

            self.stackedWidget.setCurrentIndex(4)

    def update_element(self):
        if self.choice_type.currentText() == "URL - Ссылку на сайт":
            url_change = self.database.select_query(select(models.Password.url
                                                           ).where(
                models.Password.url == self.choice_combo.currentText()), 2)
            url = self.update_name.text()

            with Session(self.database.engine) as session:
                session.query(models.Password).filter(models.Password.url == url_change).update(
                    {models.Password.url: url})
                session.commit()

            self.to_back_page()
        elif self.choice_type.currentText() == "LOGIN - Логин":
            login_change = self.database.select_query(select(models.Password.login
                                                             ).where(
                models.Password.url == self.choice_combo.currentText()), 2)
            login = self.update_name.text()

            with Session(self.database.engine) as session:
                session.query(models.Password).filter(models.Password.login == login_change).update(
                    {models.Password.login: login})
                session.commit()

            self.to_back_page()
        elif self.choice_type.currentText() == "PASSWORD - Пароль":
            password_change = self.database.select_query(select(models.Password.password
                                                                ).where(
                models.Password.url == self.choice_combo.currentText()), 2)
            password = self.update_name.text()

            with Session(self.database.engine) as session:
                session.query(models.Password).filter(models.Password.password == password_change).update(
                    {models.Password.password: password})
                session.commit()
            self.to_back_page()

    def show_delete_page(self):
        self.choice_delete.clear()
        self.choice_delete.addItems(["Выберите сайт"] + self.database.select_query(select(models.Password.url), 1))

        self.stackedWidget.setCurrentIndex(5)

    def delete_element(self):
        url_input_delete = self.choice_delete.currentText()

        self.database.engine_connect(delete(models.Password).where(models.Password.url == url_input_delete))

        self.to_back_page()
