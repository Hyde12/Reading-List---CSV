 # * ADD A BOOK
def addBook(title, author, releaseDate):

    print(f"\n{title} added!\n")
    return {
        "title": title,
        "author": author,
        "releaseDate":releaseDate,
    }

 # * SEE YOUR ADDED BOOKS
def seeList(list):
    if len(list) > 0:
        print("\n")
        for book in list:
            title = book["title"]
            author = book["author"]
            releaseDate = book["releaseDate"]
            print(f"- {title} ({releaseDate}) by {author}")
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
                print(f"\n- {title} ({releaseDate}) by {author}\n")
        else:
            print("\nWe do not have any books of that title.\n")
    else:
        print("\nYou do not have any items in your reading list.\n")

# * MAIN

readingList = []

try:
    with open("books.csv", "r") as bookFiles:
        bookData = bookFiles.readlines()

        for line in bookData:
            title, author, releaseDate = line.strip().split(",")

            readingList.append({
                "title": title,
                "author": author,
                "releaseDate": releaseDate,
            })
except:
    pass

while True:
    option = input(("Welcome to your Reading List | What would you like to do?\n1. Add a book\n2. See my reading list\n3. Search my list\n4. Exit || "))

    if option == "1":
        title = input("What is the title of the book? ").strip().title()
        author = input("Who is the author of the book? ").strip().title()
        releaseDate = input("When was the book released? ").strip()
        addedBook = (addBook(title, author, releaseDate))
        readingList.append(addedBook)

        title = addedBook["title"]
        author = addedBook["author"]
        releaseDate = addedBook["releaseDate"]

        with open("books.csv", "w") as bookData:
            title, author, releaseDate = addedBook.values()
            bookData.write(",".join(addedBook.values()) + "\n")
    elif option == "2":
        seeList(readingList)
        print("\n")
    elif option == "3":
        title = input("Enter the book name, make sure that it is the same one you entered: ").strip().title()
        search(title, readingList)
    elif option == "4":
        break
    else:
        print("\nThat is not a valid option.\n")

