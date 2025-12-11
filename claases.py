class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    def greeting(self):
            return f'Hello {self.first_name}!'

p = Person('Turki')
print(p.greeting())

class Car:
    def start(self):
        return "Car is running"

class Animal:
    def sound(self):
        return "animal noise"

class Dog(Animal):
    pass
dog = Dog()
print(dog.sound())


class cat:
    def sound(self):
        return "Meow!"

class Horse:
    def sound(self):
        return "neighing"


for i in [cat(), Horse()]:
    print(i.sound())