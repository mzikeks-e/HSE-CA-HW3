import sys
from Container import Container


def main():
    inp = sys.argv[1:]
    if len(inp) != 4:
        printInputError()
        return

    print('Start. Please, check, that all spaces in content of storehouse replaced with _.')
    container = Container()

    if inp[0] == '-f':
        container.input(inp[1])
    elif inp[0] == '-n':
        container.inputRandom(int(inp[1]))
    else:
        printInputError()
        return

    container.out(inp[2])
    container.progressingV22(inp[3])
    container.clear()
    print("finished")


def printInputError():
    print('Incorrect command!\n'
          'Waited:\n'
          '-f infile outfile01 outfile02\n'
          'Or:\n'
          '-n number outfile01 outfile02')


if __name__ == '__main__':
    main()
