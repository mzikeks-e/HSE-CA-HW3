import sys
import os
from Container import Container
import time


def main():
    try:
        time_start = time.time()
        inp = sys.argv[1:]
        if len(inp) != 4:
            printInputError()
            return

        print('Start. Please, check, that all spaces in content of storehouse replaced with _.')
        container = Container()

        if inp[0] == '-f':
            container.input(inp[1])
        elif inp[0] == '-n':
            if int(inp[1]) > 100000:
                raise AttributeError('Error! Count for generation should be < 100000')
            container.inputRandom(int(inp[1]))
        else:
            printInputError()
            return

        if not os.path.isdir('out'):
            os.mkdir('out')
        container.out(inp[2])
        container.progressingV22(inp[3])
        container.clear()

    except Exception as e:
        print(e)
    else:
        print('Successfully finished')
        print('время работы программы', time.time() - time_start)


def printInputError():
    print('Incorrect command!\n'
          'Waited:\n'
          '-f infile outfile01 outfile02\n'
          'Or:\n'
          '-n number outfile01 outfile02')


if __name__ == '__main__':
    main()
