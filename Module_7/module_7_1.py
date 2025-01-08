class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'Наименование: {self.name}; вес: {self.weight}; категория: {self.category}'

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        self.__content = ''

    def __contains__(self, product):
        return product.name in str(self.__content)

    def get_products(self):
        file = open(self.__file_name, 'r', encoding='utf-8')
        self.__content = file.read()
        file.close()
        return self.__content

    def add(self, *products):
        self.get_products()
        file = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            if product in self:
                print(f'Продукт "{product.name}" уже есть в магазине')
            else:
                file.write(str(product) + '\n')
        file.close()


s1 = Shop()
p1 = Product('Картофель', 50.5, 'Овощи')
p2 = Product('Спагетти', 3.4, 'Бакалейные товары')
p3 = Product('Картофель', 5.5, 'Овощи')

print(str(p2) + '\n')

s1.add(p1, p2, p3)

print('\n--- Содержимое магазина ---')
print(s1.get_products())