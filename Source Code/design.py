# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '440wDesign.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(510, 312)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setMaximumSize(QtCore.QSize(350, 200))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout_2.addWidget(self.listWidget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.loadFileButton = QtGui.QPushButton(self.centralwidget)
        self.loadFileButton.setMinimumSize(QtCore.QSize(0, 35))
        self.loadFileButton.setObjectName(_fromUtf8("loadFileButton"))
        self.verticalLayout_2.addWidget(self.loadFileButton)
        self.singleReportButton = QtGui.QPushButton(self.centralwidget)
        self.singleReportButton.setMinimumSize(QtCore.QSize(0, 35))
        self.singleReportButton.setObjectName(_fromUtf8("singleReportButton"))
        self.verticalLayout_2.addWidget(self.singleReportButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(10, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.qualtricsButton = QtGui.QPushButton(self.centralwidget)
        self.qualtricsButton.setMinimumSize(QtCore.QSize(0, 35))
        self.qualtricsButton.setObjectName(_fromUtf8("qualtricsButton"))
        self.horizontalLayout.addWidget(self.qualtricsButton)
        self.allReportsButton = QtGui.QPushButton(self.centralwidget)
        self.allReportsButton.setMinimumSize(QtCore.QSize(0, 35))
        self.allReportsButton.setObjectName(_fromUtf8("allReportsButton"))
        self.horizontalLayout.addWidget(self.allReportsButton)
        self.masterReportButton = QtGui.QPushButton(self.centralwidget)
        self.masterReportButton.setMinimumSize(QtCore.QSize(0, 35))
        self.masterReportButton.setObjectName(_fromUtf8("masterReportButton"))
        self.horizontalLayout.addWidget(self.masterReportButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "College of IST LA/TA Report Generator", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">TA/LA Report Genertor</span></p></body></html>", None))
        self.loadFileButton.setText(_translate("MainWindow", "Load LA/TA List", None))
        self.singleReportButton.setText(_translate("MainWindow", "Selected LA Report", None))
        self.qualtricsButton.setText(_translate("MainWindow", "Create Qualtrics CSV", None))
        self.allReportsButton.setText(_translate("MainWindow", "All Reports", None))
        self.masterReportButton.setText(_translate("MainWindow", "Master Report", None))

