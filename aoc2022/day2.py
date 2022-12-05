from .get_inputs import get_inputs


def part1(hands):
    hand_score = {'X': 1, 'Y': 2, 'Z': 3}
    score = sum(hand_score[elf_response.partition(' ')[2]] for elf_response in hands)

    for elf_response in hands:
        if elf_response in ['A X', 'B Y', 'C Z']:
            score += 3
        elif elf_response in ['A Y', 'B Z', 'C X']:
            score += 6

    return score


def part2(hands):
    outcome_score = {'X': 0, 'Y': 3, 'Z': 6}
    score = sum(outcome_score[elf_response.partition(' ')[2]] for elf_response in hands)

    for elf_outcome in hands:
        elf, _, outcome = elf_outcome.partition(' ')
        score += {
            'X': {'A': 3, 'B': 1, 'C': 2},
            'Y': {'A': 1, 'B': 2, 'C': 3},
            'Z': {'A': 2, 'B': 3, 'C': 1},
        }[outcome][elf]

    return score


if __name__ == '__main__':
    measurements = get_inputs('day2.txt')
    print(part1(measurements))
    print(part2(measurements))
