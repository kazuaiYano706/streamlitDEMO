class Book:

    def __init__(self, title: str, author: str, price: int)-> None:

        self.__title = title
        self.__author = author
        self.__price = price

    def print(self):
        print('書籍：{}　著者：{}　価格：{}'.format(self.__title,self.__author,self.__price))

    @property
    def title (self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def price(self) -> str:
        return self.__price

    def __str__(self)-> None:
        return self.__title + self.__author + str(self.__price)



b1 = Book("JAVA","kawaba",2600)
b2 = Book('Python','sibata',2600)

print(b1)
print(b2)

print('total price:',b1.price+b2.price)