from animal import Animal

class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """

    # kingdom
    # name species
    # speak()
    # __str___

    def __init__(self, name, species, size):
        super().__init__(self, species)
        self.size = size

    def __init__(self):
        return super().__str__() + f"Size: {self.size}\n"
    
    def speak(self):
        print (f"{self.name} woofs!")
    
    
    # TODO: Override the __str__ method to include the breed.
    # Example output:
    # Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute', Breed: 'breed attribute'
    
    # TODO: Add a method for the dog to make a specific sound. 
    # Call the method `speak` and make it output a specific message like 
    # "The dog barks.