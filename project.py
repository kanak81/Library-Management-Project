class Library:
    def __init__(self):
        self.books = {}
        self.users = {}

    def add_book(self, book_id, title, author):
        if book_id not in self.books:
            self.books[book_id] = {'title': title, 'author': author, 'available': True}
            print(f'Book added: {title} by {author}')
        else:
            print('Book with the same ID already exists.')

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print('Book removed.')
        else:
            print('Book not found.')

    def display_books(self):
        if not self.books:
            print('No books in the library.')
        else:
            print('Books in the library:')
            for book_id, book_info in self.books.items():
                print(f'{book_id}: {book_info["title"]} by {book_info["author"]} - {"Available" if book_info["available"] else "Checked Out"}')

    def register_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = {'name': name, 'checked_out_books': []}
            print(f'User registered: {name}')
        else:
            print('User with the same ID already exists.')

    def check_out_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            if self.books[book_id]['available']:
                self.users[user_id]['checked_out_books'].append(book_id)
                self.books[book_id]['available'] = False
                print(f'Book checked out by {self.users[user_id]["name"]}')
            else:
                print('Book is already checked out.')
        else:
            print('User or book not found.')

    def return_book(self, user_id, book_id):
        if user_id in self.users and book_id in self.books:
            if book_id in self.users[user_id]['checked_out_books']:
                self.users[user_id]['checked_out_books'].remove(book_id)
                self.books[book_id]['available'] = True
                print(f'Book returned by {self.users[user_id]["name"]}')
            else:
                print('User did not check out this book.')
        else:
            print('User or book not found.')


def main():
    library = Library()

    while True:
        print('\nLibrary Management System:')
        print('1. Add Book')
        print('2. Remove Book')
        print('3. Display Books')
        print('4. Register User')
        print('5. Check Out Book')
        print('6. Return Book')
        print('7. Quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            book_id = input('Enter book ID: ')
            title = input('Enter book title: ')
            author = input('Enter book author: ')
            library.add_book(book_id, title, author)

        elif choice == '2':
            book_id = input('Enter book ID to remove: ')
            library.remove_book(book_id)

        elif choice == '3':
            library.display_books()

        elif choice == '4':
            user_id = input('Enter user ID: ')
            name = input('Enter user name: ')
            library.register_user(user_id, name)

        elif choice == '5':
            user_id = input('Enter user ID: ')
            book_id = input('Enter book ID to check out: ')
            library.check_out_book(user_id, book_id)

        elif choice == '6':
            user_id = input('Enter user ID: ')
            book_id = input('Enter book ID to return: ')
            library.return_book(user_id, book_id)

        elif choice == '7':
            print('Exiting...')
            break

        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
