#Python Class Methods -> Allow Opertions related to class itself
#                        Take (cls) as the first parameter, which represents the class itself

class Student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
        
    #INSTANCE    
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total No Of Students: {cls.count}"
    
    @classmethod
    def get_average(cls):
        if cls.count == 0:
            return 0
        
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f} "
    
    
student1 = Student("Sherry", 3.22)
student2 = Student("Jerry", 3.0)

# print(student1.get_info())    
# print(student2.get_info())    

print(Student.get_count())
print(Student.get_average())
    