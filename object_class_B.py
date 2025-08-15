class Car:
    def __init__(self, model, year, color, for_Sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_Sale
        
    def drive(self):
        print(f"You Drive the {self.color} {self.model} Car!.")
        
    def stop(self):
        print(f"You Stop the {self.color} {self.model} Car!.")
        
    def describe(self):
        print(f"{self.model} {self.color} {self.year}")