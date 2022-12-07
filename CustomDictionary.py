
from Logger import MyLogger
class entry():

    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value

    def print(self):
        print("["  + str(self.key) + ":" + str(self.value) + "]")

    def to_json(self):

        # jsonData = {
        #     "key": self.key,
        #     "value": self.value
        # }

        return self.value

class DuplicateEntryError(Exception):
    pass
class Dict():

    #entries:entry = [] #DO NOT MAKE THIS A CLASS VARIABLE

    def __init__(self,name, logger:MyLogger) -> None:

        self.entries = []
        self.logger = logger
        self.logger.info("[" + name + "] Initialized Dictionary")
        self.name = name
        self.size = 0
        pass

    def append(self, key, value):

        if self.checkDuplicate(key):
            self.logger.error("[" + self.name + "] Cannot Add entry " + key + " because it is already in the dict")
            raise DuplicateEntryError
        else:

            newEntry = entry(key=key,value=value)
            self.entries.append(newEntry)

            self.logger.info("[" + self.name + "] Added entry with key:" + str(key) + " and value:" + str(value))

            self.size = self.size + 1

    def modify(self, key, value):
        for i in range(self.size):
            if self.entries[i].key == key:
                self.entries[i] = entry(key=key, value=value)
                
    def search(self, key) -> entry:
        for entry in self.entries:
            if entry.key == key:
                return entry.value
            else:
                pass

    def checkDuplicate(self, key) -> bool:

        for entry in self.entries:
            if entry.key == key:
                return True
        
        return False
    
    def remove(self, key) -> None:
        for i in range(len(self.entries)):
            if self.entries[i].key == key:
                self.entries.pop(i)
                self.size = self.size - 1

    def getLength(self):
        return len(self.entries)

    def print(self):
        for entry in self.entries:
            entry.print()

    def __getitem__(self, item):
        try:
            self.logger.info("[" + self.name + "] __getitem__ called with value: " + str(item) + " returning "  + str(self.entries[item].value))
            return self.entries[item].value
        except IndexError:
            self.logger.error("[" + self.name + "] __getitem__ called with value: " + str(item) + " but there is no entry")
            return None

    def __len__(self):
        return self.size

    def to_json(self):
        return {
            "entries":self.entries
        }