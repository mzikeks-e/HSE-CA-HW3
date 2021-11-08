from StorehouseOfWisdom import StorehouseOfWisdom


class Riddle(StorehouseOfWisdom):
    def __init__(self, content, answer):
        super().__init__(content)
        self.answer = answer

    def __str__(self):
        return f'It is Riddle. ' \
               f'Question: {self.content}. ' \
               f'Answer: {self.answer}. ' \
               f'Quotient = {self.getQuotient()}'
