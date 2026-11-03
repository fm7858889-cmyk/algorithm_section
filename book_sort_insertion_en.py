class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"{self.title} - {self.author} ({self.year})"


def insertion_sort(books, key, reverse=False):
    arr = list(books)

    for i in range(1, len(arr)):
        current = arr[i]
        current_value = key(current)
        j = i - 1

        while j >= 0:
            if reverse:
                should_move = key(arr[j]) < current_value
            else:
                should_move = key(arr[j]) > current_value
            if not should_move:
                break
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = current

    return arr


def get_books_from_user():
    books = []
    n = int(input("How many books do you want to enter? "))
    for i in range(n):
        print(f"\n--- Book {i + 1} ---")
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Publication year: "))
        books.append(Book(title, author, year))
    return books


def main():
    books = [
        Book("The Alchemist", "Paulo Coelho", 1988),
        Book("Awlad Haretna", "Naguib Mahfouz", 1959),
        Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", 1967),
        Book("1984", "George Orwell", 1949),
        Book("Les Miserables", "Victor Hugo", 1862),
    ]

    print("Books before sorting:")
    for b in books:
        print(" ", b)

    print("\nSorted by title:")
    for b in insertion_sort(books, key=lambda b: b.title):
        print(" ", b)

    print("\nSorted by author:")
    for b in insertion_sort(books, key=lambda b: b.author):
        print(" ", b)

    print("\nSorted by year (newest first):")
    for b in insertion_sort(books, key=lambda b: b.year, reverse=True):
        print(" ", b)

    choice = input("\nDo you want to enter your own books? (y/n): ").strip().lower()
    if choice in ("y", "yes"):
        user_books = get_books_from_user()
        print("\nSorted by year (oldest first):")
        for b in insertion_sort(user_books, key=lambda b: b.year):
            print(" ", b)


if __name__ == "__main__":
    main()
