class Journal:
    def __init__(self):
        self.entries = []
    
    def add_an_entry(self, entry):
        self.entries.append(entry)

    def delete_an_entry(self, entry_index):
        del self.entries[entry_index]
    
    def save_journal_to_file(self, filename):
        """This method adds one more responsibility of persistance. Must be avoided."""
        pass

    def load_journal_from_file(self, filename):
        """This method adds one more responsibility of persistance. Must be avoided."""
        pass
    
    def __str__(self):
        journal = ""
        for index, text in enumerate(self.entries):
            journal += f"{index}. {text}\n"
        return journal

j = Journal()
print("Adding entries")
j.add_an_entry("Journal is for recording our intimate thoughts")
j.add_an_entry("I have to keep my journal private")
j.add_an_entry("It could get very personal")

print("Printing journal")
print(j)

print("Deleting the last entry")
j.delete_an_entry(-1)

print("Printing journal")
print(j)