# class Employees:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary =salary
# class Receptionist(Employees):
#     def __init__(self,name,salary,gender):
#         super().__init__(name,salary)
#         self.gender = gender
# obj1 = Receptionist('Jane' ,20000,'female')
# obj1 = Employees('Felix',50,000)
# print(Receptionist.name)
# print(Employees.name)

class Frontend_developers:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class programmer(Frontend_developers):
    def __init__(self,name,age,experience,salary):
        super().__init__(name,age)
        self.experience = experience
        self.salary = salary
person2 = programmer('Jack',29,'5years',25000)
person1 = Frontend_developers('Grace',25)
print(person1.age)
print(person2.name)
print(person2.experience)


