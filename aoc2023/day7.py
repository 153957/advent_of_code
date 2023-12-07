from collections import Counter
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    card_order = '23456789TJQKA'
    type_order = ['high', 'one', 'two', 'three', 'full', 'four', 'five']

    def get_type(hand):
        c = Counter(hand).most_common()
        if len(c) == 1:
            return 'five'
        if len(c) == 2 and c[0][1] == 4:
            return 'four'
        if len(c) == 2 and c[0][1] == 3:
            return 'full'
        if len(c) == 3 and c[0][1] == 3:
            return 'three'
        if len(c) == 3 and c[0][1] == 2:
            return 'two'
        if len(c) == 4:
            return 'one'
        if len(c) == 5:
            return 'high'

    def keyfunc(line):
        return (
            type_order.index(get_type(line.partition(' ')[0])),
            card_order.index(line[0]),
            card_order.index(line[1]),
            card_order.index(line[2]),
            card_order.index(line[3]),
            card_order.index(line[4]),
        )

    return sum(
        multiplier * int(line.partition(' ')[2])
        for multiplier, line in enumerate(sorted(data, key=keyfunc), 1)
    )


def part2(data):
    card_order = 'J23456789TQKA'
    type_order = ['high', 'one', 'two', 'three', 'full', 'four', 'five']

    def get_type(hand):
        card_counter = Counter(hand)
        most_common_card, amount = card_counter.most_common(1)[0]
        if most_common_card == 'J' and amount != 5:
            card_counter[card_counter.most_common(2)[1][0]] += amount
            del card_counter['J']
        elif most_common_card != 'J':
            card_counter[most_common_card] += card_counter['J']
            del card_counter['J']

        c = card_counter.most_common()
        if len(c) == 1:
            return 'five'
        if len(c) == 2 and c[0][1] == 4:
            return 'four'
        if len(c) == 2 and c[0][1] == 3:
            return 'full'
        if len(c) == 3 and c[0][1] == 3:
            return 'three'
        if len(c) == 3 and c[0][1] == 2:
            return 'two'
        if len(c) == 4:
            return 'one'
        if len(c) == 5:
            return 'high'

    def keyfunc(line):
        return (
            type_order.index(get_type(line.partition(' ')[0])),
            card_order.index(line[0]),
            card_order.index(line[1]),
            card_order.index(line[2]),
            card_order.index(line[3]),
            card_order.index(line[4]),
        )

    return sum(
        multiplier * int(line.partition(' ')[2])
        for multiplier, line in enumerate(sorted(data, key=keyfunc), 1)
    )


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
