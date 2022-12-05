import string

from .get_inputs import get_inputs


def part1(assignments):
    contained_pairs = 0
    for assignment in assignments:
        elf1, _, elf2 = assignment.partition(',')
        start11, _, end11 = elf1.partition('-')
        start21, _, end21 = elf2.partition('-')
        if (
            int(start11) <= int(start21) and int(end11) >= int(end21)
            or int(start11) >= int(start21) and int(end11) <= int(end21)
        ):
            contained_pairs += 1
    return contained_pairs

def part2(assignments):
    overlapping_pairs = 0
    for assignment in assignments:
        elf1, _, elf2 = assignment.partition(',')
        start11, _, end11 = elf1.partition('-')
        start21, _, end21 = elf2.partition('-')
        if (
            int(start11) <= int(start21) <= int(end11)
            or int(start11) <= int(end21) <= int(end11)
            or int(start21) <= int(start11) <= int(end21)
            or int(start21) <= int(end11) <= int(end21)
        ):
            overlapping_pairs += 1
    return overlapping_pairs


if __name__ == '__main__':
    measurements = get_inputs('day4.txt')
    print(part1(measurements))
    print(part2(measurements))
