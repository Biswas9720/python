class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} is {self.age} years old."

person1 = Person("Alice", 25)


print(person1.name)  
print(person1.age)  


print(person1.get_info()) 
