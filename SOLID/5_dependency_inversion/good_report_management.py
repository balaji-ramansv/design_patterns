from abc import ABC, abstractmethod

class Report:
    def __init__(self, data_store):
        self.data_store = data_store
    
    def generate_and_save(self, input_data):
        print(f"{input_data} cleaned...")
        print(f"{input_data} processed...")
        self.data_store.save(input_data)
        print(f"{input_data} saved to {self.data_store}...")


class DataStore(ABC):
    @abstractmethod
    def save(self, data):
        pass

class File(DataStore):
    def save(self, data):
        print(f"{data} saved into file")

class Database(DataStore):
    def save(self, data):
        print(f"{data} saved into database")

# Now, the Report class is decoupled from the specific storage mechanism.
# It only knows that it needs something that can save data, as defined by
# the DataStore interface. You can easily switch between saving to a 
# database or a file (or any other storage mechanism) without changing the
# Report class itself. This makes the system more flexible, testable, and 
# maintainable.