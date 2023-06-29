from PyQt5 import QtCore, QtGui, QtWidgets


class UiPatology(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1200, 700)
        Form.setMinimumSize(QtCore.QSize(1200, 700))
        Form.setMaximumSize(QtCore.QSize(1200, 700))
        Form.setBaseSize(QtCore.QSize(0, 0))
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setAutoFillBackground(False)
        self.lblclinicname = QtWidgets.QLabel(Form)
        self.lblclinicname.setGeometry(QtCore.QRect(450, 10, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setUnderline(False)
        self.lblclinicname.setFont(font)
        self.lblclinicname.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lblclinicname.setAlignment(QtCore.Qt.AlignCenter)
        self.lblclinicname.setObjectName("lblclinicname")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 40, 1201, 21))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setLineWidth(3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.groupBoxpatology = QtWidgets.QGroupBox(Form)
        self.groupBoxpatology.setGeometry(QtCore.QRect(780, 70, 411, 91))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxpatology.setFont(font)
        self.groupBoxpatology.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.groupBoxpatology.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBoxpatology.setObjectName("groupBoxpatology")
        self.lblname = QtWidgets.QLabel(self.groupBoxpatology)
        self.lblname.setGeometry(QtCore.QRect(380, 50, 23, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblname.setFont(font)
        self.lblname.setObjectName("lblname")
        self.lineEditlastname = QtWidgets.QLineEdit(self.groupBoxpatology)
        self.lineEditlastname.setGeometry(QtCore.QRect(12, 50, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditlastname.setFont(font)
        self.lineEditlastname.setObjectName("lineEditlastname")
        self.lbllastname = QtWidgets.QLabel(self.groupBoxpatology)
        self.lbllastname.setGeometry(QtCore.QRect(160, 50, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lbllastname.setFont(font)
        self.lbllastname.setObjectName("lbllastname")
        self.lineEditfirstname = QtWidgets.QLineEdit(self.groupBoxpatology)
        self.lineEditfirstname.setGeometry(QtCore.QRect(260, 50, 113, 22))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditfirstname.setFont(font)
        self.lineEditfirstname.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEditfirstname.setObjectName("lineEditfirstname")
        self.pushButtonnewlab = QtWidgets.QPushButton(Form)
        self.pushButtonnewlab.setGeometry(QtCore.QRect(100, 300, 141, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(10)
        self.pushButtonnewlab.setFont(font)
        self.pushButtonnewlab.setObjectName("pushButtonnewlab")
        self.pushButtondelete = QtWidgets.QPushButton(Form)
        self.pushButtondelete.setGeometry(QtCore.QRect(280, 110, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        self.pushButtondelete.setFont(font)
        self.pushButtondelete.setObjectName("pushButtondelete")
        self.lblselecttest = QtWidgets.QLabel(Form)
        self.lblselecttest.setGeometry(QtCore.QRect(670, 119, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblselecttest.setFont(font)
        self.lblselecttest.setObjectName("lblselecttest")
        self.comboBoxselecttest = QtWidgets.QComboBox(Form)
        self.comboBoxselecttest.setGeometry(QtCore.QRect(530, 110, 141, 31))
        self.comboBoxselecttest.setObjectName("comboBoxselecttest")
        self.pushButtonaddtolist = QtWidgets.QPushButton(Form)
        self.pushButtonaddtolist.setGeometry(QtCore.QRect(400, 109, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonaddtolist.setFont(font)
        self.pushButtonaddtolist.setObjectName("pushButtonaddtolist")
        self.tableWidgetlab = QtWidgets.QTableWidget(Form)
        self.tableWidgetlab.setGeometry(QtCore.QRect(390, 171, 531, 410))
        self.tableWidgetlab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidgetlab.setObjectName("tableWidgetlab")
        self.tableWidgetlab.setColumnCount(4)
        self.tableWidgetlab.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetlab.setHorizontalHeaderItem(3, item)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 590, 101, 81))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 650, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(7)
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButtonprint = QtWidgets.QPushButton(Form)
        self.pushButtonprint.setGeometry(QtCore.QRect(120, 340, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Vazirmatn")
        font.setPointSize(12)
        self.pushButtonprint.setFont(font)
        self.pushButtonprint.setObjectName("pushButtonprint")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "آزمایشگاه"))
        self.lblclinicname.setText(_translate("Form", "درمانگاه دانشگاه پدافندهوایی خاتم الانبیاء(ص)"))
        self.groupBoxpatology.setTitle(_translate("Form", ":آزمایشگاه"))
        self.lblname.setText(_translate("Form", "نام:"))
        self.lbllastname.setText(_translate("Form", "نام خانوادگی:"))
        self.pushButtonnewlab.setText(_translate("Form", "تعریف کردن آزمایش جدید"))
        self.pushButtondelete.setText(_translate("Form", "حذف آزمایش"))
        self.lblselecttest.setText(_translate("Form", "انتخاب آزمایش:"))
        self.pushButtonaddtolist.setText(_translate("Form", "اضافه کردن به لیست"))
        item = self.tableWidgetlab.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidgetlab.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidgetlab.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidgetlab.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidgetlab.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidgetlab.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidgetlab.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidgetlab.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidgetlab.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidgetlab.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidgetlab.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Test Name"))
        item = self.tableWidgetlab.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Result"))
        item = self.tableWidgetlab.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Units"))
        item = self.tableWidgetlab.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Reference Range"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><img src=\":/newPrefix/image/xerxes.png\"/></p></body></html>"))
        self.label_3.setText(_translate("Form", "سازنده اثر: شرکت نرم افزاری XERXESS"))
        self.pushButtonprint.setText(_translate("Form", "چاپ"))
import resource_clinic_rc