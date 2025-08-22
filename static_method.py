#Python Static Method -> Belongs to class rather than any Object

# Instance Methods = Best for Operations on instances of the class (Objects)
# Static Methods = Best for Utility functions that do not need access to class 


class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cook", "Cashier", "Janitor"]
        return position in valid_positions
        
employee1 = Employee("Eugen", "Manager")
employee2 = Employee("Sherry", "Cook")
employee3 = Employee("Jerry", "Cashier")


print(Employee.is_valid_position("Cook"))
print(employee1.get_info())
        