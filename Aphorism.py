import StorehouseOfWisdom


class Aphorism(StorehouseOfWisdom):
    def __init__(self):
        self.author = ""

    @staticmethod
    def input(file):
        aphorism = Aphorism()
        return aphorism

    @staticmethod
    def inputRandom():
        aphorism = Aphorism()
        return aphorism
