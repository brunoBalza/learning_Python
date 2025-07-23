class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow (self):
        if self.available : 
            self.available = False
            print(f'El libro {self.title} ha sido prestado')
        else:
            print('Este libro está prestado')

    def return_book (self):
        self.available = True
        print(f'El libro {self.title} ha sido devuelto')

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book (self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'El libro {book.title} no esta disponible')
    
    def return_book (self, book):
        if book in self.borrowed_books:
            book.return_book()        
            self.borrowed_books.remove(book)
        else:
            print(f'El libro {book.title} no está en la lista de prestados')

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book (self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agragado')

    def register_user(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido agregado')

    def show_available_books(self):
        print(f'Los libros disponibles:')
        for book in self.books:
            if book.available:
                print(f'{book.title} por {book.author}')




#Creando libros

book1 = Book('Book 1', 'Author 1')
book2 = Book('Book 2', 'Author 2')
book3 = Book('Book 3', 'Author 3')

# Creando usuarios

user1 = User('User 1', '123')
user2 = User('User 2', '124')
user3 = User('User 3', '125')

# Creando la Libreria

Libreria = Library()
Libreria.add_book(book1)
Libreria.add_book(book2)
Libreria.add_book(book3)
Libreria.register_user(user1)
Libreria.register_user(user2)
Libreria.register_user(user3)

# Mostrar libros

Libreria.show_available_books()

# Prestamos un libro

user1.borrow_book(book1)
Libreria.show_available_books()

# Devolver Libro

user1.return_book(book1)
Libreria.show_available_books()