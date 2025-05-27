class Computer:
    def __init__(self, config):
        self.cpu = config.cpu
        self.ram = config.ram
        self.storage = config.storage
        self.graphics_card = config.graphics_card
        self.os = config.os

    def __str__(self):
        return "\n".join([f"{k}: {v}" for k, v in vars(self).items()])
    