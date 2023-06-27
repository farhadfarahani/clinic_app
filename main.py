import typing
import patology as patologys
import test as tests
import pyodbc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from patology import UiPatology
from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        mainWindow.setMaximumSize(QtCore.QSize(1200, 700))
        mainWindow.setSizeIncrement(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setUnderline(False)
        mainWindow.setFont(font)

        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                         'Server=DESKTOP-J8BACV4;'
                         'Database=clinic;'
                         'Trusted_Connection=yes;')
        cursor = connection.cursor()

        # اجرای کوئری SELECT برای دریافت داده‌ها
        cursor.execute('SELECT * FROM Patients')
        rows = cursor.fetchall()

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 10, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 650, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(7)
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 590, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1050, 60, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 1201, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.line.setFont(font)
        self.line.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(928, 100, 23, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(698, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(438, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(231, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1103, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_9.setFont(font)
        self.label_9.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(975, 100, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(813, 100, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(553, 100, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(325, 100, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 100, 131, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 170, 1201, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.line_2.setFont(font)
        self.line_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 210, 775, 415))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.tableWidget.setLineWidth(2)
        self.tableWidget.setMidLineWidth(1)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(len(rows[0]))
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 460, 171, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 430, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 490, 171, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_5.setObjectName("pushButton_5")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        for row_num, row_data in enumerate(rows):
            for col_num, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_num, col_num, item)

        # بستن اتصال و Cursor
        cursor.close()
        connection.close()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "نرم افزار درمانگاهی"))
        self.label_2.setText(_translate("mainWindow", "درمانگاه دانشگاه پدافندهوایی خاتم الانبیاء(ص)"))
        self.label_3.setText(_translate("mainWindow", "سازنده اثر: شرکت نرم افزاری XERXESS"))
        self.label_5.setText(_translate("mainWindow", "<html><head/><body><p><img src=\":/newPrefix/image/xerxes.png\"/></p></body></html>"))
        self.label.setText(_translate("mainWindow", "ورود اطلاعات بیماران:"))
        self.label_4.setText(_translate("mainWindow", "نام:"))
        self.label_6.setText(_translate("mainWindow", "نام خانوادگی:"))
        self.label_7.setText(_translate("mainWindow", "شماره پرسنلی:"))
        self.label_8.setText(_translate("mainWindow", "شماره ملی:"))
        self.label_9.setText(_translate("mainWindow", "درجه:"))
        self.pushButton.setText(_translate("mainWindow", "ثبت"))
        self.pushButton_2.setText(_translate("mainWindow", "ویرایش"))
        self.pushButton_3.setText(_translate("mainWindow", "حذف"))
        self.tableWidget.setSortingEnabled(False)
        self.pushButton_4.setText(_translate("mainWindow", "جستجو بر اساس شماره ملی"))
        self.pushButton_5.setText(_translate("mainWindow", "آزمایش"))
import resource_clinic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    patology_window = patologys.UiPatology()
    patology = QtWidgets.QDialog()
    patology_window.setupUi(patology)
    ui.pushButton_5.clicked.connect(lambda : patology.exec_())
    ui1 = UiPatology()
    ui1.setupUi(patology)
    test_window = tests.UiTest()
    test = QtWidgets.QDialog()
    test_window.setupUi(test)
    ui1.pushButtonnewlab.clicked.connect(lambda : test.exec_())

    sys.exit(app.exec_())
