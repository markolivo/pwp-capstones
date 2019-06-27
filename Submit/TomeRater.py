class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{}'s email has been updated.".format(self.name))

    def __repr__(self):
        return "User: {name}, email: {email}, books read: {read}".format(name = self.name, email = self.email, read = len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
        
    def read_book(self, book, rating=None):
        self.books[book] = rating
        
    def get_average_rating(self):
        if len(self.books) != 0:
            sum_rating = 0.0
            count_rating = 0
            for b in self.books:
                if self.books[b] != None:
                    count_rating += 1
                    sum_rating += self.books[b]
            return sum_rating / count_rating
            
class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title
        
    def get_isbn(self):
        return self.isbn
        
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{}'s isbn has been changed.".format(self.title))
        
    def add_rating(self, rating):
        if rating >= 0 or rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating!")
            
    def __repr__(self):
        return "Librong titled '{}'".format(self.title)
            
    def __eq__(self, book):
        return self.title == book.title and self.isbn == book.isbn
        
    def __hash__(self):
        return hash((self.title, self.isbn))
        
    def get_average_rating(self):
        if len(self.ratings) != 0:
            return sum(self.ratings) / len(self.ratings)
        
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self, author):
        return self.author
        
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
        
    def get_level(self):
        return self.level
        
    def __repr__(self):
        return "{title} a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
        
class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}
        
    def create_book(self, title, isbn):
        return Book(title, isbn)
    
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
        
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
        
    def add_book_to_user(self, book, email, rating=None):
        try:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if self.books.get(book, 0) == 0:
                self.books[book] = 1
            else:
                self.books[book] += 1
        except KeyError:
            print("No user with email {}!".format(email))
            
    def add_user(self, name, email, user_books=None):
        self.users[email] = User(name, email)
        if user_books != None:
            for b in user_books:
                self.add_book_to_user(b, email)

    def print_catalog(self):
        for b in self.books:
            print(b)
            
    def print_users(self):
        for u in self.users:
            print(u)
            
    def most_read_book(self):
        mx = 0
        for b in self.books:
            if self.books[b] > mx:
                mrb = b
                mx = self.books[b]
        return mrb

    def highest_rated_book(self):
        mx = 0
        for b in self.books:
            if b.get_average_rating() > mx:
                hrb = b
                mx = self.books[b]
        return hrb
        
    def most_positive_user(self):
        mx = 0
        for u in self.users.values():
            if u.get_average_rating() > mx:
                mpu = u
                mx = self.books[b]
        return mpu

