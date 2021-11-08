import StorehouseOfWisdom


class Saying(StorehouseOfWisdom):
    def __init__(self, content, country):
        self.country = country
        super(content)

    def __str__(self):
        return f'It is Saying ' \
               f'from {self.country}: ' \
               f'{self.content}. ' \
               f'Quotient = {self.getQuonitent()}'

