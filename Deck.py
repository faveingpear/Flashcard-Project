import base64
from CustomDictionary import Dict
from Logger import MyLogger
from JsonEncoder import MyJsonEncoder
import json

import time

class Card:

    def __init__(self, front_data:str, back_data:str, date_added:str, id:int, parent_deck, order_in_deck:int) -> None:
        
        # Add type checking
        self.front_data = front_data
        self.back_data = back_data
        self.date_added = time.time()
        self.id = id
        self.parent_deck = parent_deck
        self.order_in_deck = order_in_deck

    def genKey(self) -> base64:
        #return self.front_data
        return self.front_data
    
    def print(self) -> str:
        return self.front_data

    def to_json(self):

        card = {
            "front_data":self.front_data,
            "back_data":self.back_data,
            "data_added":self.date_added,
            "id":self.id,
            "order_in_deck":self.order_in_deck
        }

        return card

class Deck:

    def __init__(self, name, logger=MyLogger) -> None:

        self.logger = logger

        self.cards = Dict(name=name + " dict",logger=self.logger)
        self.name = name

        self.logger = logger

        self.logger.info("Created deck name:" + self.name)

    def deleteCard(self, name):

        self.cards.remove(name)
    
    def sort(self):
        self.cards.sort()
    
    def addCard(self, inputCard:Card):
        self.cards.append(key=inputCard.genKey(), value=inputCard)
        self.logger.info("Added card " + inputCard.front_data)

    def getCard(self, index):
        self.logger.info("Retriving card " + self.cards[index].front_data)
        return self.cards[index]

    def searchCard(self, name) -> Card:
        # for card in self.cards:
        #     if card.front_data == name:
        #         self.logger.info("Card with name " + name + "found")
        #         return card

        # self.logger.info("No card with name " + name)
        # self.logger.info("Current state of deck")
        # self.cards.print()
        
        return self.cards.search(name)

        # for i in range(len(self.cards)):

        #     if self.cards[i].front_data == name:
        #         self.logger.info("Card found with name " + name)
        #         return self.cards[i]
        #     else:
        #         self.logger.info("No card with name " + name + " found")
        #         return None

    def modifyCard(self, oldKey, newCard:Card):
        self.cards.modify(oldKey, newCard.genKey(), newCard)

    def print(self):
        self.cards.print()

# testDeck = Deck("Italian")
# testDeck.addCard(Card(
#     front_data="fare",
#     back_data="filler",
#     date_added="something",
#     parent_deck = testDeck,
#     order_in_deck = 1,
#     id=1
# ))

# for card in testDeck.cards:
#     print(card.front_data)

    def saveDeck(self, filelocation):

        self.logger.info(json.dumps(self, cls=MyJsonEncoder))

        #file = open(filelocation, "w")
        #file.write(json.dumps(self, cls=MyJsonEncoder))
        #file.close()

    def to_json(self):

        return {
            "name":self.name,
            "cards":self.cards
        }