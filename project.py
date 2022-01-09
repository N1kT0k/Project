import sqlite3
import sys

from PyQt5 import QtCore, QtWidgets, uic
from random import choices
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QDialog, QWidget


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1092, 623)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(330, 40, 751, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchLine = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.searchLine.setObjectName("searchLine")
        self.horizontalLayout.addWidget(self.searchLine)
        self.searchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.Filter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Filter.setObjectName("Filter")
        self.horizontalLayout.addWidget(self.Filter)
        self.Films_of_day = QtWidgets.QTableWidget(self.centralwidget)
        self.Films_of_day.setGeometry(QtCore.QRect(20, 460, 911, 111))
        self.Films_of_day.setObjectName("Films_of_day")
        self.Films_of_day.setColumnCount(0)
        self.Films_of_day.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 410, 161, 31))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 276, 82))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.resultade = QtWidgets.QTableWidget(self.centralwidget)
        self.resultade.setGeometry(QtCore.QRect(20, 180, 911, 192))
        self.resultade.setObjectName("resultade")
        self.resultade.setColumnCount(0)
        self.resultade.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 91, 21))
        self.label_4.setObjectName("label_4")
        self.plus = QtWidgets.QPushButton(self.centralwidget)
        self.plus.setGeometry(QtCore.QRect(890, 370, 41, 41))
        self.plus.setObjectName("plus")
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(850, 370, 41, 41))
        self.minus.setObjectName("minus")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(940, 160, 151, 414))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_2.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_2.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_2.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_2.addWidget(self.label_26)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchButton.setText(_translate("MainWindow", "🔍"))
        self.Filter.setText(_translate("MainWindow", "Параметры поиска"))
        self.label_3.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:16pt; "
                                        "font-weight:600;\">Подборка дня:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p><span style=\" font-size:36pt;\">Кино</span><span "
                                      "style=\" font-size:36pt; font-weight:600;\">Search</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:10pt;\">Лучший поисковый "
                                        "сервис фильмов в России</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow",
                                        "<html><head/><body><p><span style=\" font-size:14pt; "
                                        "font-weight:600;\">Найдено:</span></p></body></html>"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.label_5.setText(_translate("MainWindow", "1 - комедия"))
        self.label_6.setText(_translate("MainWindow", "2 - драма"))
        self.label_7.setText(_translate("MainWindow", "3 - мелодрама"))
        self.label_8.setText(_translate("MainWindow", "4 - детектив"))
        self.label_9.setText(_translate("MainWindow", "5 - документальный"))
        self.label_10.setText(_translate("MainWindow", "6 - ужасы"))
        self.label_11.setText(_translate("MainWindow", "7 - музыка"))
        self.label_12.setText(_translate("MainWindow", "8 - фантастика"))
        self.label_13.setText(_translate("MainWindow", "9 - анимация"))
        self.label_14.setText(_translate("MainWindow", "10 - биография"))
        self.label_15.setText(_translate("MainWindow", "11 - боевик"))
        self.label_16.setText(_translate("MainWindow", "12 - приключения"))
        self.label_17.setText(_translate("MainWindow", "13 - война"))
        self.label_18.setText(_translate("MainWindow", "14 семейный"))
        self.label_19.setText(_translate("MainWindow", "15 - триллер"))
        self.label_20.setText(_translate("MainWindow", "16 - фэнтези"))
        self.label_21.setText(_translate("MainWindow", "17 - вестерн"))
        self.label_22.setText(_translate("MainWindow", "18 - мистика"))
        self.label_23.setText(_translate("MainWindow", "19 - короткометражный"))
        self.label_24.setText(_translate("MainWindow", "20 - мюзикл"))
        self.label_25.setText(_translate("MainWindow", "21 - исторический"))
        self.label_26.setText(_translate("MainWindow", "22 - нуар"))


class Ui_DialogFilter(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 207)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 60, 381, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.time1 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.time1.setObjectName("time1")
        self.horizontalLayout.addWidget(self.time1)
        self.time2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.time2.setObjectName("time2")
        self.horizontalLayout.addWidget(self.time2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 201, 16))
        self.label.setObjectName("label")
        self.Genre = QtWidgets.QLineEdit(Dialog)
        self.Genre.setGeometry(QtCore.QRect(10, 130, 301, 20))
        self.Genre.setObjectName("Genre")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 91, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Продолжительность фильма(от, до)"))
        self.label_2.setText(_translate("Dialog", "Название жанра:"))


