from .get_inputs import get_inputs


def part1(brackets):
    opening_brackets = set('([{<')
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    bracket_scores = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    score = 0

    for line in brackets:
        expected = []
        for character in line:
            if character in opening_brackets:
                expected.append(character)
            elif expected and bracket_pairs[character] == expected[-1]:
                expected.pop()
            else:
                score += bracket_scores[character]
                break

    return score


def part2(brackets):
    opening_brackets = set('([{<')
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    bracket_scores = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4,
    }

    scores = []

    for line in brackets:
        score = 0
        expected = []
        for character in line:
            if character in opening_brackets:
                expected.append(character)
            elif expected and bracket_pairs[character] == expected[-1]:
                expected.pop()
            else:
                break
        else:
            while expected:
                score *= 5
                score += bracket_scores[expected.pop()]
            scores.append(score)

    return sorted(scores)[len(scores) // 2]


if __name__ == '__main__':
    brackets = get_inputs('day10.txt')
    print(part1(brackets))
    print(part2(brackets))
