from animal import Animal

class Cat(Animal):

    def __init__(self, name, species, size):
        super.__str__(self, species)
        self.size = size

    def __init__(self):
        return super().__str__() + f"Size: {self.size}\n"
    
    def speak(self):
        print (f"{self.name} Meow!")
