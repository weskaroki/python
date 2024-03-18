# class Magari:
#     def __init__(self,make,model,price,year):
#         self.make = make
#         self.model = model
#         self.price = price
#         self.year = year
#     def describe(self):
#         print( f'My favourite car is {self.make}the{self.model}.{self.price}edition priced at{self.year}')
# obj1 = Magari('Ford','Ranger',20000,1999)
# obj2 = Magari('Toyota','Axis',30000,2005)
# obj3 = Magari('Mazda','Demio',40000,2015)
# print((f'My favourite car is {obj1.make}the{obj1.model}.{obj1.price}edition priced at{obj1.year}'))
# print(obj1.describe())
# print(obj2.describe())

class Person:
    def __init__(self,firstname,lastname,gender,age):
        self.firstname =firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
    def fullname(self):
        print(f"{self.firstname}{self.lastname}")
    def display_age(self):
        print(self.age)
    def display_gender(self):
        print(self.gender)
    def show_lastname(self):
        print(self.lastname)
    def increasement_age(self):
        self.age +=10
obj1 = Person('John','MUngai','male',32)
print(obj1.fullname())
print(obj1.display_age())
print(obj1.display_gender())
print(obj1.show_lastname())
obj1.increasement_age()
print(obj1.age)