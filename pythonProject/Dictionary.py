my_dictionary = {
    "Name": "Wes",
    "Gender" : "Male",
    "Age": "19",
    "Marital Status" :"Single",
}
print(my_dictionary)
print(my_dictionary["Marital Status" ])
print(my_dictionary["Name"])
print(my_dictionary.get("Gender"))
my_dictionary["Marital Status"] ="Unmarried"
print(my_dictionary)
(my_dictionary["Age"]) = 24
print(my_dictionary)
my_dictionary["Location"] ="Kisumu"
print(my_dictionary)
my_dictionary["Salary"] = "20000"
print(my_dictionary)
my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary))
print(len(my_dictionary2))
my_dictionary.pop("Marital Status")
print(my_dictionary)
my_dictionary.pop("Name")
print(my_dictionary)
del my_dictionary["Gender"]
print(my_dictionary)
my_dictionary.clear()
print(my_dictionary)
del my_dictionary
print(my_dictionary2)
car_dictionary = {
    "Name" : "Supra",
    "Company" : "Toyota",
    "Color": "Red",
    "Year of make": "2019"
}
print(car_dictionary)