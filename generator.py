import random
from Riddle import Riddle
from Aphorism import Aphorism
from Saying import Saying


def nextInt(from_, to):
    return random.randint(from_, to)


def generateContent(length):
    generated_string = ''
    for i in range(length):
        generated_symbol = chr(nextInt(ord('A'), ord('z') + 1))
        while not generated_symbol.isalpha():
            generated_symbol = chr(nextInt(ord('A'), ord('z') + 1))
        generated_string += generated_symbol

    return generated_string


def getRandomRiddle():
    return Riddle(generateContent(nextInt(15, 100)),
                  generateContent(nextInt(5, 50)))


def getRandomAphorism():
    return Aphorism(generateContent(nextInt(3, 300)),
                    generateContent(nextInt(15, 50)))


def getRandomSaying():
    return Saying(generateContent(nextInt(10, 100)),
                  generateContent(nextInt(3, 30)))
