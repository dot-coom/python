class Book: # BASE/PARENT CLASS
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_Book(self):
        print(f"Title: {self.title}, Author: {self.author}, Price; {self.price}")

class Fictional(Book): # SUB/CHILD CLASS 1
    def __init__(self, title, author, price, genre):
        super().__init__(title, author, price)
        self.genre = genre

    def disp_Fict(self): # FUNCTION OF CURRENT SUB CLASS
        super().display_Book()
        print(f"Genre: {self.genre}")

class Non_Fictional(Book): # SUB/CHILD CLASS 2
    def __init__(self, title, author, price, subject):
        super().__init__(title, author, price)
        self.subject = subject

    def disp_Non_Fict(self): # FUNCTION OF CURRENT SUB CLASS
        super().display_Book()
        print(f"Subject: {self.subject}")

b1 = Book("ABC", "abc", 120) # BASE/PARENT CLASS OBJECT [MAIN CLASS]
fb1 = Fictional("ABC", "abc", 130, "Thriller") # CHILD/SUB CLASS OBJECT [SUB CLASS 1]
nfb1 = Non_Fictional("DEF", "def", 120, "Horror") # CHILD/SUB CLASS OBJECT [SUB CLASS 2]
fb1.disp_Fict() # CALLING FUNCTION WITH SUB CLASS OBJECT 1
nfb1.disp_Non_Fict() # CALLING FUNCTION WITH SUB CLASS OBJECT 2
