from pprint import pprint

from app.db import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
    {
        "name": "Gourmet Loose Leaf Tea",
        "description": "A selection of premium loose leaf teas to enjoy while reading your favorite book.",
        "price": "15.99",
        "url": "https://images.unsplash.com/photo-1527398317618-b3da8a79e0ca?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Handcrafted Coffee Blend",
        "description": "Rich and aromatic coffee blends, handcrafted to enhance your reading moments.",
        "price": "18.50",
        "url": "https://plus.unsplash.com/premium_photo-1671379523824-c8aae61cb52a?q=80&w=1680&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Luxury Reading Pillow",
        "description": "Supportive and comfortable reading pillow, perfect for long hours of reading in bed or on the sofa.",
        "price": "29.95",
        "url": "https://images.unsplash.com/photo-1575276510486-aa55619a8170?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Organic Snack Box",
        "description": "A box filled with healthy, organic snacks ideal for snacking while flipping through pages.",
        "price": "20.00",
        "url": "https://images.unsplash.com/photo-1677735299567-841ce2069588?q=80&w=1942&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Artisan Chocolate Bars",
        "description": "Deliciously rich artisan chocolate bars to pair with your evening reading.",
        "price": "12.99",
        "url": "https://images.unsplash.com/photo-1526081347589-7fa3cb41b4b2?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Scented Soy Candles",
        "description": "Soy candles with calming scents to set the perfect ambiance for reading.",
        "price": "14.50",
        "url": "https://images.unsplash.com/photo-1603218678692-3967d7523bb0?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Decorative Bookmarks",
        "description": "Beautifully crafted bookmarks that are as stylish as they are functional.",
        "price": "9.99",
        "url": "https://images.unsplash.com/photo-1561865406-62a037159577?q=80&w=1480&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Ergonomic Book Holder",
        "description": "An ergonomic book holder that prevents neck strain and keeps your pages in place.",
        "price": "34.99",
        "url": "https://images.unsplash.com/photo-1624862760439-4056a5111511?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    },
    {
        "name": "Herbal Relaxation Kit",
        "description": "A kit including herbal teas and aromatherapy oils designed to relax and rejuvenate.",
        "price": "22.50",
        "url": "https://images.unsplash.com/photo-1697399511512-17d3adfab058?q=80&w=1472&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }
]



if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    products = Product.all()
    print("FOUND", len(products), "PRODUCTS:")
    if any(products):
        for product in products:
            #breakpoint()
            pprint(dict(product))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Product.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    product = Product.find(1)
    print(product.name)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Product.where(name="Strawberries")
    print(len(matches))
    product = matches[0]
    print(product.name)

    print("------------")
    print("CREATING NEW PRODUCT...")
    params = {
        "name": "Blueberries",
        "price":3.99,
        "description":"organic blues",
        "url": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?q=80&w=2938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    }
    Product.create(params)
