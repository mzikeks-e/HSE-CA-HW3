from StorehouseOfWisdom import StorehouseOfWisdom


class Aphorism(StorehouseOfWisdom):
    def __init__(self, content, author):
        super().__init__(content)
        self.author = author

    def __str__(self):
        return f'It is Aphorism. ' \
               f'{self.content} - says ' \
               f'{self.author}. ' \
               f'Quotient = {self.getQuotient()}'
