import pymongo

# Підключення до сервера MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Створення бази даних
db = client["library_database"]

# Створення колекцій
books_collection = db["books"]
authors_collection = db["authors"]
visitors_collection = db["visitors"]

# Додавання авторів
authors_collection.insert_one({"name": "J.K. Rowling", "birth_year": 1965})
authors_collection.insert_one({"name": "George Orwell", "birth_year": 1903})

# Додавання книг
authors_rowling = authors_collection.find_one({"name": "J.K. Rowling"})
authors_orwell = authors_collection.find_one({"name": "George Orwell"})
books_collection.insert_one({"title": "Harry Potter and the Philosopher's Stone", "author": authors_rowling["_id"], "year_published": 1997})
books_collection.insert_one({"title": "Harry Potter and the Chamber of Secrets", "author": authors_rowling["_id"], "year_published": 1998})
books_collection.insert_one({"title": "1984", "author": authors_orwell["_id"], "year_published": 1949})

# Додавання відвідувачів
visitors_collection.insert_one({"first_name": "Alice", "last_name": "Smith", "membership_number": "V12345"})
visitors_collection.insert_one({"first_name": "Bob", "last_name": "Johnson", "membership_number": "V67890"})

# Пошук книги за назвою
book = books_collection.find_one({"title": "1984"})
if book:
    author = authors_collection.find_one({"_id": book["author"]})
    print(f"Знайдена книга: {book['title']}, Автор: {author['name']}, Рік публікації: {book['year_published']}")
else:
    print("Книга не знайдена.")

# Пошук книг за автором
author_rowling = authors_collection.find_one({"name": "J.K. Rowling"})
books = books_collection.find({"author": author_rowling["_id"]})
print(f"Книги автора {author_rowling['name']}:")
for book in books:
    print(f" - {book['title']}, Рік публікації: {book['year_published']}")

# Оновлення року публікації книги
books_collection.update_one({"title": "1984"}, {"$set": {"year_published": 1950}})
print("Рік публікації книги '1984' оновлено на 1950.")

# Видалення книги
books_collection.delete_one({"title": "Harry Potter and the Philosopher's Stone"})
print("Книга 'Harry Potter and the Philosopher's Stone' видалена.")

# Видалення відвідувача
visitors_collection.delete_one({"first_name": "Alice", "last_name": "Smith"})
print("Відвідувач Alice Smith видалений.")

# Закриття підключення
client.close()
