from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    return sum(
        int(2 ** len(
            {int(number) for number in line.partition(':')[2].partition('|')[0].split(' ') if number}.intersection(
                {int(number) for number in line.partition('|')[2].split(' ') if number}
            )
        ) / 2)
        for line in data
    )


def part2(data):
    scores = [
        len(
            {int(number) for number in line.partition(':')[2].partition('|')[0].split(' ') if number}.intersection(
                {int(number) for number in line.partition('|')[2].split(' ') if number}
            )
        )
        for line in data
    ]
    scratch_cards = [1 for score in scores]
    for i, score in enumerate(scores):
        for _ in range(scratch_cards[i]):
            for j in range(i + 1, i + 1 + score):
                scratch_cards[j] += 1
    return sum(scratch_cards)


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
