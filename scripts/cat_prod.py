from shop.models import Category, Product


def run():
    rock = Category.objects.create(name="Rock")
    blues = Category.objects.create(name="Blues")
    hard_rock = Category.objects.create(name="Hard Rock", parent=rock)
    pop_rock = Category.objects.create(name="Pop Rock", parent=rock)

    # Create products and assign them to categories
    product1 = Product.objects.create(name="Guitar", price=599.99)
    product1.categories.add(rock, hard_rock)

    product2 = Product.objects.create(name="Drums", price=899.99)
    product2.categories.add(rock)

    product3 = Product.objects.create(name="Saxophone", price=499.99)
    product3.categories.add(blues)

    product4 = Product.objects.create(name="Microphone", price=199.99)
    product4.categories.add(pop_rock)

    product5 = Product.objects.create(name="Keyboard", price=799.99)
    product5.categories.add(pop_rock)

    product5 = Product.objects.create(name="Keyboard", price=879.99)
    product5.categories.add(blues)

    print("Data was added to database")