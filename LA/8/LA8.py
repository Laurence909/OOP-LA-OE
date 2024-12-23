#LA8
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        

book1 = Book("Ang Unggoy at ang kuneho", "Jobert")
print(f"Title: {book1.title} - Aupthor: {book1.author}")
del book1.author
print(f"Title: {book1.title} - Author: {book1.author}")

book2 = Book("How to train your dog", "Pedro")
print(f"Title: {book2.title} - Author: {book2.author}")
