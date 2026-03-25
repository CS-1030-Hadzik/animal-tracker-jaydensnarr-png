from animal import Animal
from dog import Dog
from cat import Cat

if __name__ == "__main__":

#object of the animal class instance of the animal class/ Intanciation the class
    animal1 = Animal("Gus", "Mouse")
    animal2 = Cat("Kittens", "cat", "small")
    animal3 = Dog("Nala", "Canine", "medium")

    print(animal1)
    animal1.speak()

    print(animal2)
    animal2.speak()

    print(animal3)
    animal3.speak()

    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals
