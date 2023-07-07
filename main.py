
import patology as patologys
import test as tests
import resource_clinic_rc

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from patology import UiPatology
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql


class UiMainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1200, 700)
        mainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        mainWindow.setMaximumSize(QtCore.QSize(1200, 700))
        mainWindow.setSizeIncrement(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        font.setUnderline(False)
        mainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblproject = QtWidgets.QLabel(self.centralwidget)
        self.lblproject.setGeometry(QtCore.QRect(450, 10, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setUnderline(False)
        self.lblproject.setFont(font)
        self.lblproject.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblproject.setAlignment(QtCore.Qt.AlignCenter)
        self.lblproject.setObjectName("lblproject")
        self.lblcompany = QtWidgets.QLabel(self.centralwidget)
        self.lblcompany.setGeometry(QtCore.QRect(10, 650, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(7)
        font.setUnderline(False)
        self.lblcompany.setFont(font)
        self.lblcompany.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblcompany.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblcompany.setObjectName("lblcompany")
        self.lbllogo = QtWidgets.QLabel(self.centralwidget)
        self.lbllogo.setGeometry(QtCore.QRect(20, 590, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setUnderline(False)
        self.lbllogo.setFont(font)
        self.lbllogo.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbllogo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbllogo.setObjectName("lbllogo")
        self.lblpatient = QtWidgets.QLabel(self.centralwidget)
        self.lblpatient.setGeometry(QtCore.QRect(1050, 60, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblpatient.setFont(font)
        self.lblpatient.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblpatient.setObjectName("lblpatient")
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
        self.lblfirstname = QtWidgets.QLabel(self.centralwidget)
        self.lblfirstname.setGeometry(QtCore.QRect(915, 100, 23, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblfirstname.setFont(font)
        self.lblfirstname.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblfirstname.setObjectName("lblfirstname")
        self.lbllastname = QtWidgets.QLabel(self.centralwidget)
        self.lbllastname.setGeometry(QtCore.QRect(668, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbllastname.setFont(font)
        self.lbllastname.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lbllastname.setObjectName("lbllastname")
        self.lblpersonnelId = QtWidgets.QLabel(self.centralwidget)
        self.lblpersonnelId.setGeometry(QtCore.QRect(408, 100, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblpersonnelId.setFont(font)
        self.lblpersonnelId.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblpersonnelId.setObjectName("lblpersonnelId")
        self.lblnationalId = QtWidgets.QLabel(self.centralwidget)
        self.lblnationalId.setGeometry(QtCore.QRect(181, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblnationalId.setFont(font)
        self.lblnationalId.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblnationalId.setObjectName("lblnationalId")
        self.lblrank = QtWidgets.QLabel(self.centralwidget)
        self.lblrank.setGeometry(QtCore.QRect(1123, 100, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblrank.setFont(font)
        self.lblrank.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblrank.setObjectName("lblrank")
        self.lineEditfirstname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditfirstname.setGeometry(QtCore.QRect(782, 98, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEditfirstname.setFont(font)
        self.lineEditfirstname.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditfirstname.setObjectName("lineEditfirstname")
        self.lineEditlastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditlastname.setGeometry(QtCore.QRect(523, 98, 151, 24))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEditlastname.setFont(font)
        self.lineEditlastname.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditlastname.setObjectName("lineEditlastname")
        self.lineEditpersonnelId = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditpersonnelId.setGeometry(QtCore.QRect(275, 98, 131, 24))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEditpersonnelId.setFont(font)
        self.lineEditpersonnelId.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditpersonnelId.setObjectName("lineEditpersonnelId")
        self.lineEditnationalId = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditnationalId.setGeometry(QtCore.QRect(40, 98, 141, 24))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEditnationalId.setFont(font)
        self.lineEditnationalId.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditnationalId.setObjectName("lineEditnationalId")
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
        self.pushButtonsubmit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonsubmit.setGeometry(QtCore.QRect(40, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButtonsubmit.setFont(font)
        self.pushButtonsubmit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButtonsubmit.setObjectName("pushButtonsubmit")
        self.pushButtonedit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonedit.setGeometry(QtCore.QRect(150, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButtonedit.setFont(font)
        self.pushButtonedit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButtonedit.setObjectName("pushButtonedit")
        self.pushButtondelete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtondelete.setGeometry(QtCore.QRect(260, 140, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButtondelete.setFont(font)
        self.pushButtondelete.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButtondelete.setObjectName("pushButtondelete")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(250, 210, 775, 415))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.tableView.setFont(font)
        self.tableView.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setObjectName("tableView")
        self.pushButtonsearch = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonsearch.setGeometry(QtCore.QRect(50, 460, 171, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButtonsearch.setFont(font)
        self.pushButtonsearch.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButtonsearch.setObjectName("pushButtonsearch")
        self.lineEditsearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditsearch.setGeometry(QtCore.QRect(50, 430, 171, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.lineEditsearch.setFont(font)
        self.lineEditsearch.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditsearch.setObjectName("lineEditsearch")
        self.pushButtonlab = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonlab.setGeometry(QtCore.QRect(50, 490, 171, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButtonlab.setFont(font)
        self.pushButtonlab.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButtonlab.setObjectName("pushButtonlab")
        self.comboBoxrank = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxrank.setGeometry(QtCore.QRect(962, 98, 161, 24))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setUnderline(False)
        self.comboBoxrank.setFont(font)
        self.comboBoxrank.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.comboBoxrank.setObjectName("comboBoxrank")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.setFixedSize()
        

        db = QtSql.QSqlDatabase.addDatabase("QODBC")
        db.setDatabaseName("DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-J8BACV4;DATABASE=clinic;UID=sa;PWD=62399")

        if db.open():
            print("Connected to databse")

            model = QtSql.QSqlTableModel()
            model.setTable("Patients")
            model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
            model.select()
            model.setHeaderData(0, QtCore.Qt.Horizontal, "شماره پرونده")
            model.setHeaderData(1, QtCore.Qt.Horizontal, "درجه/رتبه")
            model.setHeaderData(2, QtCore.Qt.Horizontal, "نام")
            model.setHeaderData(3, QtCore.Qt.Horizontal, "نام خانوادگی")
            model.setHeaderData(4, QtCore.Qt.Horizontal, "شماره پرسنلی")
            model.setHeaderData(5, QtCore.Qt.Horizontal, "کد ملی")
            
            self.tableView.setModel(model)

            self.pushButtonsubmit.clicked.connect(self.addDataToDatabase)
            self.pushButtondelete.clicked.connect(self.deleteDataFromDatabase)
            self.pushButtonsubmit.clicked.connect(self.saveComboBoxDataToDatabase)
            self.pushButtonedit.clicked.connect(self.updateDataInDatabase)
            self.pushButtonsearch.clicked.connect(self.searchInDatabase)
            self.tableView.clicked.connect(self.showSelectedRowData)

        else:
            print("Failed to connect to database")
        
        query = QtSql.QSqlQuery()
        query.exec_("SELECT Rank FROM Ranks")

        while query.next():
            value = query.value(0)
            self.comboBoxrank.addItem(value)
            
    def addDataToDatabase(self):
        model = self.tableView.model()

        # Get the values from the QLineEdit fields
        value1 = self.comboBoxrank.currentText()
        value2 = self.lineEditfirstname.text()
        value3 = self.lineEditlastname.text()
        value4 = self.lineEditpersonnelId.text()
        value5 = self.lineEditnationalId.text()

        # Check if the fields are empty
        if value2.strip() == "" or value3.strip() == "" or value4.strip() == "" or value5.strip() == "":
            QMessageBox.warning(self, "Warning", "Please fill all the fields.")

        # Insert a new empty record
        if not model.insertRow(0):
            print("Failed to insert record.")
            model.database().rollback()
            return
        
        if value1:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO Patients (Rankp) VALUES (?)")
            query.addBindValue(value1)
            if query.exec_():
                print("Data inserted successfully.")
            else:
                print("Failed to insert data:", query.lastError().text())
        else:
            print("No value selected.")
        # Get the index of the new row
        index = model.index(0, 0)

        # Set the values in the record
        model.setData(index.siblingAtColumn(1), value1, QtCore.Qt.EditRole)
        model.setData(index.siblingAtColumn(2), value2, QtCore.Qt.EditRole)
        model.setData(index.siblingAtColumn(3), value3, QtCore.Qt.EditRole)
        model.setData(index.siblingAtColumn(4), value4, QtCore.Qt.EditRole)
        model.setData(index.siblingAtColumn(5), value5, QtCore.Qt.EditRole)

        # Submit the changes to the model
        if model.submitAll():
            model.database().commit()
            print("Record inserted successfully.")
        else:
            print("Failed to submit changes.")
            model.database().rollback()
        
        self.comboBoxrank.setCurrentIndex(0)
        self.lineEditfirstname.clear()
        self.lineEditlastname.clear()
        self.lineEditpersonnelId.clear()
        self.lineEditnationalId.clear()
    
    def saveComboBoxDataToDatabase(self):
        selectedValue = self.comboBoxrank.currentText()
        if selectedValue:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO Patients (Rankp) VALUES (?)")
            query.addBindValue(selectedValue)
            if query.exec_():
                print("Data inserted successfully.")
            else:
                print("Failed to insert data:", query.lastError().text())
        else:
            print("No value selected.")

    def deleteDataFromDatabase(self):
        model = self.tableView.model()
        selectionModel = self.tableView.selectionModel()

        # Check if any row is selected
        if not selectionModel.hasSelection():
            print("No row selected.")
            return

        # Get the selected row(s) index
        indexes = selectionModel.selectedRows()

        # Delete the selected row(s)
        for index in indexes:
            model.removeRow(index.row())

        # Submit the changes to the model
        if model.submitAll():
            model.database().commit()
            print("Record(s) deleted successfully.")
        else:
            print("Failed to submit changes.")
            model.database().rollback()
        self.comboBoxrank.setCurrentIndex(0)

    def updateDataInDatabase(self):
        selectedRow = self.tableView.currentIndex().row()
        if selectedRow >= 0:
            model = self.tableView.model()

            value1 = self.comboBoxrank.currentText()
            value2 = self.lineEditfirstname.text()
            value3 = self.lineEditlastname.text()
            value4 = self.lineEditpersonnelId.text()
            value5 = self.lineEditnationalId.text()
            
            model.setData(model.index(selectedRow, 1), value1, QtCore.Qt.EditRole)
            model.setData(model.index(selectedRow, 2), value2, QtCore.Qt.EditRole)
            model.setData(model.index(selectedRow, 3), value3, QtCore.Qt.EditRole)
            model.setData(model.index(selectedRow, 4), value4, QtCore.Qt.EditRole)
            model.setData(model.index(selectedRow, 5), value5, QtCore.Qt.EditRole)
            
            if model.submitAll():
                print("Data updated successfully.")
            else:
                print("Failed to update data:", model.lastError().text())
        else:
            print("No row selected.")
        
        self.comboBoxrank.setCurrentIndex(0)
        self.lineEditfirstname.clear()
        self.lineEditlastname.clear()
        self.lineEditpersonnelId.clear()
        self.lineEditnationalId.clear()

    def searchInDatabase(self):
        model = self.tableView.model()

        # خواندن مقدار ورودی از QLineEdit
        search_value = self.lineEditsearch.text()

        # اجرای کوئری جستجو با استفاده از عبارت WHERE
        model.setFilter("NationalId LIKE '%{}%'".format(search_value))

        # بازیابی نتایج جستجو
        model.select()
        
        self.lineEditsearch.clear()

    def showSelectedRowData(self):
        model = self.tableView.model()

            # دریافت ردیف‌های انتخاب شده
        selected_indexes = self.tableView.selectedIndexes()
        # index = self.comboBoxrank.currentIndex()
        # value1 = model.index(selected_row, 1).data

            # بررسی آیا ردیفی انتخاب شده است
        if selected_indexes:
                # دریافت شماره ردیف انتخاب شده
            selected_row = selected_indexes[0].row()

                # دریافت مقادیر سلول‌های ردیف انتخاب شده
            value2 = model.index(selected_row, 2).data()
            value3 = model.index(selected_row, 3).data()
            value4 = model.index(selected_row, 4).data()
            value5 = model.index(selected_row, 5).data()

            # self.comboBoxrank.setCurrentIndex(index)
            self.lineEditfirstname.setText(value2)
            self.lineEditlastname.setText(value3)
            self.lineEditpersonnelId.setText(str(value4))
            self.lineEditnationalId.setText(str(value5))
    
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "نرم افزار درمانگاهی"))
        self.lblproject.setText(_translate("mainWindow", "درمانگاه دانشگاه پدافندهوایی خاتم الانبیاء(ص)"))
        self.lblcompany.setText(_translate("mainWindow", "سازنده اثر: شرکت نرم افزاری XERXESS"))
        self.lbllogo.setText(_translate("mainWindow", "<html><head/><body><p><img src=\":/newPrefix/image/xerxes.png\"/></p></body></html>"))
        self.lblpatient.setText(_translate("mainWindow", "ورود اطلاعات بیماران:"))
        self.lblfirstname.setText(_translate("mainWindow", "نام:"))
        self.lbllastname.setText(_translate("mainWindow", "نام خانوادگی:"))
        self.lblpersonnelId.setText(_translate("mainWindow", "شماره پرسنلی:"))
        self.lblnationalId.setText(_translate("mainWindow", "شماره ملی:"))
        self.lblrank.setText(_translate("mainWindow", "درجه:"))
        self.pushButtonsubmit.setText(_translate("mainWindow", "ثبت"))
        self.pushButtonedit.setText(_translate("mainWindow", "ویرایش"))
        self.pushButtondelete.setText(_translate("mainWindow", "حذف"))
        self.tableView.setSortingEnabled(False)
        self.pushButtonsearch.setText(_translate("mainWindow", "جستجو بر اساس شماره ملی"))
        self.pushButtonlab.setText(_translate("mainWindow", "آزمایش"))

    def setFixedSize(self):
        self.centralwidget.setFixedSize(1200, 700)

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
    ui.pushButtonlab.clicked.connect(lambda : patology.exec_())
    ui1 = UiPatology()
    ui1.setupUi(patology)
    test_window = tests.UiTest()
    test = QtWidgets.QDialog()
    test_window.setupUi(test)
    # ui1.pushButtonnewlab.clicked.connect(lambda : test.exec_())

    sys.exit(app.exec_())
