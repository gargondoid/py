# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proccess_model.ui'
#
# Created: Thu Nov 14 12:30:01 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProccessModel(object):
    def setupUi(self, ProccessModel):
        ProccessModel.setObjectName(_fromUtf8("ProccessModel"))
        ProccessModel.setWindowModality(QtCore.Qt.NonModal)
        ProccessModel.resize(290, 320)
        ProccessModel.setMinimumSize(QtCore.QSize(290, 320))
        ProccessModel.setMaximumSize(QtCore.QSize(290, 320))
        self.gridLayoutWidget = QtGui.QWidget(ProccessModel)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 270, 158))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lblVar2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblVar2.setFont(font)
        self.lblVar2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblVar2.setObjectName(_fromUtf8("lblVar2"))
        self.gridLayout.addWidget(self.lblVar2, 3, 0, 1, 1)
        self.cmbTFForm = QtGui.QComboBox(self.gridLayoutWidget)
        self.cmbTFForm.setObjectName(_fromUtf8("cmbTFForm"))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.cmbTFForm.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cmbTFForm, 0, 1, 1, 1)
        self.lblTFForm = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTFForm.setFont(font)
        self.lblTFForm.setObjectName(_fromUtf8("lblTFForm"))
        self.gridLayout.addWidget(self.lblTFForm, 0, 0, 1, 1)
        self.leVar1 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.leVar1.setObjectName(_fromUtf8("leVar1"))
        self.gridLayout.addWidget(self.leVar1, 2, 1, 1, 1)
        self.leGain = QtGui.QLineEdit(self.gridLayoutWidget)
        self.leGain.setObjectName(_fromUtf8("leGain"))
        self.gridLayout.addWidget(self.leGain, 1, 1, 1, 1)
        self.lblVar1 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblVar1.setFont(font)
        self.lblVar1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblVar1.setObjectName(_fromUtf8("lblVar1"))
        self.gridLayout.addWidget(self.lblVar1, 2, 0, 1, 1)
        self.lblGain = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblGain.setFont(font)
        self.lblGain.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblGain.setObjectName(_fromUtf8("lblGain"))
        self.gridLayout.addWidget(self.lblGain, 1, 0, 1, 1)
        self.leVar2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.leVar2.setObjectName(_fromUtf8("leVar2"))
        self.gridLayout.addWidget(self.leVar2, 3, 1, 1, 1)
        self.lblDelay = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDelay.setFont(font)
        self.lblDelay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblDelay.setObjectName(_fromUtf8("lblDelay"))
        self.gridLayout.addWidget(self.lblDelay, 4, 0, 1, 1)
        self.lblPadeOrder = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPadeOrder.setFont(font)
        self.lblPadeOrder.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPadeOrder.setObjectName(_fromUtf8("lblPadeOrder"))
        self.gridLayout.addWidget(self.lblPadeOrder, 5, 0, 1, 1)
        self.leDelay = QtGui.QLineEdit(self.gridLayoutWidget)
        self.leDelay.setObjectName(_fromUtf8("leDelay"))
        self.gridLayout.addWidget(self.leDelay, 4, 1, 1, 1)
        self.sbPadeOrder = QtGui.QSpinBox(self.gridLayoutWidget)
        self.sbPadeOrder.setMinimum(1)
        self.sbPadeOrder.setMaximum(10)
        self.sbPadeOrder.setProperty("value", 1)
        self.sbPadeOrder.setObjectName(_fromUtf8("sbPadeOrder"))
        self.gridLayout.addWidget(self.sbPadeOrder, 5, 1, 1, 1)
        self.verticalLayoutWidget = QtGui.QWidget(ProccessModel)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 180, 271, 127))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lblTF = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTF.setFont(font)
        self.lblTF.setFrameShape(QtGui.QFrame.Box)
        self.lblTF.setFrameShadow(QtGui.QFrame.Sunken)
        self.lblTF.setText(_fromUtf8(""))
        self.lblTF.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTF.setObjectName(_fromUtf8("lblTF"))
        self.verticalLayout.addWidget(self.lblTF)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Apply|QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProccessModel)
        QtCore.QMetaObject.connectSlotsByName(ProccessModel)

    def retranslateUi(self, ProccessModel):
        ProccessModel.setWindowTitle(QtGui.QApplication.translate("ProccessModel", "Proccess Model", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVar2.setText(QtGui.QApplication.translate("ProccessModel", "lblVar2", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTFForm.setItemText(0, QtGui.QApplication.translate("ProccessModel", "Num / Den", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTFForm.setItemText(1, QtGui.QApplication.translate("ProccessModel", "Zero / Poles", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTFForm.setItemText(2, QtGui.QApplication.translate("ProccessModel", "Time Constants", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbTFForm.setItemText(3, QtGui.QApplication.translate("ProccessModel", "First Order with Delay", None, QtGui.QApplication.UnicodeUTF8))
        self.lblTFForm.setText(QtGui.QApplication.translate("ProccessModel", "Transfer Function Form", None, QtGui.QApplication.UnicodeUTF8))
        self.lblVar1.setText(QtGui.QApplication.translate("ProccessModel", "lblVar1", None, QtGui.QApplication.UnicodeUTF8))
        self.lblGain.setText(QtGui.QApplication.translate("ProccessModel", "K", None, QtGui.QApplication.UnicodeUTF8))
        self.lblDelay.setText(QtGui.QApplication.translate("ProccessModel", "Delay", None, QtGui.QApplication.UnicodeUTF8))
        self.lblPadeOrder.setText(QtGui.QApplication.translate("ProccessModel", "Pade aprox. for delay", None, QtGui.QApplication.UnicodeUTF8))

