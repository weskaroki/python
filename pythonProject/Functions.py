# print('This is my first function')
# print('This is my first function')
# print('This is my first function')
#
# def Karibu():
#     print('THis my first function')
#     print('This my first function')
#     print('This is my first function')
# Karibu()
# Karibu()
# def myfunction(name):
#     print(name)
#     print(name)
#     print(name)
# myfunction('John')
# myfunction('Ann')
# myfunction('Peter')
#
# def num(nambari):
#     print(nambari)
#     print(nambari)
# num(56)
#
# def salutation(first_name):
#     print('Hi '+ first_name+ " Good Morning")
# salutation('Esther')
#
# def miaka(age):
#     print('Hello,you are' + str(age) +'Years old')
# miaka(18)
# def my_name(first_name,last_name,age):
#            print(first_name+ last_name + "is the student")
# my_name('joe','west',19)
#
# def employees(name,age):
#     if age>=15:
#         print(name + 'you are' + str(age) +'years old')
#     elif age<20 and age>=15:
#         print(name + 'you are' +str(age) + 'yeqars old')
#     elif age<15 and age>10:
#         print(name + "you are" +str(age) +'years old')
#     else:
#         print('You are not yet born')
# employees('Mbuthia',23)
# employees('Otieno',9)
#
# def age_calculator(age):
#     new_age =age + 10
#     return new_age
# print(age_calculator(18))
#
# def marks_calculators(*subjects):
#     total_marks = sum(subjects)
#     return total_marks
# print(marks_calculators(23,45,67))
# print(marks_calculators(2,56,68,90))
# print(marks_calculators(34,56))

def items_bought(item,no,price):
    total = int((no*price))
    return total
print(items_bought(' sugar packects',3,150))
print(items_bought('flour',2,100))

def residentials(Location,age):
    if age >60:
        print('You will be posted to Kisumu')
    elif age >=50 and age <=60:
        print('You will be posted to Nakuru')
    elif age >=30 and age <=40:
        print('You will be posted to Mombasa')
    else:
        print("You will be posted to Nairobi")
print(residentials('Kisumu',50))
print(residentials('Westlands',30))
def country (nchi = "kenya"):
    return nchi
print(country("Kenya"))
print(country('Uganda'))
print(country("Russia"))










