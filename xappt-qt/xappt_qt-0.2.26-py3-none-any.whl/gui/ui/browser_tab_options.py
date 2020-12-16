# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser_tab_options.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tabOptions(object):
    def setupUi(self, tabOptions):
        tabOptions.setObjectName("tabOptions")
        tabOptions.resize(263, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(tabOptions)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(6, 6, 6, 6)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chkLaunchNewProcess = QtWidgets.QCheckBox(tabOptions)
        self.chkLaunchNewProcess.setObjectName("chkLaunchNewProcess")
        self.gridLayout_3.addWidget(self.chkLaunchNewProcess, 0, 0, 1, 1)
        self.chkMinimizeToTray = QtWidgets.QCheckBox(tabOptions)
        self.chkMinimizeToTray.setObjectName("chkMinimizeToTray")
        self.gridLayout_3.addWidget(self.chkMinimizeToTray, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 237, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(tabOptions)
        QtCore.QMetaObject.connectSlotsByName(tabOptions)

    def retranslateUi(self, tabOptions):
        _translate = QtCore.QCoreApplication.translate
        tabOptions.setWindowTitle(_translate("tabOptions", "Options"))
        self.chkLaunchNewProcess.setText(_translate("tabOptions", "Launch tools in new process"))
        self.chkMinimizeToTray.setText(_translate("tabOptions", "Minimize to system tray"))
