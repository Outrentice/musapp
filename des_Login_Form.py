from PyQt6 import QtCore, QtGui, QtWidgets
from style_login_form import *


class UiLoginForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 300)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 40, 141, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_line_edit = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_line_edit.addStretch(1)
        self.verticalLayout_line_edit.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_line_edit.setObjectName("verticalLayout")
        self.login_line_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.login_line_edit.setObjectName("lineEdit")
        self.verticalLayout_line_edit.addWidget(self.login_line_edit)
        self.password_line_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_line_edit.setObjectName("lineEdit_2")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout_line_edit.addWidget(self.password_line_edit)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 140, 101, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_button = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_button.addStretch(1)
        self.verticalLayout_button.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_button.setObjectName("verticalLayout_2")
        self.sign_in_push_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sign_in_push_button.setObjectName("pushButton")
        self.verticalLayout_button.addWidget(self.sign_in_push_button)
        self.sign_up_push_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sign_up_push_button.setObjectName("pushButton_2")
        self.verticalLayout_button.addWidget(self.sign_up_push_button)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(123, 190, 261, 21))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.error_label.setText("")
        self.error_label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.error_label)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login_line_edit.setPlaceholderText(_translate("Form", "Login.."))
        self.password_line_edit.setPlaceholderText(_translate("Form", "Password.."))
        self.sign_in_push_button.setText(_translate("Form", "Sign In"))
        self.sign_up_push_button.setText(_translate("Form", "Sign Up"))


class UiSignUpForm(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(330, 300)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 40, 141, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.login_register_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.login_register_line_edit.setToolTip("")
        self.login_register_line_edit.setStatusTip("")
        self.login_register_line_edit.setWhatsThis("")
        self.login_register_line_edit.setInputMask("")
        self.login_register_line_edit.setText("")
        self.login_register_line_edit.setObjectName("login_register_line_edit")
        self.verticalLayout.addWidget(self.login_register_line_edit)
        self.email_register_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.email_register_line_edit.setObjectName("email_register_line_edit")
        self.verticalLayout.addWidget(self.email_register_line_edit)
        self.phone_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.phone_line_edit.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.phone_line_edit)
        self.password_line_edit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password_line_edit.setObjectName("lineEdit")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.verticalLayout.addWidget(self.password_line_edit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(120, 140, 101, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.sign_up_register_push_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.sign_up_register_push_button.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.sign_up_register_push_button)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(45, 170, 261, 21))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.error_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.error_label.setText("")
        self.error_label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.error_label)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login_register_line_edit.setPlaceholderText(_translate("Form", "Login.."))
        self.email_register_line_edit.setPlaceholderText(_translate("Form", "Email.."))
        self.phone_line_edit.setPlaceholderText(_translate("Form", "Phone.."))
        self.password_line_edit.setPlaceholderText(_translate("Form", "Password.."))
        self.sign_up_register_push_button.setText(_translate("Form", "Sign up"))


