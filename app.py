from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self.__name

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

def animal_speak(animal):
    print(f"{animal.get_name()} says {animal.make_sound()}")

dog = Dog("Buddy")
cat = Cat("Whiskers")

animal_speak(dog)
animal_speak(cat)
