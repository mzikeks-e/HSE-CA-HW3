import StorehouseOfWisdom


class Saying(StorehouseOfWisdom):
    def __init__(self):
        self.country = ""

    @staticmethod
    def input(file):
        saying = Saying()
        return saying

    @staticmethod
    def inputRandom():
        saying = Saying()
        return saying
