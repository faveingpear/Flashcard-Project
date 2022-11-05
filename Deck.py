import base64
from CustomDictionary import Dict
from Logger import MyLogger

class Card:

    def __init__(self, front_data:str, back_data:str, date_added:str, id:int, parent_deck, order_in_deck:int) -> None:
        
        # Add type checking
        self.front_data = front_data
        self.back_data = back_data
        self.date_added = date_added
        self.id = id
        self.parent_deck = parent_deck
        self.order_in_deck = order_in_deck

    def genKey(self) -> base64:
        #return self.front_data
        return base64.b64encode(self.front_data.encode("utf-8"))
    
    def print(self) -> str:
        return self.front_data

class Deck:

    def __init__(self, name, logger=MyLogger) -> None:

        self.logger = logger

        self.cards = Dict(name=name + " dict",logger=self.logger)
        self.name = name

        self.logger = logger

        self.logger.info("Created deck name:" + self.name)
    
    def addCard(self, inputCard:Card):
        self.cards.append(key=inputCard.genKey(), value=inputCard)
        self.logger.info("Added card " + inputCard.front_data)

    def getCard(self, index):
        self.logger.info("Retriving card " + self.cards[index].front_data)
        return self.cards[index]

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