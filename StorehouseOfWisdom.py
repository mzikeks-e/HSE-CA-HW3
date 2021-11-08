class StorehouseOfWisdom:
    def __init__(self, content):
        self.content = content

    def getQuotient(self):
        punctuation_count = 0
        for symbol in self.content:
            if not symbol.isalpha() and not symbol.isdigit():
                punctuation_count += 1

        return punctuation_count / len(self.content)
