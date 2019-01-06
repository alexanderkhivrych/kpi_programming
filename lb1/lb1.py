class Product:
    prize = 0
    name = ''
    id = ''

    def __init__(self, id, name, prize):
        self.name = name
        self.id = id
        self.prize = prize

    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Prize: {self.prize}'


class Customer:
    id = 0
    full_name = ''
    username = ''
    email = ''
    discount = 0

    def __init__(self, id, username, full_name, email, discount=0):
        self.id = id
        self.username = username
        self.full_name = full_name
        self.email = email
        self.discount = discount

    def __str__(self):
        return f'Username: {self.username}, Full name: {self.full_name}, Email: {self.email}, Discount: {self.discount}'


class Shop:
    __name = ''
    __products = dict()
    __regular_customers = dict()
    __discount = 0
    __season_discount = 0

    def __init__(self, name, products, regular_customers, discount=0, season_discount=0):
        self.__name = name
        self.__discount = discount
        self.__season_discount = season_discount
        for product in products:
            self.__products.update({product.id: product})
        for regular_customer in regular_customers:
            self.__regular_customers.update({regular_customer.id: regular_customer})

    def __str__(self):
        return f'Name: {self.__name}\n'

    def get_products(self):
        return self.__products.values()

    def get_customers(self):
        return self.__regular_customers.values()

    def get_product(self, id):
        return self.__products.get(id)

    def get_customer(self, id):
        return self.__regular_customers.get(id)

    def get_customer_discount(self, customer_id):
        customer = self.get_customer(customer_id)

        return customer.discount + self.__discount + self.__season_discount

    def calculateProductPrice(self, product_id, customer_id):
        product = self.get_product(product_id)
        customer = self.get_customer(customer_id)

        return product.prize - (product.prize * (customer.discount + self.__discount + self.__season_discount) / 100)


lia_shop = Shop(
    'The Lia Shop',
    [
        Product(1, 'T-Shirt Adidas', 2.5),
        Product(2, 'T-Shirt Nike', 4)
    ],
    [
        Customer(1, 'alex', 'Alexander Khivrych', 'alexandr.khivrich@gmail.com'),
        Customer(2, 'alexbruce', 'Alex Brucel', 'bruce@gmail.com', 10)
    ],
    2,
    2
)

customers = '\n'.join(map(lambda el: str(el), lia_shop.get_customers()))
products = '\n'.join(map(lambda el: str(el), lia_shop.get_products()))

current_customer_id = 2
selected_product_id = 1

print(f"Regular customers:\n-----------------\n{customers}\n-----------------")
print(f"Product list:\n-----------------\n{products}\n-----------------")

print(f"Hi, {lia_shop.get_customer(current_customer_id).full_name},"
      f" your discount is {lia_shop.get_customer_discount(current_customer_id)}%\n"
      f"total prize for {lia_shop.get_product(selected_product_id).name}"
      f" is {lia_shop.calculateProductPrice(selected_product_id, current_customer_id)}")
