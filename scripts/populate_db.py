from catalog.models import Category, Tag, Product

# Create 5 categories
category_electronics = Category.objects.create(name="Electronics")
category_clothing = Category.objects.create(name="Clothing")
category_home_appliances = Category.objects.create(name="Home Appliances")
category_books = Category.objects.create(name="Books")
category_toys = Category.objects.create(name="Toys")

# Create 10 tags
tag_new = Tag.objects.create(name="New")
tag_sale = Tag.objects.create(name="Sale")
tag_popular = Tag.objects.create(name="Popular")
tag_discounted = Tag.objects.create(name="Discounted")
tag_trending = Tag.objects.create(name="Trending")
tag_hot = Tag.objects.create(name="Hot")
tag_best_seller = Tag.objects.create(name="Best Seller")
tag_limited_edition = Tag.objects.create(name="Limited Edition")
tag_gift_idea = Tag.objects.create(name="Gift Idea")
tag_clearance = Tag.objects.create(name="Clearance")

# Create 20 products
product_1 = Product.objects.create(
    name="Smartphone",
    description="A new and popular smartphone with the latest features.",
    category=category_electronics
)
product_1.tags.add(tag_new, tag_popular, tag_sale)

product_2 = Product.objects.create(
    name="T-shirt",
    description="A stylish T-shirt available for a discounted price.",
    category=category_clothing
)
product_2.tags.add(tag_sale, tag_discounted, tag_trending)

product_3 = Product.objects.create(
    name="Laptop",
    description="A powerful laptop for work and play.",
    category=category_electronics
)
product_3.tags.add(tag_new, tag_popular, tag_sale)

product_4 = Product.objects.create(
    name="Jeans",
    description="Comfortable jeans for everyday wear.",
    category=category_clothing
)
product_4.tags.add(tag_popular, tag_discounted, tag_clearance)

product_5 = Product.objects.create(
    name="Wireless Earbuds",
    description="High-quality wireless earbuds for music lovers.",
    category=category_electronics
)
product_5.tags.add(tag_new, tag_discounted, tag_trending)

product_6 = Product.objects.create(
    name="Air Conditioner",
    description="A powerful air conditioner to keep your home cool.",
    category=category_home_appliances
)
product_6.tags.add(tag_hot, tag_sale, tag_trending)

product_7 = Product.objects.create(
    name="Washing Machine",
    description="An efficient washing machine with multiple settings.",
    category=category_home_appliances
)
product_7.tags.add(tag_sale, tag_best_seller)

product_8 = Product.objects.create(
    name="Smart Watch",
    description="A smart watch with fitness tracking and notifications.",
    category=category_electronics
)
product_8.tags.add(tag_new, tag_trending, tag_best_seller)

product_9 = Product.objects.create(
    name="Sofa",
    description="A comfortable sofa with premium cushioning.",
    category=category_home_appliances
)
product_9.tags.add(tag_hot, tag_best_seller, tag_clearance)

product_10 = Product.objects.create(
    name="Gaming Console",
    description="A high-performance gaming console for gamers.",
    category=category_electronics
)
product_10.tags.add(tag_new, tag_sale, tag_popular)

product_11 = Product.objects.create(
    name="Novel",
    description="A gripping novel about an unforgettable journey.",
    category=category_books
)
product_11.tags.add(tag_new, tag_trending)

product_12 = Product.objects.create(
    name="Cookbook",
    description="A cookbook with healthy recipes for every meal.",
    category=category_books
)
product_12.tags.add(tag_popular, tag_best_seller)

product_13 = Product.objects.create(
    name="Board Game",
    description="A fun and engaging board game for family nights.",
    category=category_toys
)
product_13.tags.add(tag_trending, tag_best_seller)

product_14 = Product.objects.create(
    name="Puzzle Set",
    description="A challenging puzzle set for all ages.",
    category=category_toys
)
product_14.tags.add(tag_new, tag_popular, tag_gift_idea)

product_15 = Product.objects.create(
    name="Smartphone Case",
    description="A durable smartphone case to protect your device.",
    category=category_electronics
)
product_15.tags.add(tag_sale, tag_discounted)

product_16 = Product.objects.create(
    name="Tennis Racket",
    description="A lightweight tennis racket for competitive players.",
    category=category_toys
)
product_16.tags.add(tag_popular, tag_clearance)

product_17 = Product.objects.create(
    name="Electric Kettle",
    description="An efficient electric kettle to boil water quickly.",
    category=category_home_appliances
)
product_17.tags.add(tag_sale, tag_discounted)

product_18 = Product.objects.create(
    name="E-reader",
    description="A lightweight e-reader for reading books on the go.",
    category=category_books
)
product_18.tags.add(tag_new, tag_best_seller)

product_19 = Product.objects.create(
    name="Action Figure",
    description="A detailed action figure from your favorite movie.",
    category=category_toys
)
product_19.tags.add(tag_popular, tag_gift_idea)

product_20 = Product.objects.create(
    name="Blender",
    description="A powerful blender for making smoothies and shakes.",
    category=category_home_appliances
)
product_20.tags.add(tag_hot, tag_trending, tag_sale)

print("Database populated with 20 sample products.")
