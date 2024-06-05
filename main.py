def main():
    bookList = []
    
    choice = 0
    while choice != 4:
        print("-----Book Manager-----")
        print("1) Add a book")
        print("2) Look up a book")
        print("3) Display all books")
        print("4) Quit")
        
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            print("Adding a book...")
            nBook = input("Enter the name of the book >>> ")
            nAuthor = input("Enter the name of the author >>> ")
            nPages = input("Enter the number of pages >>> ")
            bookList.append([nBook, nAuthor, nPages])
        elif choice == 2:
            print("Looking up a book...")
            keyword = input("Enter Search Term: ")
            found_books = [book for book in bookList if keyword.lower() in [entry.lower() for entry in book]]
            if found_books:
                for book in found_books:
                    print(book)
            else:
                print("No books found with the search term.")
        elif choice == 3:
            print("Displaying all books...")
            for book in bookList:
                print(book)
        elif choice == 4:
            print("Quitting Program")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
