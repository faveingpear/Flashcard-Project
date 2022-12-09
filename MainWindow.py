# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from Deck import *
from CustomDictionary import *
import traceback

from FlashCardAddWidget import Ui_FlashCardAddWidget
from FLashCardWidget import Ui_FlashCardWidget
from StudySelectDiolog import Ui_StudySelectDiolog
from AddDeckWidget import Ui_AddDeckWidget
from DeckEditWidget import Ui_DeckEditWidget
from cardSearch import Ui_CardSearchWidget

from PyQt5 import QtCore, QtGui, QtWidgets

from Logger import MyLogger

FILEPATH = "decks.json"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(573, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 553, 430))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.MainVerticalLayout = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.MainVerticalLayout.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MainVerticalLayout.sizePolicy().hasHeightForWidth())
        self.MainVerticalLayout.setSizePolicy(sizePolicy)
        self.MainVerticalLayout.setObjectName("MainVerticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MainVerticalLayout)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addWidget(self.MainVerticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionBackup_all = QtWidgets.QAction(MainWindow)
        self.actionBackup_all.setObjectName("actionBackup_all")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionNew_Deck = QtWidgets.QAction(MainWindow)
        self.actionNew_Deck.setObjectName("actionNew_Deck")
        self.actionNew_Card = QtWidgets.QAction(MainWindow)
        self.actionNew_Card.setObjectName("actionNew_Card")
        self.actionEdit_deck = QtWidgets.QAction(MainWindow)
        self.actionEdit_deck.setObjectName("actionEdit_deck")
        self.actionEdit_deck.setText("Edit Deck")
        self.actionStudy = QtWidgets.QAction(MainWindow)
        self.actionStudy.setObjectName("actionStudy")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addAction(self.actionBackup_all)
        self.menuFile.addAction(self.actionExit_2)
        self.menuEdit.addAction(self.actionNew_Deck)
        self.menuEdit.addAction(self.actionNew_Card)
        self.menuEdit.addAction(self.actionEdit_deck)
        self.menuTools.addAction(self.actionStudy)
        self.menuTools.addAction(self.actionPreferences)
        self.menuTools.addAction(self.actionSearch)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.actionExit_2.triggered.connect(self.exit)

        self.actionNew_Card.triggered.connect(lambda state:self.spawnCardAdderWidget(MainWindow=MainWindow))
        self.actionNew_Deck.triggered.connect(lambda state, x=self, y=MainWindow:self.spawnAddDeckWidget(parent=x, MainWindow=y))
        self.actionEdit_deck.triggered.connect(lambda state, x=self, y=MainWindow:self.spawnDeckEditWidget(parent=x, MainWindow=y))
        self.actionSearch.triggered.connect(lambda state, x=self, y=MainWindow:self.spawnSearch(parent=x, MainWindow=y))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.logger.info("MainWindow UI setup")

    def __init__(self, decks, logger:MyLogger) -> None:
        self.decks = decks

        self.logger = logger

        self.logger.info("Initialized main window")

    def spawnSearch(self, parent, MainWindow):
        try:
            self.logger.info("Spawing searchWidget")
            self.searchWidget = QtWidgets.QWidget()
            ui = Ui_CardSearchWidget(parent=parent, MainWindow=MainWindow, logger=self.logger, decks=self.decks)
            ui.setupUi(self.searchWidget)
            self.searchWidget.show()
        except Exception as e:
            self.logger.error(traceback.format_exc())

    def exit(self):
        self.saveDecks()
        QtCore.QCoreApplication.exit()

    def saveDecks(self):

        for deck in self.decks:
            deck.sort()

        file = open(FILEPATH, "w")
        #file.write_through()
        file.write(json.dumps(self.decks, cls=MyJsonEncoder))
        file.close()
        
    def loadDecks(self, MainWindow):
        for deck in self.decks:

            Deckentry = QtWidgets.QWidget(self.MainVerticalLayout)
            Deckentry.setObjectName(deck.name)

            horizontalLayout = QtWidgets.QHBoxLayout(Deckentry)

            label = QtWidgets.QLabel(Deckentry)
            label.setText(deck.name)
            
            font = QtGui.QFont()
            font.setPointSize(20)

            label.setFont(font)

            horizontalLayout.addWidget(label)

            pushButton = QtWidgets.QPushButton(Deckentry)
            pushButton.clicked.connect(lambda state, x=deck:self.spawnStudyDialog(MainWindow=MainWindow,deck=x))
            pushButton.setText("Study")
            deleteButton = QtWidgets.QPushButton(Deckentry)
            deleteButton.clicked.connect(lambda state, x=deck:self.deleteDeck(MainWindow=MainWindow,deck=x))
            deleteButton.setText("Delete")
            horizontalLayout.addWidget(pushButton)
            horizontalLayout.addWidget(deleteButton)

            self.verticalLayout_3.addWidget(Deckentry)

            self.logger.info("Loaded deck:" + deck.name)
        
    def deleteDeck(self, MainWindow, deck):
        self.logger.info("Deleting Deck " + deck.name)
        
        for i in range(len(self.decks)):
            if self.decks[i].name == deck.name:
                del self.decks[i]
                widget = self.verticalLayout_3.takeAt(i+1)
                if widget.widget():
                    widget.widget().deleteLater()
                return


    def addDeck(self, MainWindow, deck):

        #self.decks[0].saveDeck(filelocation="")
        #self.logger.info(json.dumps(self.decks, cls=MyJsonEncoder))

        Deckentry = QtWidgets.QWidget(self.MainVerticalLayout)
        Deckentry.setObjectName(deck.name)

        horizontalLayout = QtWidgets.QHBoxLayout(Deckentry)

        label = QtWidgets.QLabel(Deckentry)
        label.setText(deck.name)
        
        font = QtGui.QFont()
        font.setPointSize(20)

        label.setFont(font)

        horizontalLayout.addWidget(label)

        pushButton = QtWidgets.QPushButton(Deckentry)
        pushButton.clicked.connect(lambda state, x=deck:self.spawnStudyDialog(MainWindow=MainWindow,deck=x))
        pushButton.setText("Study")
        deleteButton = QtWidgets.QPushButton(Deckentry)
        deleteButton.clicked.connect(lambda state, x=deck:self.deleteDeck(MainWindow=MainWindow,deck=x))
        deleteButton.setText("Delete")
        horizontalLayout.addWidget(pushButton)
        horizontalLayout.addWidget(deleteButton)

        self.verticalLayout_3.addWidget(Deckentry)

    def clearDeckUI(self):
            while self.verticalLayout_3.count():
                child = self.verticalLayout_3.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

    def spawnDeckEditWidget(self, parent, MainWindow):

        try:
            self.logger.info("Spawing EditDeckWidget")
            self.AddDeckWidget = QtWidgets.QWidget()
            ui = Ui_DeckEditWidget(parent=parent, MainWindow=MainWindow, logger=self.logger, decks=self.decks)
            ui.setupUi(self.AddDeckWidget)
            self.AddDeckWidget.show()
        except Exception as e:
            self.logger.error(traceback.format_exc())

    def spawnAddDeckWidget(self, parent, MainWindow):
        try:
            self.logger.info("Spawing AddDeckWidget")
            self.AddDeckWidget = QtWidgets.QWidget()
            ui = Ui_AddDeckWidget(parent=parent, MainWindow=MainWindow, logger=self.logger, decks=self.decks)
            ui.setupUi(self.AddDeckWidget)
            self.AddDeckWidget.show()
        except Exception as e:
            self.logger.error(traceback.format_exc())

    def spawnCardAdderWidget(self, MainWindow):
        try:
            self.logger.info("Spawing FlashCardAddWidget")
            self.AddCardDialog = QtWidgets.QWidget()
            ui = Ui_FlashCardAddWidget(parent=MainWindow, logger=self.logger, decks=self.decks)
            ui.setupUi(self.AddCardDialog)
            self.AddCardDialog.show()
        except Exception as e:
            self.logger.error(traceback.format_exc())

    def spawnStudyDialog(self, MainWindow, deck):
        try:
            self.studyDialog = QtWidgets.QWidget() # Commits studydialog to the namespace of the class so it will not be deleted
            ui = Ui_FlashCardWidget(deck=deck,parent=MainWindow, logger=self.logger)
            ui.setupUi(self.studyDialog)
            ui.loadCard()
            self.studyDialog.show()
        except Exception as e:
            self.logger.error(traceback.format_exc())
        #MainWindow.setDisabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionBackup_all.setText(_translate("MainWindow", "Backup all"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionNew_Deck.setText(_translate("MainWindow", "New Deck"))
        self.actionNew_Card.setText(_translate("MainWindow", "New Card"))
        self.actionStudy.setText(_translate("MainWindow", "Study"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))

def loadDecks(data):

    decks = []

    for deck in data:
            newDeck = Deck(name=deck['name'], logger=DeckLogger)

            for card in deck['cards']['entries']:

                
                newDeck.addCard(Card(
                    front_data=card['front_data'],
                    back_data=card['back_data'],
                    date_added=card['data_added'],
                    order_in_deck=card['order_in_deck'],
                    id=card['id'],
                    parent_deck=newDeck
                ))

            decks.append(newDeck)

    return decks

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    MainWindowLogger = MyLogger("FlashCard.log", "GUI")

    DeckLogger = MyLogger("FlashCard.log", "Deck")

    try:
        file = open(FILEPATH, "r")
        data = json.loads(file.read())
        file.close()

        decks = loadDecks(data)
    except json.decoder.JSONDecodeError:

        MainWindowLogger.error("JsonDecodingError")
        decks = []
        pass
    except FileNotFoundError:

        MainWindowLogger.error("File not found, created new file")

        file = open(FILEPATH, "x")
        file.close()

        decks = []
        pass
    except:
        MainWindowLogger.logger.error(traceback.format_exc())
        decks = []
        pass

    ui = Ui_MainWindow(decks=decks, logger=MainWindowLogger)

    ui.setupUi(MainWindow)
    ui.loadDecks(MainWindow)

    # for deck in decks:
    #     deck.print()

    MainWindow.show()
    sys.exit(app.exec_())
