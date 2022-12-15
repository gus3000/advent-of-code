import parse
from advent_lib.advent_lib import *


def contains(min1: int, max1: int, min2: int, max2: int) -> bool:
    return min1 <= min2 and max1 >= max2


def overlaps(min1: int, max1: int, min2: int, max2: int) -> bool:
    return min2 <= min1 <= max2 or min2 <= max1 <= max2 or min1 <= min2 <= max1 or min1 <= max2 <= max1


def redundant(min1: int, max1: int, min2: int, max2: int) -> bool:
    return contains(min1, max1, min2, max2) or contains(min2, max2, min1, max1)


def main():
    # assignments = read_test_input()
    assignments = read_input()

    format = '{:d}-{:d},{:d}-{:d}'

    toConsiderate = 0
    for a in assignments:
        min1, max1, min2, max2 = parse.parse(format, a)
        redondant = redundant(min1, max1, min2, max2)
        overlap = overlaps(min1, max1, min2, max2)
        print(f'{a} => ({min1},{max1}) ({min2},{max2}) => {redondant}, {overlap}')
        if overlap:
            toConsiderate += 1

    print(f'to considerate : {toConsiderate}')


if __name__ == '__main__':
    main()
