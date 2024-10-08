import sys
from PyQt5.QtWidgets import QApplication

from os import path
from models import PlayList, Albums
from classes import MainClass


def main() -> None:
    """Звпуск основного окна"""
    app = QApplication(sys.argv)
    main_window = MainClass()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    # Создание таблиц в БД
    if not path.exists('DB/playlist.db'):
        PlayList.create_table()
        Albums.create_table()
    main()
