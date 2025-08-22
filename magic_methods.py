#Python Magic Methods -> Dunder Methods (Double Underscore) __init__, __str__, __eq__ 


class Book:
    
    def __init__(self, title, author, No_pages):
        
        self.title = title
        self.author = author
        self.no_pages = No_pages
        
    def __str__(self):
        
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        
        return self.no_pages < other.no_pages
    
    def __gt__(self, other):
        
        return self.no_pages > other.no_pages
    
    def __add__(self, other):
        return f"{self.no_pages + other.no_pages} pages."
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        
        if key == "title":
            return self.title
        
        if key == "author":
            return self.author
        
        elif key == "no_pages":
            return self.no_pages
        
        else:
            return f"{key} Not Found!"
        
        
book1 = Book("Atomic Habbits", "Sherry", 315)
book2 = Book("Money Hacks", "Jerry", 500)
book3 = Book("Money Model", "Tom", 149)



print(book1["audio"])
        
        
        
        
        
        
        
    