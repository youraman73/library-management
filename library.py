import csv
from prettytable import PrettyTable

# Function to display the menu
def display_menu():
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Quit")

# Function to add a book to the CSV file
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    with open('lib.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title, author])
    print("Book added successfully!")

# Function to display all books in a table
def display_books():
    table = PrettyTable()
    table.field_names = ["Title", "Author"]

    with open('lib.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            table.add_row([row[0], row[1]])

    print(table)

# Function to search for a book by title and display the results in a table
def search_book():
    search_title = input("Enter the title to search: ")

    table = PrettyTable()
    table.field_names = ["Title", "Author"]

    with open('lib.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if search_title.lower() in row[0].lower():
                table.add_row([row[0], row[1]])

    result_string = table.get_string()

    if result_string.strip():  # Check if the result string is not empty
        print("Search Results:")
        print(result_string)
    else:
        print("Book not found.")



# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        display_books()
    elif choice == '3':
        search_book()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
