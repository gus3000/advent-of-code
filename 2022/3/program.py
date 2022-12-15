from typing import Set

from advent_lib.advent_lib import *

# bags = read_test_input()
bags = read_input()


def letter_value(letter: str) -> int:
    if letter.islower():
        return ord(letter) - ord('a') + 1
    return ord(letter) - ord('A') + 27


def letter_in_common(s1: str, s2: str, s3: str = None) -> str:
    for c in s1:
        if c in s2 and (s3 is None or c in s3):
            return c
    raise Exception('unable to find common letter')


def handle_bag(bag: str) -> int:
    first = bag[0:len(bag) // 2]
    second = bag[len(bag) // 2:]
    letter = letter_in_common(first, second)
    priority = letter_value(letter)
    # print(f'bag => {first} - {second}, letter : {letter} => {priority}')
    return priority


def handle_bag_triplet(group: [str]) -> int:
    letter = letter_in_common(group[0], group[1], group[2])
    priority = letter_value(letter)
    print(f'group => group, letter : {letter} => {priority}')
    return priority


priorities = 0
group = []
for bag in bags:
    # priorities += handle_bag(bag)
    group.append(bag)
    if len(group) == 3:
        priorities += handle_bag_triplet(group)
        group = []

print(priorities)