class UiUserProfile(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1009, 590)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        Form.setFont(font)
        Form.setStyleSheet("background-color: rgb(62, 79, 65);")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(350, 370, 504, 152))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_playlist = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_playlist.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_playlist.setSpacing(26)
        self.horizontalLayout_playlist.setObjectName("horizontalLayout_playlist")
        self.playlist1_into_main = QtWidgets.QPushButton(self.layoutWidget)
        self.playlist1_into_main.setMinimumSize(QtCore.QSize(150, 150))
        self.playlist1_into_main.setMaximumSize(QtCore.QSize(150, 150))
        self.playlist1_into_main.setStyleSheet("border: 1px solid black; border-radius: 7%;"
                                               "background-color: rgb(89, 114, 93);")
        self.playlist1_into_main.setObjectName("playlist1_into_main")
        self.horizontalLayout_playlist.addWidget(self.playlist1_into_main)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(180, 0, 10, 591))
        self.label_5.setStyleSheet("background-color: rgb(33, 34, 32);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 0, 181, 591))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_sidebar = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_sidebar.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_sidebar.setObjectName("verticalLayout_sidebar")
        self.label_musapp = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_musapp.setMaximumSize(QtCore.QSize(180, 16777215))
        self.label_musapp.setObjectName("label_musapp")
        self.verticalLayout_sidebar.addWidget(self.label_musapp)
        self.toolBox = QtWidgets.QToolBox(self.layoutWidget_2)
        self.toolBox.setMaximumSize(QtCore.QSize(180, 16777215))
        self.toolBox.setStyleSheet("background-color: rgb(89, 114, 93);")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 179, 516))
        self.page.setObjectName("page")
        self.artist1_in_scroll = QtWidgets.QPushButton(self.page)
        self.artist1_in_scroll.setGeometry(QtCore.QRect(30, 10, 113, 32))
        self.artist1_in_scroll.setObjectName("artist1_in_scroll")
        self.artist2_in_scroll = QtWidgets.QPushButton(self.page)
        self.artist2_in_scroll.setGeometry(QtCore.QRect(30, 60, 113, 32))
        self.artist2_in_scroll.setObjectName("artist2_in_scroll")
        self.artist3_in_scroll = QtWidgets.QPushButton(self.page)
        self.artist3_in_scroll.setGeometry(QtCore.QRect(30, 110, 113, 32))
        self.artist3_in_scroll.setObjectName("artist3_in_scroll")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 179, 516))
        self.page_2.setObjectName("page_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea.setGeometry(QtCore.QRect(0, -10, 181, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_in_scroll = QtWidgets.QVBoxLayout()
        self.verticalLayout_in_scroll.setObjectName("verticalLayout_in_scroll")
        self.playlist1_into_scroll = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.playlist1_into_scroll.setMinimumSize(QtCore.QSize(150, 150))
        self.playlist1_into_scroll.setObjectName("playlist1_into_scroll")
        self.playlist1_into_scroll.setStyleSheet("border: 1px solid black; border-radius: 7%;"
                                                 "background-color: rgb(62, 79, 65);")
        self.verticalLayout_in_scroll.addWidget(self.playlist1_into_scroll)
        self.verticalLayout_4.addLayout(self.verticalLayout_in_scroll)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_sidebar.addWidget(self.toolBox)
        self.username = QtWidgets.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(470, 250, 250, 51))
        self.username.setMinimumSize(QtCore.QSize(250, 0))
        self.username.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.username.setObjectName("username")
        self.Profile_picture = QtWidgets.QLabel(Form)
        self.Profile_picture.setEnabled(True)
        self.Profile_picture.setGeometry(QtCore.QRect(510, 40, 180, 181))
        self.Profile_picture.setMinimumSize(QtCore.QSize(180, 180))
        self.Profile_picture.setStyleSheet("border: 1px solid black; border-radius: 3%;")
        self.Profile_picture.setObjectName("Profile_picture")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(590, 530, 31, 31))
        self.pushButton.setStyleSheet("border: 1.5px solid black; border-radius: 15%;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/stade/Downloads/plus-alt-svgrepo-com.svg"))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.playlist1_into_main.setText(_translate("Form", "playlist1"))
        self.label_musapp.setText(_translate("Form", "musapp"))
        self.artist1_in_scroll.setText(_translate("Form", "artist 1"))
        self.artist2_in_scroll.setText(_translate("Form", "artist 2"))
        self.artist3_in_scroll.setText(_translate("Form", "artist 3"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Artists"))
        self.playlist1_into_scroll.setText(_translate("Form", "playlist 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "playlists"))
        self.username.setText(_translate("Form", "Username"))
        self.Profile_picture.setText(_translate("Form", "Profile Pic"))
        # self.pushButton.setText(_translate("Form", "+"))


class UiCreatePlaylist(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton_Create = QtWidgets.QPushButton(Dialog)
        self.pushButton_Create.setGeometry(QtCore.QRect(160, 250, 75, 23))
        self.pushButton_Create.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(130, 100, 135, 41))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.error_label = QtWidgets.QLabel(self.widget)
        self.error_label.setText("")
        self.error_label.setObjectName("label")
        self.error_label.setStyleSheet("color: rgb(202, 0, 0);")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addWidget(self.error_label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_Create.setText(_translate("Dialog", "Create"))
        self.label.setText(_translate("Dialog", "Playlist name:"))


