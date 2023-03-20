class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

class Person:
    def __init__(self, name, age, street, city, country):
        self.name = name
        self.age = age
        self.address = Address(street, city, country)

person = Person("Biswas", 25, "27 main street", "downtown", "USA")
print(person.name)
print(person.age)
print(person.address.street)
print(person.address.city)
print(person.address.country)
