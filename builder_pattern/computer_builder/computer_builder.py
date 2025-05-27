from builder import Builder
from computer import Computer


class ComputerBuilder(Builder):
    def __init__(self, computer_type):
        self.computer_type = computer_type

    def build_cpu(self, cpu):
        self.cpu = cpu
        print(f"{self.computer_type} CPU {self.cpu} built!")
        return self
    
    def build_ram(self, ram):
        self.ram = ram
        print(f"{self.computer_type} RAM {self.ram} built!")
        return self
    
    def build_graphic_card(self, graphics_card):
        self.graphics_card = graphics_card
        print(f"{self.computer_type} graphic card {self.graphics_card} built!")
        return self
    
    def build_storage(self, storage):
        self.storage = storage
        print(f"{self.computer_type} storage {self.storage} built!")
        return self
    
    def build_os(self, os):
        self.os = os
        print(f"{self.computer_type} OS {self.os} built!")
        return self
    
    def build(self):
        return Computer(self)