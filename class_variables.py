#Python Class-Variables -> Shared among all instances of class


class Student:
    
    class_year = 2024 #Class Variable
    num_students = 0  #Class Variable
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 
        
        
student1 = Student("Sherry", 30)
student2 = Student("Ali", 25)
student3 = Student("Ahmed", 22)
student4 = Student("Abu Bakar", 20)

# print(student1.name)
# print(student1.age)
# print(student1.class_year)
# print(student2.class_year)

# print(Student.num_students)

print(f"My Graduating Class {Student.class_year} has {Student.num_students} Students.")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

