import StorehouseOfWisdom
from Riddle import Riddle
from Aphorism import Aphorism
from Saying import Saying


class Container:
    def __init__(self):
        self.length = 0
        self.container = []

    def clear(self):
        self.container = []
        self.length = 0

    def input(self, filename):
        file = open(filename, 'r').readlines()
        for line in file:
            if len(line.split()) != 3:
                raise AttributeError('Error while reading file!\n'
                                     'input string must have 3 arguments separated by spaces\n'
                                     'first - integer from 0 to 3, second and third - content')

            wisdom_type, content1, content2 = line.split()
            if wisdom_type == '0':  # riddle
                self.container.append(Riddle(content1, content2))
            elif wisdom_type == '1':  # aphorism
                self.container.append(Aphorism(content1, content2))
            elif wisdom_type == '2':  # saying
                self.container.append(Saying(content1, content2))
            else:
                raise AttributeError('Error while reading file!\n'
                                     'argument 1 (type) should be a integer from 0 to 3\n'
                                     '(0 - riddle, 1 - aphorism, 2 - saying)')
            self.length += 1

    def inputRandom(self, size):
        pass

    def progressingV22(self, filename):
        file = open(filename, 'w')
        mean = sum([i.getQuotient() for i in self.container]) / len(self.container)
        file.write(f'Arithmetic mean: {mean}\n')

        file.writelines([el + "\t" + el.getQuotient() for el in self.container
                         if el.getQuotient() <= mean])
        file.writelines([el + "\t" + el.getQuotient() for el in self.container
                         if el.getQuotient() > mean])

    def out(self, filename):
        file = open(filename, 'w')
        file.write(f'Container contains {len(self.container)} elements.')
        file.writelines([el for el in self.container])

