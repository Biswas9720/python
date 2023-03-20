class Dog:
    def talk(self):
        print("Bark")


class Cat:
    def talk(self):
        print("Meow")

class Person():
    def catch(self,dog):
        dog.talk()
        print("It's running")
dog = Dog()
person = Person()

person.catch(
    dog
)




