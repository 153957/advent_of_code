from .get_inputs import get_inputs


def part1(assignments):
    contained_pairs = 0
    for assignment in assignments:
        elf1, _, elf2 = assignment.partition(',')
        start1, _, end1 = elf1.partition('-')
        start2, _, end2 = elf2.partition('-')
        if (
            int(start1) <= int(start2) and int(end1) >= int(end2)
            or int(start1) >= int(start2) and int(end1) <= int(end2)
        ):
            contained_pairs += 1
    return contained_pairs


def part2(assignments):
    overlapping_pairs = 0
    for assignment in assignments:
        elf1, _, elf2 = assignment.partition(',')
        start1, _, end1 = elf1.partition('-')
        start2, _, end2 = elf2.partition('-')
        if (
            int(start1) <= int(start2) <= int(end1)
            or int(start1) <= int(end2) <= int(end1)
            or int(start2) <= int(start1) <= int(end2)
            or int(start2) <= int(end1) <= int(end2)
        ):
            overlapping_pairs += 1
    return overlapping_pairs


if __name__ == '__main__':
    measurements = get_inputs('day4.txt')
    print(part1(measurements))
    print(part2(measurements))
