# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\AddDeckWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import traceback
from typing import List
from PyQt5 import QtCore, QtGui, QtWidgets
from Deck import Deck

from Logger import MyLogger


class Ui_AddDeckWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(277, 86)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.nameInput = QtWidgets.QLineEdit(Form)
        self.nameInput.setGeometry(QtCore.QRect(140, 20, 113, 20))
        self.nameInput.setObjectName("nameInput")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(180, 50, 75, 23))
        self.addButton.setObjectName("addButton")
        self.addButton.clicked.connect(lambda state:self.addDeck())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def __init__(self, parent, MainWindow, logger:MyLogger, decks:List[Deck]) -> None:
        self.parent = parent
        self.logger = logger
        self.decks = decks
        self.MainWindow = MainWindow

    def addDeck(self):

        try:
            deckName = self.nameInput.text()

            for deck in self.decks:
                if deck.name == deckName:
                    self.logger.error("Duplicate error")
                    return
                
            if deckName == "":
                self.logger.error("Cannot add deck with no name")
            else:
                self.logger.info("Adding deck " + deckName)


                newDeck = Deck(deckName, self.logger)
                self.decks.append(newDeck) #Fix logger?

                #self.parent.clearDeckUI()
                self.parent.addDeck(self.MainWindow, newDeck)

        except Exception as e:
            self.logger.error(traceback.format_exc())

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Deck Name:"))
        self.addButton.setText(_translate("Form", "Add"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_AddDeckWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
