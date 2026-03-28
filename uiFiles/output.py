# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prototype3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QListView, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 480)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(600, 480))
        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 10, 581, 461))
        self.forStretchVerticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.forStretchVerticalLayout.setObjectName(u"forStretchVerticalLayout")
        self.forStretchVerticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MainPages = QStackedWidget(self.verticalLayoutWidget_2)
        self.MainPages.setObjectName(u"MainPages")
        sizePolicy.setHeightForWidth(self.MainPages.sizePolicy().hasHeightForWidth())
        self.MainPages.setSizePolicy(sizePolicy)
        self.pageLogin = QWidget()
        self.pageLogin.setObjectName(u"pageLogin")
        sizePolicy.setHeightForWidth(self.pageLogin.sizePolicy().hasHeightForWidth())
        self.pageLogin.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_5 = QWidget(self.pageLogin)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 0, 581, 461))
        self.VLLogin = QVBoxLayout(self.verticalLayoutWidget_5)
        self.VLLogin.setSpacing(0)
        self.VLLogin.setObjectName(u"VLLogin")
        self.VLLogin.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_6 = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLLogin.addItem(self.verticalSpacer_6)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_28 = QSpacerItem(80, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_28)

        self.label_2 = QLabel(self.verticalLayoutWidget_5)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_2)

        self.horizontalSpacer_29 = QSpacerItem(80, 5, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)


        self.VLLogin.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_27 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_27)

        self.label_9 = QLabel(self.verticalLayoutWidget_5)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_9.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label_9)


        self.VLLogin.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 0, -1, 20)
        self.horizontalSpacer_26 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_26)

        self.loginUsername = QTextEdit(self.verticalLayoutWidget_5)
        self.loginUsername.setObjectName(u"loginUsername")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loginUsername.sizePolicy().hasHeightForWidth())
        self.loginUsername.setSizePolicy(sizePolicy1)

        self.horizontalLayout_21.addWidget(self.loginUsername)

        self.horizontalSpacer_24 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_24)


        self.VLLogin.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_23 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_23)

        self.label_10 = QLabel(self.verticalLayoutWidget_5)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setFont(font1)

        self.horizontalLayout_20.addWidget(self.label_10)


        self.VLLogin.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 20)
        self.horizontalSpacer_25 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_25)

        self.loginPassword = QTextEdit(self.verticalLayoutWidget_5)
        self.loginPassword.setObjectName(u"loginPassword")
        sizePolicy1.setHeightForWidth(self.loginPassword.sizePolicy().hasHeightForWidth())
        self.loginPassword.setSizePolicy(sizePolicy1)

        self.horizontalLayout_19.addWidget(self.loginPassword)

        self.horizontalSpacer_22 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_22)


        self.VLLogin.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_30 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_30)

        self.loginRegisterBtn = QPushButton(self.verticalLayoutWidget_5)
        self.loginRegisterBtn.setObjectName(u"loginRegisterBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.loginRegisterBtn.sizePolicy().hasHeightForWidth())
        self.loginRegisterBtn.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.loginRegisterBtn.setFont(font2)

        self.horizontalLayout_18.addWidget(self.loginRegisterBtn)

        self.horizontalSpacer_31 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_31)

        self.loginConfirmBtn = QPushButton(self.verticalLayoutWidget_5)
        self.loginConfirmBtn.setObjectName(u"loginConfirmBtn")
        sizePolicy3.setHeightForWidth(self.loginConfirmBtn.sizePolicy().hasHeightForWidth())
        self.loginConfirmBtn.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.loginConfirmBtn.setFont(font3)

        self.horizontalLayout_18.addWidget(self.loginConfirmBtn)

        self.horizontalSpacer_21 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_21)


        self.VLLogin.addLayout(self.horizontalLayout_18)

        self.verticalSpacer_5 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLLogin.addItem(self.verticalSpacer_5)

        self.MainPages.addWidget(self.pageLogin)
        self.pageRegister = QWidget()
        self.pageRegister.setObjectName(u"pageRegister")
        sizePolicy.setHeightForWidth(self.pageRegister.sizePolicy().hasHeightForWidth())
        self.pageRegister.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_6 = QWidget(self.pageRegister)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 0, 581, 461))
        self.VLRegister = QVBoxLayout(self.verticalLayoutWidget_6)
        self.VLRegister.setSpacing(0)
        self.VLRegister.setObjectName(u"VLRegister")
        self.VLRegister.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_7 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLRegister.addItem(self.verticalSpacer_7)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_33)

        self.label_3 = QLabel(self.verticalLayoutWidget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_31.addWidget(self.label_3)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_34)


        self.VLRegister.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_32 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_32)

        self.label_11 = QLabel(self.verticalLayoutWidget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_11)


        self.VLRegister.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_35 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_35)

        self.registerUsername = QTextEdit(self.verticalLayoutWidget_6)
        self.registerUsername.setObjectName(u"registerUsername")
        sizePolicy1.setHeightForWidth(self.registerUsername.sizePolicy().hasHeightForWidth())
        self.registerUsername.setSizePolicy(sizePolicy1)

        self.horizontalLayout_29.addWidget(self.registerUsername)

        self.horizontalSpacer_36 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_36)


        self.VLRegister.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_51 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_51)

        self.label_17 = QLabel(self.verticalLayoutWidget_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_35.addWidget(self.label_17)

        self.label_14 = QLabel(self.verticalLayoutWidget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_35.addWidget(self.label_14)

        self.horizontalSpacer_54 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_35.addItem(self.horizontalSpacer_54)


        self.VLRegister.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_52 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_52)

        self.registerUsername_2 = QTextEdit(self.verticalLayoutWidget_6)
        self.registerUsername_2.setObjectName(u"registerUsername_2")
        sizePolicy1.setHeightForWidth(self.registerUsername_2.sizePolicy().hasHeightForWidth())
        self.registerUsername_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_39.addWidget(self.registerUsername_2)

        self.registerUsername_3 = QTextEdit(self.verticalLayoutWidget_6)
        self.registerUsername_3.setObjectName(u"registerUsername_3")
        sizePolicy1.setHeightForWidth(self.registerUsername_3.sizePolicy().hasHeightForWidth())
        self.registerUsername_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_39.addWidget(self.registerUsername_3)

        self.horizontalSpacer_53 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_53)


        self.VLRegister.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_37 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_37)

        self.label_12 = QLabel(self.verticalLayoutWidget_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_12)


        self.VLRegister.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_45 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_45)

        self.registerPassword = QTextEdit(self.verticalLayoutWidget_6)
        self.registerPassword.setObjectName(u"registerPassword")
        sizePolicy1.setHeightForWidth(self.registerPassword.sizePolicy().hasHeightForWidth())
        self.registerPassword.setSizePolicy(sizePolicy1)

        self.horizontalLayout_27.addWidget(self.registerPassword)

        self.horizontalSpacer_38 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_38)


        self.VLRegister.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 5, -1, -1)
        self.horizontalSpacer_44 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_44)

        self.label_13 = QLabel(self.verticalLayoutWidget_6)
        self.label_13.setObjectName(u"label_13")
        sizePolicy2.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy2)
        self.label_13.setFont(font1)

        self.horizontalLayout_26.addWidget(self.label_13)


        self.VLRegister.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, -1, -1, 5)
        self.horizontalSpacer_41 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_41)

        self.registerConfirmPassword = QTextEdit(self.verticalLayoutWidget_6)
        self.registerConfirmPassword.setObjectName(u"registerConfirmPassword")
        sizePolicy1.setHeightForWidth(self.registerConfirmPassword.sizePolicy().hasHeightForWidth())
        self.registerConfirmPassword.setSizePolicy(sizePolicy1)

        self.horizontalLayout_25.addWidget(self.registerConfirmPassword)

        self.horizontalSpacer_40 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_40)


        self.VLRegister.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 5, -1, 5)
        self.horizontalSpacer_42 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_42)

        self.registerLoginBtn = QPushButton(self.verticalLayoutWidget_6)
        self.registerLoginBtn.setObjectName(u"registerLoginBtn")
        sizePolicy3.setHeightForWidth(self.registerLoginBtn.sizePolicy().hasHeightForWidth())
        self.registerLoginBtn.setSizePolicy(sizePolicy3)
        self.registerLoginBtn.setFont(font3)

        self.horizontalLayout_24.addWidget(self.registerLoginBtn)

        self.horizontalSpacer_43 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_43)

        self.registerConfirmBtn = QPushButton(self.verticalLayoutWidget_6)
        self.registerConfirmBtn.setObjectName(u"registerConfirmBtn")
        sizePolicy3.setHeightForWidth(self.registerConfirmBtn.sizePolicy().hasHeightForWidth())
        self.registerConfirmBtn.setSizePolicy(sizePolicy3)
        self.registerConfirmBtn.setFont(font3)

        self.horizontalLayout_24.addWidget(self.registerConfirmBtn)

        self.horizontalSpacer_39 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_39)


        self.VLRegister.addLayout(self.horizontalLayout_24)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLRegister.addItem(self.verticalSpacer_8)

        self.MainPages.addWidget(self.pageRegister)
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        sizePolicy.setHeightForWidth(self.pageHome.sizePolicy().hasHeightForWidth())
        self.pageHome.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.pageHome)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 581, 461))
        self.VLHome = QVBoxLayout(self.verticalLayoutWidget)
        self.VLHome.setObjectName(u"VLHome")
        self.VLHome.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.VLHome.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.homeUserName = QLabel(self.verticalLayoutWidget)
        self.homeUserName.setObjectName(u"homeUserName")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.homeUserName.setFont(font4)

        self.horizontalLayout.addWidget(self.homeUserName)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.homeSearchBar = QLineEdit(self.verticalLayoutWidget)
        self.homeSearchBar.setObjectName(u"homeSearchBar")

        self.horizontalLayout.addWidget(self.homeSearchBar)

        self.horizontalSpacer_13 = QSpacerItem(10, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_13)

        self.homeLogoutBtn = QPushButton(self.verticalLayoutWidget)
        self.homeLogoutBtn.setObjectName(u"homeLogoutBtn")
        font5 = QFont()
        font5.setBold(True)
        self.homeLogoutBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.homeLogoutBtn)

        self.homeAddRoomBtn = QPushButton(self.verticalLayoutWidget)
        self.homeAddRoomBtn.setObjectName(u"homeAddRoomBtn")
        self.homeAddRoomBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.homeAddRoomBtn)

        self.homeCreateRoomBtn = QPushButton(self.verticalLayoutWidget)
        self.homeCreateRoomBtn.setObjectName(u"homeCreateRoomBtn")
        self.homeCreateRoomBtn.setFont(font5)

        self.horizontalLayout.addWidget(self.homeCreateRoomBtn)


        self.VLHome.addLayout(self.horizontalLayout)

        self.scrollArea = QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy4)
        self.scrollArea.setSizeIncrement(QSize(1, 1))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 577, 419))
        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.VLHome.addWidget(self.scrollArea)

        self.MainPages.addWidget(self.pageHome)
        self.pageCreateRoom = QWidget()
        self.pageCreateRoom.setObjectName(u"pageCreateRoom")
        sizePolicy.setHeightForWidth(self.pageCreateRoom.sizePolicy().hasHeightForWidth())
        self.pageCreateRoom.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_3 = QWidget(self.pageCreateRoom)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(0, 0, 581, 461))
        self.VLCreateRoom = QVBoxLayout(self.verticalLayoutWidget_3)
        self.VLCreateRoom.setSpacing(0)
        self.VLCreateRoom.setObjectName(u"VLCreateRoom")
        self.VLCreateRoom.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.VLCreateRoom.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 70, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLCreateRoom.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.VLCreateRoom.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_7)


        self.VLCreateRoom.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_7 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)

        self.createRoomName = QTextEdit(self.verticalLayoutWidget_3)
        self.createRoomName.setObjectName(u"createRoomName")
        self.createRoomName.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.createRoomName.sizePolicy().hasHeightForWidth())
        self.createRoomName.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.createRoomName)

        self.horizontalSpacer_8 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)


        self.VLCreateRoom.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 20, -1, -1)
        self.horizontalSpacer_4 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(self.verticalLayoutWidget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_8)


        self.VLCreateRoom.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_5 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.createRoomDescription = QTextEdit(self.verticalLayoutWidget_3)
        self.createRoomDescription.setObjectName(u"createRoomDescription")
        sizePolicy1.setHeightForWidth(self.createRoomDescription.sizePolicy().hasHeightForWidth())
        self.createRoomDescription.setSizePolicy(sizePolicy1)

        self.horizontalLayout_9.addWidget(self.createRoomDescription)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)


        self.VLCreateRoom.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 10, -1, 10)
        self.horizontalSpacer_9 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.createRoomCancleBtn = QPushButton(self.verticalLayoutWidget_3)
        self.createRoomCancleBtn.setObjectName(u"createRoomCancleBtn")
        sizePolicy3.setHeightForWidth(self.createRoomCancleBtn.sizePolicy().hasHeightForWidth())
        self.createRoomCancleBtn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.createRoomCancleBtn)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)

        self.createRoomConfirmBtn = QPushButton(self.verticalLayoutWidget_3)
        self.createRoomConfirmBtn.setObjectName(u"createRoomConfirmBtn")
        sizePolicy3.setHeightForWidth(self.createRoomConfirmBtn.sizePolicy().hasHeightForWidth())
        self.createRoomConfirmBtn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_10.addWidget(self.createRoomConfirmBtn)

        self.horizontalSpacer_10 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.VLCreateRoom.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_2 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLCreateRoom.addItem(self.verticalSpacer_2)

        self.MainPages.addWidget(self.pageCreateRoom)
        self.pageJoinRoom = QWidget()
        self.pageJoinRoom.setObjectName(u"pageJoinRoom")
        sizePolicy.setHeightForWidth(self.pageJoinRoom.sizePolicy().hasHeightForWidth())
        self.pageJoinRoom.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_4 = QWidget(self.pageJoinRoom)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 0, 581, 461))
        self.VLJoinRoom = QVBoxLayout(self.verticalLayoutWidget_4)
        self.VLJoinRoom.setSpacing(0)
        self.VLJoinRoom.setObjectName(u"VLJoinRoom")
        self.VLJoinRoom.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_4 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLJoinRoom.addItem(self.verticalSpacer_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_12)

        self.label_15 = QLabel(self.verticalLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy5)
        self.label_15.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)


        self.VLJoinRoom.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 15, -1, 15)
        self.horizontalSpacer_16 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.label_16 = QLabel(self.verticalLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Ignored)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy6)
        self.label_16.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_16)

        self.horizontalSpacer_50 = QSpacerItem(10, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_50)

        self.joinRoomCode = QTextEdit(self.verticalLayoutWidget_4)
        self.joinRoomCode.setObjectName(u"joinRoomCode")
        sizePolicy1.setHeightForWidth(self.joinRoomCode.sizePolicy().hasHeightForWidth())
        self.joinRoomCode.setSizePolicy(sizePolicy1)

        self.horizontalLayout_17.addWidget(self.joinRoomCode)

        self.horizontalSpacer_17 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)


        self.VLJoinRoom.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 15, -1, 15)
        self.horizontalSpacer_19 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.joinRoomCancleBtn = QPushButton(self.verticalLayoutWidget_4)
        self.joinRoomCancleBtn.setObjectName(u"joinRoomCancleBtn")
        sizePolicy3.setHeightForWidth(self.joinRoomCancleBtn.sizePolicy().hasHeightForWidth())
        self.joinRoomCancleBtn.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.joinRoomCancleBtn)

        self.horizontalSpacer_20 = QSpacerItem(40, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_20)

        self.joinRoomConfirm = QPushButton(self.verticalLayoutWidget_4)
        self.joinRoomConfirm.setObjectName(u"joinRoomConfirm")
        sizePolicy3.setHeightForWidth(self.joinRoomConfirm.sizePolicy().hasHeightForWidth())
        self.joinRoomConfirm.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.joinRoomConfirm)

        self.horizontalSpacer_18 = QSpacerItem(80, 5, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_18)


        self.VLJoinRoom.addLayout(self.horizontalLayout_15)

        self.verticalSpacer_3 = QSpacerItem(20, 120, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLJoinRoom.addItem(self.verticalSpacer_3)

        self.MainPages.addWidget(self.pageJoinRoom)
        self.pageRoom = QWidget()
        self.pageRoom.setObjectName(u"pageRoom")
        sizePolicy.setHeightForWidth(self.pageRoom.sizePolicy().hasHeightForWidth())
        self.pageRoom.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_7 = QWidget(self.pageRoom)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(0, 0, 581, 461))
        self.VLRoom = QVBoxLayout(self.verticalLayoutWidget_7)
        self.VLRoom.setSpacing(0)
        self.VLRoom.setObjectName(u"VLRoom")
        self.VLRoom.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.roomHomeBtn = QPushButton(self.verticalLayoutWidget_7)
        self.roomHomeBtn.setObjectName(u"roomHomeBtn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.roomHomeBtn.sizePolicy().hasHeightForWidth())
        self.roomHomeBtn.setSizePolicy(sizePolicy7)
        self.roomHomeBtn.setFont(font2)

        self.horizontalLayout_34.addWidget(self.roomHomeBtn)

        self.horizontalSpacer_49 = QSpacerItem(10, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_49)

        self.roomCode = QLabel(self.verticalLayoutWidget_7)
        self.roomCode.setObjectName(u"roomCode")
        sizePolicy7.setHeightForWidth(self.roomCode.sizePolicy().hasHeightForWidth())
        self.roomCode.setSizePolicy(sizePolicy7)
        font6 = QFont()
        font6.setPointSize(15)
        font6.setBold(True)
        self.roomCode.setFont(font6)

        self.horizontalLayout_34.addWidget(self.roomCode)

        self.roomName = QLabel(self.verticalLayoutWidget_7)
        self.roomName.setObjectName(u"roomName")
        sizePolicy3.setHeightForWidth(self.roomName.sizePolicy().hasHeightForWidth())
        self.roomName.setSizePolicy(sizePolicy3)
        self.roomName.setFont(font6)

        self.horizontalLayout_34.addWidget(self.roomName)


        self.VLRoom.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")

        self.VLRoom.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 20, 10, 20)
        self.roomChatBtn = QPushButton(self.verticalLayoutWidget_7)
        self.roomChatBtn.setObjectName(u"roomChatBtn")
        sizePolicy3.setHeightForWidth(self.roomChatBtn.sizePolicy().hasHeightForWidth())
        self.roomChatBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.roomChatBtn)

        self.roomCallBtn = QPushButton(self.verticalLayoutWidget_7)
        self.roomCallBtn.setObjectName(u"roomCallBtn")
        sizePolicy3.setHeightForWidth(self.roomCallBtn.sizePolicy().hasHeightForWidth())
        self.roomCallBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.roomCallBtn)

        self.roomWorkshopBtn = QPushButton(self.verticalLayoutWidget_7)
        self.roomWorkshopBtn.setObjectName(u"roomWorkshopBtn")
        sizePolicy3.setHeightForWidth(self.roomWorkshopBtn.sizePolicy().hasHeightForWidth())
        self.roomWorkshopBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.roomWorkshopBtn)

        self.roomMemberBtn = QPushButton(self.verticalLayoutWidget_7)
        self.roomMemberBtn.setObjectName(u"roomMemberBtn")
        sizePolicy3.setHeightForWidth(self.roomMemberBtn.sizePolicy().hasHeightForWidth())
        self.roomMemberBtn.setSizePolicy(sizePolicy3)

        self.verticalLayout_2.addWidget(self.roomMemberBtn)


        self.horizontalLayout_32.addLayout(self.verticalLayout_2)

        self.SubPages = QStackedWidget(self.verticalLayoutWidget_7)
        self.SubPages.setObjectName(u"SubPages")
        sizePolicy.setHeightForWidth(self.SubPages.sizePolicy().hasHeightForWidth())
        self.SubPages.setSizePolicy(sizePolicy)
        self.pageChat = QWidget()
        self.pageChat.setObjectName(u"pageChat")
        sizePolicy.setHeightForWidth(self.pageChat.sizePolicy().hasHeightForWidth())
        self.pageChat.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_11 = QWidget(self.pageChat)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(0, 0, 481, 421))
        self.VLChat = QVBoxLayout(self.verticalLayoutWidget_11)
        self.VLChat.setObjectName(u"VLChat")
        self.VLChat.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_46)

        self.label_5 = QLabel(self.verticalLayoutWidget_11)
        self.label_5.setObjectName(u"label_5")
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.label_5.setFont(font7)

        self.horizontalLayout_36.addWidget(self.label_5)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_36.addItem(self.horizontalSpacer_47)


        self.VLChat.addLayout(self.horizontalLayout_36)

        self.chatHistoryArea = QScrollArea(self.verticalLayoutWidget_11)
        self.chatHistoryArea.setObjectName(u"chatHistoryArea")
        self.chatHistoryArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 477, 336))
        self.chatHistoryArea.setWidget(self.scrollAreaWidgetContents_2)

        self.VLChat.addWidget(self.chatHistoryArea)

        self.verticalSpacer_9 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.VLChat.addItem(self.verticalSpacer_9)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(-1, 0, 0, -1)
        self.chatSendTextEdit = QTextEdit(self.verticalLayoutWidget_11)
        self.chatSendTextEdit.setObjectName(u"chatSendTextEdit")
        sizePolicy1.setHeightForWidth(self.chatSendTextEdit.sizePolicy().hasHeightForWidth())
        self.chatSendTextEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_37.addWidget(self.chatSendTextEdit)

        self.chatSendTextConfirmBtn = QPushButton(self.verticalLayoutWidget_11)
        self.chatSendTextConfirmBtn.setObjectName(u"chatSendTextConfirmBtn")
        sizePolicy3.setHeightForWidth(self.chatSendTextConfirmBtn.sizePolicy().hasHeightForWidth())
        self.chatSendTextConfirmBtn.setSizePolicy(sizePolicy3)
        self.chatSendTextConfirmBtn.setFont(font2)

        self.horizontalLayout_37.addWidget(self.chatSendTextConfirmBtn)


        self.VLChat.addLayout(self.horizontalLayout_37)

        self.SubPages.addWidget(self.pageChat)
        self.pageCall = QWidget()
        self.pageCall.setObjectName(u"pageCall")
        sizePolicy.setHeightForWidth(self.pageCall.sizePolicy().hasHeightForWidth())
        self.pageCall.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_10 = QWidget(self.pageCall)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(0, 0, 481, 421))
        self.VLCall = QVBoxLayout(self.verticalLayoutWidget_10)
        self.VLCall.setSpacing(0)
        self.VLCall.setObjectName(u"VLCall")
        self.VLCall.setContentsMargins(40, 40, 40, 40)
        self.enterOrLeaveCall = QPushButton(self.verticalLayoutWidget_10)
        self.enterOrLeaveCall.setObjectName(u"enterOrLeaveCall")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.enterOrLeaveCall.sizePolicy().hasHeightForWidth())
        self.enterOrLeaveCall.setSizePolicy(sizePolicy8)

        self.VLCall.addWidget(self.enterOrLeaveCall)

        self.SubPages.addWidget(self.pageCall)
        self.pageWorkShop = QWidget()
        self.pageWorkShop.setObjectName(u"pageWorkShop")
        sizePolicy.setHeightForWidth(self.pageWorkShop.sizePolicy().hasHeightForWidth())
        self.pageWorkShop.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_12 = QWidget(self.pageWorkShop)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(0, 0, 481, 421))
        self.VLWorkShop = QVBoxLayout(self.verticalLayoutWidget_12)
        self.VLWorkShop.setObjectName(u"VLWorkShop")
        self.VLWorkShop.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_6 = QLabel(self.verticalLayoutWidget_12)
        self.label_6.setObjectName(u"label_6")
        sizePolicy7.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy7)
        self.label_6.setFont(font3)

        self.horizontalLayout_38.addWidget(self.label_6)

        self.workshopRunBtn = QPushButton(self.verticalLayoutWidget_12)
        self.workshopRunBtn.setObjectName(u"workshopRunBtn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.workshopRunBtn.sizePolicy().hasHeightForWidth())
        self.workshopRunBtn.setSizePolicy(sizePolicy9)
        self.workshopRunBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopRunBtn)

        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_48)

        self.workshopImportBtn = QPushButton(self.verticalLayoutWidget_12)
        self.workshopImportBtn.setObjectName(u"workshopImportBtn")
        sizePolicy9.setHeightForWidth(self.workshopImportBtn.sizePolicy().hasHeightForWidth())
        self.workshopImportBtn.setSizePolicy(sizePolicy9)
        self.workshopImportBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopImportBtn)

        self.workshopExportBtn = QPushButton(self.verticalLayoutWidget_12)
        self.workshopExportBtn.setObjectName(u"workshopExportBtn")
        sizePolicy9.setHeightForWidth(self.workshopExportBtn.sizePolicy().hasHeightForWidth())
        self.workshopExportBtn.setSizePolicy(sizePolicy9)
        self.workshopExportBtn.setFont(font3)

        self.horizontalLayout_38.addWidget(self.workshopExportBtn)


        self.VLWorkShop.addLayout(self.horizontalLayout_38)

        self.workshopCodeSpace = QTextEdit(self.verticalLayoutWidget_12)
        self.workshopCodeSpace.setObjectName(u"workshopCodeSpace")

        self.VLWorkShop.addWidget(self.workshopCodeSpace)

        self.SubPages.addWidget(self.pageWorkShop)
        self.pageMember = QWidget()
        self.pageMember.setObjectName(u"pageMember")
        sizePolicy.setHeightForWidth(self.pageMember.sizePolicy().hasHeightForWidth())
        self.pageMember.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget_9 = QWidget(self.pageMember)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(0, 0, 481, 421))
        self.VLMember = QVBoxLayout(self.verticalLayoutWidget_9)
        self.VLMember.setObjectName(u"VLMember")
        self.VLMember.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.verticalLayoutWidget_9)
        self.listView.setObjectName(u"listView")

        self.VLMember.addWidget(self.listView)

        self.SubPages.addWidget(self.pageMember)

        self.horizontalLayout_32.addWidget(self.SubPages)


        self.VLRoom.addLayout(self.horizontalLayout_32)

        self.MainPages.addWidget(self.pageRoom)

        self.forStretchVerticalLayout.addWidget(self.MainPages)


        self.retranslateUi(Form)

        self.MainPages.setCurrentIndex(1)
        self.SubPages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Username :", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Password : ", None))
        self.loginRegisterBtn.setText(QCoreApplication.translate("Form", u"Register", None))
        self.loginConfirmBtn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Register", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Username :", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"Gmail :", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Phone Number :", None))
        self.registerUsername_2.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Password : ", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Confirm Password :", None))
        self.registerLoginBtn.setText(QCoreApplication.translate("Form", u"Login", None))
        self.registerConfirmBtn.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.homeUserName.setText(QCoreApplication.translate("Form", u"Name Surname", None))
        self.homeLogoutBtn.setText(QCoreApplication.translate("Form", u"logout", None))
        self.homeAddRoomBtn.setText(QCoreApplication.translate("Form", u"Add", None))
        self.homeCreateRoomBtn.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Create Room", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Room Name :", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Description :", None))
        self.createRoomCancleBtn.setText(QCoreApplication.translate("Form", u"Cancle", None))
        self.createRoomConfirmBtn.setText(QCoreApplication.translate("Form", u"Create", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Join Room", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Room Code:", None))
        self.joinRoomCancleBtn.setText(QCoreApplication.translate("Form", u"Cancle", None))
        self.joinRoomConfirm.setText(QCoreApplication.translate("Form", u"Confirm", None))
        self.roomHomeBtn.setText(QCoreApplication.translate("Form", u"Home", None))
        self.roomCode.setText(QCoreApplication.translate("Form", u"Code : ", None))
        self.roomName.setText(QCoreApplication.translate("Form", u"Place Holder", None))
        self.roomChatBtn.setText(QCoreApplication.translate("Form", u"Chat", None))
        self.roomCallBtn.setText(QCoreApplication.translate("Form", u"Call", None))
        self.roomWorkshopBtn.setText(QCoreApplication.translate("Form", u"Workshop", None))
        self.roomMemberBtn.setText(QCoreApplication.translate("Form", u"Members", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Chat", None))
        self.chatSendTextConfirmBtn.setText(QCoreApplication.translate("Form", u"<", None))
        self.enterOrLeaveCall.setText(QCoreApplication.translate("Form", u"Enter Call", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"WorkSpace", None))
        self.workshopRunBtn.setText(QCoreApplication.translate("Form", u"Run", None))
        self.workshopImportBtn.setText(QCoreApplication.translate("Form", u"Import", None))
        self.workshopExportBtn.setText(QCoreApplication.translate("Form", u"Export", None))
    # retranslateUi

