"""
Created on Fri Dec 20 18:12:05 2019

@author: AGHEZZAF Mohamed
@email:  aghe.mohamed@gmail.com
"""



from PyQt5 import QtCore, QtGui, QtWidgets
from acceuil import Ui_Form

class Ui_FormSign(object):
    def connexion(self):
            md =self.lineEdit_2.text()
            id=self.lineEdit.text()
            if id!="" and md!="":
                if(id=="admin" and md=="admin"):
                    print("valide")
                    self.window = QtWidgets.QMainWindow()
                    self.ui = Ui_Form()
                    self.ui.setupUi(self.window)
                    Form.hide()
                    self.window.show()
                            
                else:
                    print("Les données sont incorréctes")
                    self.lineEdit.clear()
                    self.lineEdit_2.clear()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(369, 500)
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        Form.setFont(font)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setFocusPolicy(QtCore.Qt.NoFocus)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(False)
        Form.setToolTip("")
        Form.setStatusTip("")
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("*{\n"
"font-size:20px;\n"
"font-family:sans-serif;\n"
"}\n"
"#label{\n"
"\n"
"    color: #fff;\n"
"    text-align: center;\n"
"    font-family:  Tahoma, sans-serif;\n"
"}\n"
"#label_2{\n"
"background:#13386d;\n"
"height: 5px\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"}\n"
"#frame1{\n"
"background:#3d3d3d;\n"
"}\n"
"#pushButton{\n"
"background:rgb(80, 80, 80);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"#pushButton_2{\n"
"  display:block;\n"
"  height: 300px;\n"
"  width: 300px;\n"
"  border-radius: 50%;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"background:rgb(111, 111, 111);\n"
"color:#fff;\n"
"border-radius:15px;\n"
"}\n"
"QLineEdit\n"
"{\n"
"border-radius:15px;\n"
"background:transparent;\n"
"border:none;\n"
"color:#fff;\n"
"border-bottom:1px solid #fff;\n"
"}\n"
"#plainTextEdit{\n"
"  width: 100%;\n"
"  height: 150px;\n"
"  padding: 2px 4px;\n"
"  box-sizing: border-box;\n"
"  border: 0.2px solid #ccc;\n"
"  border-radius: 0.5px;\n"
"  background-color: #f8f8f8;\n"
"  resize: none;\n"
"overflow:hidden;\n"
"}\n"
".scroll::-webkit-scrollbar {\n"
"   display: none;\n"
" }")
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame1 = QtWidgets.QFrame(Form)
        self.frame1.setGeometry(QtCore.QRect(0, 0, 371, 501))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame1)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 20, 121, 121))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setTabletTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAccessibleDescription("")
        self.pushButton_2.setAutoFillBackground(False)
        self.pushButton_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(120, 120))
        self.pushButton_2.setShortcut("")
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setChecked(False)
        self.pushButton_2.setAutoRepeat(False)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame1)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 430, 341, 41))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 370, 321, 41))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(20, 340, 141, 41))
        self.label_3.setMouseTracking(True)
        self.label_3.setTabletTracking(False)
        self.label_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_3.setAcceptDrops(False)
        self.label_3.setStatusTip("")
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setWordWrap(False)
        self.label_3.setOpenExternalLinks(False)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.frame1)
        self.lineEdit.setGeometry(QtCore.QRect(20, 270, 321, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.frame1)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("sans-serif")
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setTabletTracking(False)
        self.label_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_4.setAcceptDrops(False)
        self.label_4.setStatusTip("")
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_4.setObjectName("label_4")
        self.pushButton.clicked.connect(self.connexion)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Authentification"))
        self.pushButton.setText(_translate("Form", "Connexion"))
        self.lineEdit_2.setText(_translate("Form", ""))
        self.label_3.setText(_translate("Form", "Mot de passe"))
        self.lineEdit.setText(_translate("Form", ""))
        self.label_4.setText(_translate("Form", "Identification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_FormSign()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
