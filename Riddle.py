import StorehouseOfWisdom


class Riddle(StorehouseOfWisdom):
    def __init__(self, content, answer):
        self.answer = answer
        super(content)

    def __str__(self):
        return f'It is Riddle. ' \
               f'Question: {self.content}. ' \
               f'Answer: {self.answer}. ' \
               f'Quotient = {self.getQuonitent()}'