class Ui_DialogAddFilm(QWidget):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 449)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(90, 240, 221, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 101, 21))
        self.label.setObjectName("label")
        self.film = QtWidgets.QLineEdit(Dialog)
        self.film.setGeometry(QtCore.QRect(30, 60, 281, 20))
        self.film.setObjectName("film")
        self.genree = QtWidgets.QSpinBox(Dialog)
        self.genree.setGeometry(QtCore.QRect(30, 120, 111, 20))
        self.genree.setObjectName("genree")
        self.duration = QtWidgets.QSpinBox(Dialog)
        self.duration.setGeometry(QtCore.QRect(30, 180, 251, 20))
        self.duration.setObjectName("duration")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 121, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 101, 16))
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 20, 160, 414))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.verticalLayout.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.verticalLayout.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.verticalLayout.addWidget(self.label_18)
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.verticalLayout.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.verticalLayout.addWidget(self.label_21)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.verticalLayout.addWidget(self.label_22)
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.verticalLayout.addWidget(self.label_23)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.verticalLayout.addWidget(self.label_25)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Название фильма"))
        self.label_2.setText(_translate("Dialog", "Жанр"))
        self.label_3.setText(_translate("Dialog", "Длительность"))
        self.label_4.setText(_translate("Dialog", "1 - комедия"))
        self.label_6.setText(_translate("Dialog", "2 - драма"))
        self.label_5.setText(_translate("Dialog", "3 - мелодрама"))
        self.label_7.setText(_translate("Dialog", "4 - детектив"))
        self.label_8.setText(_translate("Dialog", "5 - документальный"))
        self.label_9.setText(_translate("Dialog", "6 - ужасы"))
        self.label_10.setText(_translate("Dialog", "7 - музыка"))
        self.label_11.setText(_translate("Dialog", "8 - фантастика"))
        self.label_12.setText(_translate("Dialog", "9 - анимация"))
        self.label_13.setText(_translate("Dialog", "10 - биография"))
        self.label_14.setText(_translate("Dialog", "11 - боевик"))
        self.label_15.setText(_translate("Dialog", "12 - приключения"))
        self.label_16.setText(_translate("Dialog", "13 - война"))
        self.label_17.setText(_translate("Dialog", "14 семейный"))
        self.label_18.setText(_translate("Dialog", "15 - триллер"))
        self.label_19.setText(_translate("Dialog", "16 - фэнтези"))
        self.label_20.setText(_translate("Dialog", "17 - вестерн"))
        self.label_21.setText(_translate("Dialog", "18 - мистика"))
        self.label_22.setText(_translate("Dialog", "19 - короткометражный"))
        self.label_23.setText(_translate("Dialog", "20 - мюзикл"))
        self.label_24.setText(_translate("Dialog", "21 - исторический"))
        self.label_25.setText(_translate("Dialog", "22 - нуар"))


class DialogAddFilm(QDialog, Ui_DialogAddFilm):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.film.textChanged[str].connect(self.onChanged)
        self.genree.setMaximum(22)
        self.duration.setMaximum(999)
        self.genree.valueChanged.connect(self.get_value)
        self.duration.valueChanged.connect(self.get_value)
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)

    def onChanged(self, text):
        self.text = text

    def get_value(self):
        self.genree1 = self.genree.value()
        self.duration1 = self.duration.value()

    def acept_data(self):
        self.con = sqlite3.connect("films_db.sqlite")
        cur = self.con.cursor()
        add = cur.execute(f"""INSERT INTO films(title, genre, duration) 
                VALUES("{self.text}", {self.genree1}, {self.duration1})""")
        self.con.commit()
        self.con.close()

    def reject_data(self):
        self.close()


class DialogFilter(QDialog, Ui_DialogFilter):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.time1.setMaximum(999)
        self.time2.setMaximum(999)
        self.time1.valueChanged.connect(self.get_value)
        self.time2.valueChanged.connect(self.get_value)
        self.genre = self.Genre.text().lower()
        self.buttonBox.accepted.connect(self.acept_data)
        self.buttonBox.rejected.connect(self.reject_data)

    def get_value(self):
        self.value1 = self.time1.value()
        self.value2 = self.time2.value()

    def acept_data(self):
        self.close()

    def reject_data(self):
        self.value1 = 0
        self.value2 = 0
        self.genre = ""
        self.close()


class MovieSearch(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.value1 = 0
        self.value2 = 0
        self.genre = ""
        self.con = sqlite3.connect("films_db.sqlite")
        self.searchButton.clicked.connect(self.search)
        self.Filter.clicked.connect(self.filter)
        self.plus.clicked.connect(self.add_film)
        cur = self.con.cursor()
        result = cur.execute("""SELECT title, genre, duration FROM films 
        WHERE title like '%'""").fetchall()
        films = choices(result, k=3)
        self.Films_of_day.setRowCount(len(films))
        self.Films_of_day.setColumnCount(len(films[0]))
        self.Films_of_day.setHorizontalHeaderLabels(["Название", "Жанр", "Продолжительность в минутах"])
        self.titles = [description[1] for description in cur.description]
        for i, elem in enumerate(films):
            for j, val in enumerate(elem):
                self.Films_of_day.setItem(i, j, QTableWidgetItem(str(val)))

    def filter(self):
        self.DialogWindow = DialogFilter()
        self.DialogWindow.show()
        self.DialogWindow.exec()
        self.value1 = self.DialogWindow.value1
        self.value2 = self.DialogWindow.value2
        self.genre = self.DialogWindow.Genre.text()

    def add_film(self):
        self.DialogAddFilm = DialogAddFilm()
        self.DialogAddFilm.show()
        self.DialogAddFilm.exec()

    def search(self):
        cur = self.con.cursor()
        if self.value1 != 0 and self.value2 != 0 and self.genre != "":
            print(1)
            result = cur.execute(f"""SELECT title, genre, duration FROM films 
                    WHERE title like '%{self.searchLine.text().lower()}%' AND
                        duration BETWEEN {self.value1} AND {self.value2} AND
                    genre=(SELECT id FROM genres 
                    WHERE title = '{self.genre}')""").fetchall()
        else:
            print(2)
            result = cur.execute(f"""SELECT title, genre, duration FROM films 
                    WHERE lower(title) like '%{self.searchLine.text().lower()}%'""").fetchall()
        for i in result:
            word = i[0]
            if word[:len(self.searchLine.text().lower())].lower() != self.searchLine.text().lower():
                result.remove(i)
        if result:
            self.resultade.setRowCount(len(result))
            self.resultade.setColumnCount(len(result[0]))
            self.resultade.setHorizontalHeaderLabels(["Название", "Жанр", "Продолжительность в минутах"])
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.resultade.setItem(i, j, QTableWidgetItem(str(val)))
            self.statusBar().showMessage(f'По вашему запросу найдено: {len(result)} результатов')
        else:
            self.statusBar().showMessage('По вашему запросу ничего не нашлось')
            self.resultade.setRowCount(0)
            self.resultade.setColumnCount(0)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MovieSearch()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
