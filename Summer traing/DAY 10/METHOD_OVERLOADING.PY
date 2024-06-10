# method overloading
class Animal:
    def speak(self):
        return "Animal makes a sound"
class Dog(Animal):
    def speak(self):
        return "WOof"
class Cat(Animal):
    def speak(self):
        return "MEow"
class Cow(Animal):
    pass
dog=Dog()
cat=Cat()
cow=Cow()
print("Animal speaks",dog.speak())
print("Animal speaks",cat.speak())
print("Animal speaks",cow.speak())