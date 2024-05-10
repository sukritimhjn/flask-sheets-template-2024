
from app.db import BaseModel

class Book(BaseModel):

    SHEET_NAME = "books"

    COLUMNS = ["title", "author", "year", "price", "img"]

    SEEDS = [
       {"title": "To Kill a Mockingbird","author": "Harper Lee", "year": 1960, "price": 10, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715320076/to-kill-a-mocking-bird_x9i9qk.jpg"},
       {"title": "1984", "author": "George Orwell", "year": 1949, "price": 9, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715320130/1984-george-orwell_imsg6m.jpg"},
       {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "price": 8.76, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715320267/the-great-gatsby_ubbqlt.jpg"},
       {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "price": 11, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715320368/the-catcher-in-the-Rye_r3re4x.jpg"},
       {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813, "price": 10, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715320540/pride-and-prejudice_dl9r9d.jpg"},
       {"title": "To the Lighthouse", "author": "Virginia Woolf", "year": 1927, "price": 13, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715320630/to-the-Lighthouse_ht0nff.jpg"},
       {"title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937, "price": 12, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715324253/the-hobbit_w2eg32.jpg"},
       {"title": "Moby-Dick", "author": "Herman Melville", "year": 1851, "price": 9.99, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715324253/moby-dick_qizr6h.jpg"},
       {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "price": 10.13, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715324037/brave-new-world_jbij4l.jpg"},
       {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "year": 1865, "price": 15, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715324252/alice-wonderland_a0tcy8.jpg"},
       {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "year": 1997, "price": 11, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715324252/harry-potter-philosopher-stone_qfgbuy.jpg"},
       {"title": "Harry Potter and the Chamber of Secrets", "author": "J.K. Rowling", "year": 1998, "price": 8.75, "img":"https://res.cloudinary.com/di0vnxjrj/image/upload/v1715324252/harry-potter-chambers-of-secret_b764xn.jpg"},
   ]


if __name__ == "__main__":

    # books = Book.all()
    # print("FOUND", len(books), "BOOKS")
    # if any(books):
    #     for book in books:
    #         print(book.title, book.author, book.year)
    # else:
    #     Book.seed()

    print("------------")
    print("EXISTING RECORDS:")
    books = Book.all()
    print("FOUND", len(books), "BOOKS")
    if any(books):
        for book in books:
            #breakpoint()
            pprint(dict(book))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Book.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    book = Book.find(1)
    print(book.title)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Book.where(title="To Kill a Mockingbird")
    print(len(matches))
    book = matches[0]
    print(book.title)

    print("------------")
    print("CREATING NEW BOOK...")
    params = {
        "title": "The Magic of Thinking Big",
        "author": "David J. Schwartz",
        "year": 1959,
        "price": 12.75,
        "img":"https://i.imgur.com/t9zxmVq.jpeg"
        },
    Book.create(params)

