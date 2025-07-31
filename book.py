class Book:
    def __init__(self,title,author,P_year):
        self.title = title
        self.author = author
        self.P_year = P_year

    def BookInfo(self):
        print(f"The Book {self.title} written by {self.author} on {self.P_year}")
        
class FictionBook(Book):
    def __init__(self, title, author, P_year,genre):
        super().__init__(title, author, P_year)
        self.genre = genre

    def dis_genre(self):
        super().BookInfo()
        print(f"Genre of the book is {self.genre}")

class NonFicBook(Book):
    def __init__(self, title, author, P_year,subject):
        super().__init__(title, author, P_year)     
        self.subject = subject

    def dis_sub(self):
        super().BookInfo()
        print(f"The subject is {self.subject}")   


b1 = FictionBook("ABC","NJAANA",2020,"Novel")
b1.dis_genre()

b2 = NonFicBook("CBA","AAROO",2020,"Short Story")
b2.dis_sub()