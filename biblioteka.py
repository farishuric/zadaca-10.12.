print("1 - Add book,\n2 - Show all books,\n3 - Remove book,\n4 - Show book details\n5 - Program end")
user_input = int(input("Enter your command: "))


add_book = 1
show_all_books = 2
remove_book = 3
show_book_details = 4
program_end = 5
books = []
book_place = 1
book_place_details = 1

while True:
    if user_input == 1:
        user_book_input = input("Enter name of book? ")
        user_book_details = input("Enter book details? ")
        user_book_author = input("Enter book author? ")
        books.append([user_book_input, user_book_details, user_book_author])
        user_input = int(input("Enter your command:"))
    if user_input == 2:
        for i in books:
            print (book_place, i[0])
            book_place = book_place + 1
        book_place = 1
        user_input = int(input("Enter your command:"))
    if user_input == 3:
        for i in books:
            print(book_place, i[0])
            book_place = book_place + 1
        book_place = 1
        user_book_remove = int(input("Which book do you want to remove? "))
        if user_book_remove == 1:
            books.remove(books[0])
        if user_book_remove == 2:
            books.remove(books[1])
        if user_book_remove == 3:
            books.remove(books[2])
        if user_book_remove == 4:
            books.remove(books[3])
        if user_book_remove == 5:
            books.remove(books[4])
        user_input = int(input("Enter your command:"))
        book_place = 1
    if user_input == 4:
        for i in books:
            print(book_place_details, i[0])
            book_place_details = book_place_details + 1
        book_details_give = int(input("Which book are you interested in details? "))
        if book_details_give == 1:
            print(books[0][1])
        if book_details_give == 2:
            print(books[1][1])
        if book_details_give == 3:
            print(books[2][1])
        user_input = int(input("Enter your command:"))
        book_place_details = 1
    if user_input == 5:
        print("Have a nice day.")
        break

    

