# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui1_7.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)
# import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"/* Main window background */\n"
"        QMainWindow {\n"
"            background-color: #2e2e2e;\n"
"        }\n"
"\n"
"        /* Labels */\n"
"        QLabel {\n"
"            font-size: 20px;\n"
"            font-weight: bold;\n"
"            color: #f0f0f0;\n"
"            padding: 10px;\n"
"        }\n"
"\n"
"        /* Push buttons */\n"
"        QPushButton {\n"
"            background-color: #4d4d4d;\n"
"            color: #f0f0f0;\n"
"            border: 1px solid #4d4d4d;\n"
"            padding: 10px 20px;\n"
"            text-align: center;\n"
"            text-decoration: none;\n"
"            display: inline-block;\n"
"            font-size: 16px;\n"
"            margin: 4px 2px;\n"
"            transition-duration: 0.4s;\n"
"            cursor: pointer;\n"
"            border-radius: 8px;\n"
"        }\n"
"\n"
"        QPushButton:hover {\n"
"            background-color: #666666;\n"
"            border: 1px solid #f0f0f0;\n"
"        }\n"
"\n"
"        QPushButton:pressed {\n"
"            bac"
                        "kground-color: #333333;\n"
"            border: 1px solid #f0f0f0;\n"
"        }\n"
"\n"
"        /* Tool buttons */\n"
"        QToolButton {\n"
"            background-color: #4d4d4d;\n"
"            color: #f0f0f0;\n"
"            border: 1px solid #4d4d4d;\n"
"            padding: 10px 20px;\n"
"            text-align: center;\n"
"            text-decoration: none;\n"
"            display: inline-block;\n"
"            font-size: 16px;\n"
"            margin: 4px 2px;\n"
"            transition-duration: 0.4s;\n"
"            cursor: pointer;\n"
"            border-radius: 8px;\n"
"        }\n"
"\n"
"        QToolButton:hover {\n"
"            background-color: #666666;\n"
"            border: 1px solid #f0f0f0;\n"
"        }\n"
"\n"
"        QToolButton:pressed {\n"
"            background-color: #333333;\n"
"            border: 1px solid #f0f0f0;\n"
"        }\n"
"\n"
"        /* Combo boxes */\n"
"        QComboBox {\n"
"            background-color: #3d3d3d;\n"
"            color: #f0f0f0;\n"
"        "
                        "    border: 1px solid #4d4d4d;\n"
