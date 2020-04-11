class NamedPrinter:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.name = f'{first_name} {last_name}' 

    def print_msg(self, msg):
        print(f"{self.name}: {msg}")

    def print_name(self):
        msg = f"My name is {self.last_name}, {self.name}."
        self.print_msg(msg)

