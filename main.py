import sys
import Container


def main():
    inp = sys.argv[1:]
    if len(inp) != 5:
        printInputError()
        return

    print("Start. Please, check, that all spaces in content of storehouse replaced with _.")
    container = Container()



def printInputError():
    print('''Incorrect command!\n
           Waited:\n
           -f infile outfile01 outfile02\n
           Or:\n
           -n number outfile01 outfile02''')


if __name__ == '__main__':
    main()
