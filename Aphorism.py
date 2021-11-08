import StorehouseOfWisdom


class Aphorism(StorehouseOfWisdom):
    def __init__(self, content, author):
        self.author = author
        super(content)

    def __str__(self):
        return f'It is Aphorism. ' \
               f'{self.content} - says ' \
               f'{self.author}. ' \
               f'Quotient = {self.getQuonitent()}'
