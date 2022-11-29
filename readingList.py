 # * ADD A BOOK
def addBook():
    title = input("What is the title of the book? ").strip().title()
    author = input("Who is the author of the book? ").strip().title()
    releaseDate = input("When was the book released? ").strip()
    read = input("Have you read this book?\n1 for Yes\n2 for No || ")

    while read != "1" and read != "2":
        print("That is not an option.")
        read = input("Have you read this book?\n1 for Yes\n2 for No || ")
    else:
        if read == "1":
            read = "/"
        else:
            read = "X"

    print(f"\n{title} added!\n")
    return {
        "title": title,
        "author": author,
        "releaseDate":releaseDate,
        "read": read,
    }


 # * SEE YOUR ADDED BOOKS
def seeList(list):
    if len(list) > 0:
        print("\n")
        for book in list:
            title = book["title"]
            author = book["author"]
            releaseDate = book["releaseDate"]
            read = book["read"]
            print(f"{read} - {title} ({releaseDate}) by {author}")
    else:
        print("\nYou do not have any books in your list yet.")


 # * SEARCH FOR AN ADDED BOOk
def search(userIn, list):
    if len(list) > 0:
        books = []
        for book in list:
            title = book["title"]

            if title == userIn:
                books.append(book)
                continue
            else: continue
        
        if len(books) > 0:
            for book in books:
                title = book["title"]
                author = book["author"]
                releaseDate = book["releaseDate"]
                read = book["read"]

                print(f"\n{read} - {title} ({releaseDate}) by {author}\n")
        else:
            print("\nWe do not have any books of that title.\n")
    else:
        print("\nYou do not have any items in your reading list.\n")


def readBook(book, list):
    for bookData in list:
        bookTitle = bookData['title']
        bookRead = bookData["read"]

        if book == bookTitle and bookRead == "X":
            bookData["read"] = "/"
            print(f"\n{bookTitle} marked as read!\n")
            break
    else:
        print(f"\nNo book found with the name '{book}'. Or the book is already marked as read.\n")


def delete(book, list):
    for bookData in list:
        bookTitle = bookData["title"]
        
        if book == bookTitle:
            print(f"\nSuccessfully deleted {bookTitle}!\n")
            list.remove(bookData)
            return
    else:
        print(f"\nNo book found with the title, {book}.\n")


# * MAIN
readingList = []

try:
    with open("books.csv", "r") as bookFiles:
        bookData = bookFiles.readlines()

    for line in bookData[0::]:
        title, author, releaseDate, read = line.strip().split(",")

        readingList.append({
            "title": title,
            "author": author,
            "releaseDate": releaseDate,
            "read": read,
        })   
except:
    pass


while True:
    option = input(("Welcome to your Reading List | What would you like to do?\n1. Add a book\n2. See my reading list\n3. Search my list\n4. Mark a book as read\n5. Remove a book\n6. Exit || "))

    if option == "1":
        addedBook = (addBook())
        readingList.append(addedBook)

        title = addedBook["title"]
        author = addedBook["author"]
        releaseDate = addedBook["releaseDate"]
        read = addedBook["read"]

        with open("books.csv", "a") as bookData:
            title, author, releaseDate, read = readingList[-1].values()
            bookData.write(",".join(addedBook.values()) + "\n")

    elif option == "2":
        seeList(readingList)
        print("\n")

    elif option == "3":
        title = input("Enter the book name, make sure that it is the same one you entered: ").strip().title()
        search(title, readingList)

    elif option == "4":
        book = input("What is the book that you wish to mark as read? ").strip().title()
        readBook(book, readingList)

    elif option == "5":
        book = input("What is the book that you wish to delete? ").strip().title()
        delete(book, readingList)

        with open("books.csv", "w") as bookData:
            bookData.truncate()
            for row in readingList:
                title = row["title"]
                author = row["author"]
                releaseDate = row["releaseDate"]
                read = row["read"]

                title, author, releaseDate, read = row.values()
                bookData.write(",".join(row.values()) + "\n")

    elif option == "6":
        break

    else:
        print("\nThat is not a valid option.\n")
