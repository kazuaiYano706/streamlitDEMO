class Book:

    def __init__(self, title: str, author: str, price: int) -> None:

        self.title = title
        self.author = author
        self.price = price

    def print(self) -> None:
        print(f'書籍：{self.title}著者：{self.author}価格：{self.price}')

book1 = Book('aa','bb',2600)
book2 = Book('新・明解python','柴田',2600)

book1.print()
book2.print()
