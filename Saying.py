from StorehouseOfWisdom import StorehouseOfWisdom


class Saying(StorehouseOfWisdom):
    def __init__(self, content, country):
        super().__init__(content)
        self.country = country

    def __str__(self):
        return f'It is Saying ' \
               f'from {self.country}: ' \
               f'{self.content}. ' \
               f'Quotient = {self.getQuotient()}'

