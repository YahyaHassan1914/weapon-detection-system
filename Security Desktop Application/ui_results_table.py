# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_results_table.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 400)
        Form.setStyleSheet(u"/* Table Widget */\n"
"    QTableWidget {\n"
"        background-color: #3d3d3d;\n"
"        color: #f0f0f0;\n"
"        border: 1px solid #4d4d4d;\n"
"        border-radius: 8px;\n"
"        font-size: 16px;\n"
"        padding: 10px;\n"
"    }\n"
"\n"
"    QTableWidget::item {\n"
"        border: 1px solid #4d4d4d;\n"
"    }\n"
"\n"
"    QHeaderView::section {\n"
"        background-color: #4d4d4d;\n"
"        color: #f0f0f0;\n"
"        border: 1px solid #4d4d4d;\n"
"        padding: 10px;\n"
"    }\n"
"\n"
"    QTableWidget::item:selected {\n"
"        background-color: #666666;\n"
"        color: #f0f0f0;\n"
"        border: none; /* Remove border on selected item */\n"
"    }\n"
"\n"
"    /* Row Headers */\n"
"    QHeaderView::section:vertical {\n"
"        background-color: #4d4d4d;\n"
"        color: #f0f0f0;\n"
"        padding: 5px;\n"
"        border: 1px solid #4d4d4d;\n"
"    }\n"
"\n"
"    QTableCornerButton::section {\n"
"        background-color: #4d4d4d;\n"
"        "
                        "border: 1px solid #4d4d4d;\n"
"    }\n"
"\n"
"    /* Ensure the area without numbers is styled */\n"
"    QHeaderView::section {\n"
"        background-color: #4d4d4d;\n"
"        color: #f0f0f0;\n"
"        padding: 5px;\n"
"        border: 1px solid #4d4d4d;\n"
"    }")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.results_table = QTableWidget(Form)
        if (self.results_table.columnCount() < 2):
            self.results_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.results_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.results_table.setObjectName(u"results_table")
        self.results_table.setAlternatingRowColors(False)
        self.results_table.horizontalHeader().setVisible(True)
        self.results_table.horizontalHeader().setHighlightSections(True)
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.results_table)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.results_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Class Name", None));
        ___qtablewidgetitem1 = self.results_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Detection Number", None));
    # retranslateUi

