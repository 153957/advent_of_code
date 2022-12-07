import string

from .get_inputs import get_inputs


def part1(sacks):
    return sum(
        string.ascii_letters.index(item) + 1
        for sack in sacks
        for item in set(sack[:len(sack) // 2]).intersection(sack[len(sack) // 2:])
    )


def part2(sacks):
    return sum(
        string.ascii_letters.index(item) + 1
        for sack1, sack2, sack3 in zip(sacks[::3], sacks[1::3], sacks[2::3])
        for item in set(sack1).intersection(sack2).intersection(sack3)
    )


if __name__ == '__main__':
    sacks = get_inputs('day3.txt')
    print(part1(sacks))
    print(part2(sacks))
