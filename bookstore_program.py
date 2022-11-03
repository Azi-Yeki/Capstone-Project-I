#I'm not sure how to view the whole table and see if everything is happening like it should
import sqlite3

#open a file called student_db with a SQLite3 DB
db = sqlite3.connect('data/student_db')

#get a cursor object
cursor = db.cursor()

#creating the table named ebookstore
cursor.execute('''CREATE TABLE ebookstore(id INTEGER, title TEXT, author TEXT, qty INTEGER)
''')
db.commit()

#the data going into the table
#ids, titles,authors and quantities
id1 = 3001
title1 = "A Tale of Two Cities"
author1 = "Charles Dickens"
qty1 = 30

id2 = 3002
title2 = "Harry Potter and the Philosopher's Stone"
author2 = "J.K. Rowling"
qty2 = 40

id3 = 3003
title3 = "The Lion, the Witch and the Wardrobe"
author3 = "C.S. Lewis"
qty3 = 25

id4 = 3004
title4 = "The Lord of the Rings"
author4 = "J.R.R Tolkien"
qty4 = 37

id5 = 3005
title5 = "Alice In Wonderland"
author5 = "Lewis Carroll"
qty5 = 12

#populate table with data
cursor.execute('''INSERT INTO ebookstore(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id1,title1,author1,qty1))

cursor.execute('''INSERT INTO ebookstore(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id2,title2,author2,qty2))

cursor.execute('''INSERT INTO ebookstore(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id3,title3,author3,qty3))

cursor.execute('''INSERT INTO ebookstore(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id4,title4,author4,qty4))

cursor.execute('''INSERT INTO ebookstore(id, title, author, qty)
                  VALUES(?,?,?,?)''', (id5,title5,author5,qty5))

db.commit()

#create a menu with options for the user to choose from
while True:
    menu_choice = int(input('''WHat would you like to do?
    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    0. Exit
    Your choice: '''))

    #if the user chooses to enter a new book
    #they are prompted for information that gets added to the table
    if menu_choice == 1:
        id = int(input("Enter id: "))
        title = input("Book title: ")
        author = input("Author: ")
        qty = int(input("How many: "))
        cursor.execute('''INSERT INTO ebookstore(id, title, author, qty)
                          VALUES(?,?,?,?)''', (id,title,author,qty))
        print("Book added.")

        db.commit()

    #the title and author of a book never change so I'm guessing it's the quantity being changed
    #the user is prompted to enter a new quantity and the information is updated in the table
    elif menu_choice == 2:
        id = int(input("Enter id of book you want to update: "))
        qty = int(input("Enter new quantity: "))
        cursor.execute('''UPDATE ebookstore SET qty = ? WHERE id = ? ''', (qty,id))

        print("Updated.")
        db.commit()

    #the user enters the id for the book the want to delete and it is removed from the table
    elif menu_choice == 3:
        id = int(input("Enter id of book you want to delete: "))
        cursor.execute('''DELETE ebookstore WHERE id = ? ''', (id,))
        print("Book deleted.")
        db.commit()

    #if they are searching for a book
    #they enter the id and the book info is displayed
    elif menu_choice == 4:
        id = int(input("Enter id of book you want to search: "))
        cursor.execute('''SELECT id, title, author, qty FROM ebookstore WHERE id = ? ''', (id,))
        book = cursor.fetchone()
        print(book)

    #if the user chooses to exit the program
    elif menu_choice == 0:
        print("Goodbye.")
        exit()

    #if they enter an invalid choice
    else:
        print("Invalid choice, please try again.")