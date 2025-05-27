class Database:
    def save(self, data):
        print(f"{data} saved into database.")

class Report:
    def __init__(self):
        self.database = Database()
    
    def generate_and_save(self, input_data):
        print(f"{input_data} cleaned...")
        print(f"{input_data} processed...")
        self.database.save(input_data)
        print(f"{input_data} saved to {self.database}...")

# There is a big problem with the Report class
# The Report class can only save to database
# In case, we want to save to a file rather than a database,
# we have to modify the constructor to receive a file input.
# Then we have to create a new method or modify the "generate_and_save" 
# method to work with files instead of database.
# Clearly this is not robust and this is forcing us to modify - 
# i.e. forcing us to violate "open for extension; closed for modification"
# principle.