class Basket:
    def __init__(self):
        self.contents = []
        self.discount = 0

    def add(self, *books):
        for book in books:
            self.contents.append(book)

    def count_discount(self):
        distinct_books = len(set(self.contents_names()))
        if distinct_books > 1:
            return (distinct_books - 1) * 0.05
        return 0
