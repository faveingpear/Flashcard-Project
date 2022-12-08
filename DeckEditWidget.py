# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\DeckEditWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from CustomDictionary import DuplicateEntryError
from Deck import *

import time

class Ui_DeckEditWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(444, 316)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.deckComboBox = QtWidgets.QComboBox(Form)
        self.deckComboBox.setGeometry(QtCore.QRect(150, 20, 151, 22))
        self.deckComboBox.setObjectName("deckComboBox")
        self.cardListView = QtWidgets.QListWidget(Form)
        self.cardListView.setGeometry(QtCore.QRect(10, 50, 191, 251))
        self.cardListView.setObjectName("cardListView")
        self.topTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.topTextEdit.setGeometry(QtCore.QRect(210, 50, 220, 121))
        self.topTextEdit.setObjectName("topTextEdit")
        self.bottomTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.bottomTextEdit.setGeometry(QtCore.QRect(210, 180, 220, 121))
        self.bottomTextEdit.setObjectName("bottomTextEdit")
        self.addButton = QtWidgets.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(360, 20, 75, 23))
        self.addButton.setObjectName("addButton")
        self.removeButton = QtWidgets.QPushButton(Form)
        self.removeButton.setGeometry(QtCore.QRect(360-50, 20, 75, 23))
        self.removeButton.setObjectName("removeButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.fillComboBox()

        self.fillListView()

        self.deckComboBox.currentTextChanged.connect(lambda state:self.fillListView())
        self.cardListView.itemClicked.connect(lambda item:self.fillCardWidgets(item=item))
        self.addButton.clicked.connect(lambda state:self.saveCard())
        self.removeButton.clicked.connect(lambda state:self.deleteCard())


    def __init__(self, parent, MainWindow, logger, decks):
        self.parent = parent
        self.MainWindow = MainWindow
        self.logger = logger
        self.decks = decks

        #self.widgets = [] # For keeping tack of the list view entries. 
        # Not needed since cardListView.clear does the same thing

    def deleteCard(self):
        self.decks[self.deckComboBox.currentIndex()].deleteCard(self.selectedCard.genKey())
        self.fillListView()

    def saveCard(self):

        #self.selectedCard.front_data = self.topTextEdit.toPlainText()
        #self.selectedCard.bottom_data = self.bottomTextEdit.toPlainText()

        #self.fillListView()

        #self.decks[self.deckComboBox.currentIndex()].deleteCard(self.selectedCard.front_data)

        newCard = Card(
            front_data=self.topTextEdit.toPlainText(),
            back_data=self.bottomTextEdit.toPlainText(),
            date_added=time.time(),
            id=1,
            parent_deck=self.decks[self.deckComboBox.currentIndex()],
            order_in_deck=len(self.decks[self.deckComboBox.currentIndex()].cards)+1
        )

        #self.decks[self.deckComboBox.currentIndex()].addCard(newCard)

        self.decks[self.deckComboBox.currentIndex()].print()

        self.logger.info("Modiying card: oldkey=" + self.selectedCard.genKey() + " newcard =" + newCard.genKey())

        self.decks[self.deckComboBox.currentIndex()].modifyCard(self.selectedCard.genKey(), newCard)

        self.selectedCard = newCard

        self.fillListView()
        #self.fillCardWidgets()

    def fillComboBox(self):

        for deck in self.decks:
            self.deckComboBox.addItem(deck.name)

    def fillListView(self):

        self.cardListView.clear()

        for i in range(len(self.decks[self.deckComboBox.currentIndex()].cards)):
            newWidget = QtWidgets.QListWidgetItem()

            newWidget.setText(self.decks[self.deckComboBox.currentIndex()].cards[i].front_data)

            self.cardListView.addItem(newWidget)


        #selected = self.cardListView.itemClicked.connect(lambda)
        #print(selected)


        # for card in self.decks[self.deckComboBox.currentIndex()].cards:

        #     newWidget = QtWidgets.QListWidgetItem()

        #     newWidget.setText(card.front_data)

        #     self.cardListView.addItem(newWidget)
        #     pass

    def fillCardWidgets(self, item):
        cardName = item.text()
        self.logger.info("Clicked item: " + item.text())
        card = self.decks[self.deckComboBox.currentIndex()].searchCard(cardName)
        
        self.topTextEdit.setPlainText(card.front_data)
        self.bottomTextEdit.setPlainText(card.back_data)

        self.selectedCard = card

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Choose a Deck:"))
        self.addButton.setText(_translate("Form", "Save"))
        self.removeButton.setText(_translate("Form", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_DeckEditWidget()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
