import sys

from PyQt5 import QtWidgets

from config.config import Config
from database.database import DataBase
from gui.connection.main_connection import MainWindow


def main():
    config = Config()
    database = DataBase("manager")
    database.create_all_tables()

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(database, config)
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