"            border-radius: 8px;\n"
"            padding: 10px;\n"
"            font-size: 16px;\n"
"        }\n"
"\n"
"        QComboBox::drop-down {\n"
"            subcontrol-origin: padding;\n"
"            subcontrol-position: top right;\n"
"            width: 20px;\n"
"            border-left-width: 1px;\n"
"            border-left-color: #4d4d4d;\n"
"            border-left-style: solid;\n"
"            border-top-right-radius: 8px;\n"
"            border-bottom-right-radius: 8px;\n"
"        }\n"
"\n"
"        QComboBox QAbstractItemView {\n"
"            background-color: #4d4d4d;\n"
"            color: #f0f0f0;\n"
"            border: 1px solid #4d4d4d;\n"
"            selection-background-color: #666666;\n"
"            selection-color: #f0f0f0;\n"
"        }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_display = QFrame(self.centralwidget)
        self.frame_display.setObjectName(u"frame_display")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_display.sizePolicy().hasHeightForWidth())
        self.frame_display.setSizePolicy(sizePolicy)
        self.frame_display.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_display.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_display)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_display = QLabel(self.frame_display)
        self.label_display.setObjectName(u"label_display")
        self.label_display.setMinimumSize(QSize(1024, 567))
        self.label_display.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.label_display)

        self.verticalLayout.setStretch(0, 9)

        self.horizontalLayout.addWidget(self.frame_display)

        self.frame_controls = QFrame(self.centralwidget)
        self.frame_controls.setObjectName(u"frame_controls")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_controls.sizePolicy().hasHeightForWidth())
        self.frame_controls.setSizePolicy(sizePolicy1)
        self.frame_controls.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_controls.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_controls)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_arrows = QFrame(self.frame_controls)
        self.frame_arrows.setObjectName(u"frame_arrows")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.frame_arrows.sizePolicy().hasHeightForWidth())
        self.frame_arrows.setSizePolicy(sizePolicy2)
        self.frame_arrows.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_arrows.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_arrows)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolButton_right_arrow = QToolButton(self.frame_arrows)
        self.toolButton_right_arrow.setObjectName(u"toolButton_right_arrow")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_right_arrow.sizePolicy().hasHeightForWidth())
        self.toolButton_right_arrow.setSizePolicy(sizePolicy3)
        self.toolButton_right_arrow.setArrowType(Qt.ArrowType.RightArrow)

        self.gridLayout.addWidget(self.toolButton_right_arrow, 1, 3, 1, 1)

        self.toolButton_left_arrow = QToolButton(self.frame_arrows)
        self.toolButton_left_arrow.setObjectName(u"toolButton_left_arrow")
        sizePolicy3.setHeightForWidth(self.toolButton_left_arrow.sizePolicy().hasHeightForWidth())
        self.toolButton_left_arrow.setSizePolicy(sizePolicy3)
        self.toolButton_left_arrow.setArrowType(Qt.ArrowType.LeftArrow)

        self.gridLayout.addWidget(self.toolButton_left_arrow, 1, 0, 1, 1)

        self.toolButton_up_arrow = QToolButton(self.frame_arrows)
        self.toolButton_up_arrow.setObjectName(u"toolButton_up_arrow")
        sizePolicy3.setHeightForWidth(self.toolButton_up_arrow.sizePolicy().hasHeightForWidth())
        self.toolButton_up_arrow.setSizePolicy(sizePolicy3)
        self.toolButton_up_arrow.setArrowType(Qt.ArrowType.UpArrow)

        self.gridLayout.addWidget(self.toolButton_up_arrow, 0, 2, 1, 1)

        self.toolButton_center = QToolButton(self.frame_arrows)
        self.toolButton_center.setObjectName(u"toolButton_center")
        sizePolicy3.setHeightForWidth(self.toolButton_center.sizePolicy().hasHeightForWidth())
        self.toolButton_center.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.toolButton_center, 1, 2, 1, 1)

        self.toolButton_down_arrow = QToolButton(self.frame_arrows)
        self.toolButton_down_arrow.setObjectName(u"toolButton_down_arrow")
        sizePolicy3.setHeightForWidth(self.toolButton_down_arrow.sizePolicy().hasHeightForWidth())
        self.toolButton_down_arrow.setSizePolicy(sizePolicy3)
        self.toolButton_down_arrow.setArrowType(Qt.ArrowType.DownArrow)

        self.gridLayout.addWidget(self.toolButton_down_arrow, 2, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_arrows)

        self.frame_description = QFrame(self.frame_controls)
        self.frame_description.setObjectName(u"frame_description")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(7)
        sizePolicy4.setHeightForWidth(self.frame_description.sizePolicy().hasHeightForWidth())
        self.frame_description.setSizePolicy(sizePolicy4)
        self.frame_description.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_description.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_description)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_browse_media = QPushButton(self.frame_description)
        self.pushButton_browse_media.setObjectName(u"pushButton_browse_media")

        self.verticalLayout_4.addWidget(self.pushButton_browse_media)

        self.pushButton_webcam = QPushButton(self.frame_description)
        self.pushButton_webcam.setObjectName(u"pushButton_webcam")

        self.verticalLayout_4.addWidget(self.pushButton_webcam)

        self.label = QLabel(self.frame_description)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.comboBox_cameras = QComboBox(self.frame_description)
        self.comboBox_cameras.addItem("")
        self.comboBox_cameras.setObjectName(u"comboBox_cameras")

        self.verticalLayout_4.addWidget(self.comboBox_cameras)

        self.pushButton_play = QPushButton(self.frame_description)
        self.pushButton_play.setObjectName(u"pushButton_play")
        font = QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_play.setFont(font)
        self.pushButton_play.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.pushButton_play)

        self.pushButton_stop = QPushButton(self.frame_description)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setFont(font)
        self.pushButton_stop.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.pushButton_stop)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.label_targets_guns = QLabel(self.frame_description)
        self.label_targets_guns.setObjectName(u"label_targets_guns")

        self.verticalLayout_4.addWidget(self.label_targets_guns)

        self.label_targets_individual = QLabel(self.frame_description)
        self.label_targets_individual.setObjectName(u"label_targets_individual")

        self.verticalLayout_4.addWidget(self.label_targets_individual)

        self.pushButton_results = QPushButton(self.frame_description)
        self.pushButton_results.setObjectName(u"pushButton_results")

        self.verticalLayout_4.addWidget(self.pushButton_results)

        self.verticalLayout_4.setStretch(0, 1)

        self.verticalLayout_2.addWidget(self.frame_description)


        self.horizontalLayout.addWidget(self.frame_controls)

        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_display.setText("")
        self.toolButton_right_arrow.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_left_arrow.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_up_arrow.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_center.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.toolButton_down_arrow.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_browse_media.setText(QCoreApplication.translate("MainWindow", u"Browse Media", None))
        self.pushButton_webcam.setText(QCoreApplication.translate("MainWindow", u"Web Camera", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CCTV Cameras", None))
        self.comboBox_cameras.setItemText(0, QCoreApplication.translate("MainWindow", u"Choose Camera", None))

        self.pushButton_play.setText(QCoreApplication.translate("MainWindow", u"Start Detection", None))
        self.pushButton_stop.setText(QCoreApplication.translate("MainWindow", u"Stop Detection", None))
        self.label_targets_guns.setText(QCoreApplication.translate("MainWindow", u"Guns : 0", None))
        self.label_targets_individual.setText(QCoreApplication.translate("MainWindow", u"Individual : 0", None))
        self.pushButton_results.setText(QCoreApplication.translate("MainWindow", u"Results", None))
    # retranslateUi

