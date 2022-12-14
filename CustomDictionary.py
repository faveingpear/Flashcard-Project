
from Logger import MyLogger

class entry():

    def __init__(self,key,value) -> None:
        self.key = key
        self.value = value

    def print(self):
        print("["  + str(self.key) + ":" + str(self.value) + "]")

    def to_json(self):
        return self.value
    
    #def compare(self, other:str):

    #    return self.key > other


class DuplicateEntryError(Exception):
    pass
class ObjectNotComparableError(Exception):
    pass

class EntryNotFound(Exception):
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

    def modify(self,oldKey, newKey, value):

        self.logger.info("Modifying key:" + oldKey)

        for i in range(self.size): # Loop through the length of the array
            if self.entries[i].key == oldKey: # If the key of the entry matches the oldKey
                #self.entries[i] = None
                self.entries[i] = entry(key=newKey, value=value) # Change the pointer to the new entry

    def sort(self):
        self.logger.info("Sorting dict")
        for step in range(1, len(self.entries)): # Starts looping though the array from 1 to the size
            key = self.entries[step].key
            temp = self.entries[step]
            j = step - 1

            while j>= 0 and key < self.entries[j].key: # If the current key is less than the next key, then move it over once
                self.entries[j+1] = self.entries[j]
                j = j - 1

            self.entries[j + 1] = temp
            
    def search(self, key) -> entry:
        self.logger.info("Searching for key:" + key + "d")
        for entry in self.entries: # Loop through all entries in the dictionary
            if entry.key == key: # If the key of the entry matches the inputed key
                self.logger.info("Entry found for key:" + key)
                return entry.value # Return the value
            else:
                pass # Else do nothing
        self.logger.info("Entry not found for key:" + key)
        raise EntryNotFound 
    
    def checkDuplicate(self, key) -> bool:

        for entry in self.entries:
            if entry.key == key:
                return True
        
        return False
    
    def remove(self, key) -> None:
        for i in range(len(self.entries)):
            if self.entries[i].key == key: # If the entry key matches the inputed key
                for x in range((self.size-1)-i): # Shift every entry after the key to the left one
                    self.entries[i+x] = self.entries[i+x+1]
                self.size = self.size - 1
                del self.entries[-1] # To Fix last entry persisting
                return

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