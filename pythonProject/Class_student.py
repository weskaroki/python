class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
student1 = students("Alice",80)
student2 = students('Alex',60)
print(student1.name)
print(student1.marks)
print(student2.name)
print(student2.marks)
addition = (student2.marks +10)
print(addition)