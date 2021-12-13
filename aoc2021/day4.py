from itertools import groupby
from operator import itemgetter

from .get_inputs import get_inputs


def part1(bingo):
    number_pool = [int(number) for number in bingo[0].split(',')]

    cards = [
        [
            *[
                {int(card.split('\n')[row][column:column+3]) for row in range(5)}
                for column in range(0, 15, 3)
            ],
            *[
                {int(card.split('\n')[row][column:column+3]) for column in range(0, 15, 3)}
                for row in range(5)
            ]
        ]
        for card in '\n'.join(bingo[2:]).split('\n\n')
    ]

    for drawn_number in number_pool:
        for card in cards:
            for options in card:
                if drawn_number in options:
                    options.remove(drawn_number)

            if any(not len(options) for options in card):
                return drawn_number * sum({number for options in card for number in options})


def part2(bingo):
    number_pool = [int(number) for number in bingo[0].split(',')]

    cards = [
        [
            *[
                {int(card.split('\n')[row][column:column+3]) for row in range(5)}
                for column in range(0, 15, 3)
            ],
            *[
                {int(card.split('\n')[row][column:column+3]) for column in range(0, 15, 3)}
                for row in range(5)
            ]
        ]
        for card in '\n'.join(bingo[2:]).split('\n\n')
    ]

    unfinished_cards = set(range(len(cards)))

    for drawn_number in number_pool:
        for card_number, card in enumerate(cards):
            if card_number in unfinished_cards:
                for options in card:
                    if drawn_number in options:
                        options.remove(drawn_number)

                if any(not len(options) for options in card):
                    unfinished_cards.remove(card_number)
                if not unfinished_cards:
                    return drawn_number * sum({number for options in card for number in options})


if __name__ == '__main__':
    bingo = get_inputs('day4.txt')
    print(part1(bingo))
    print(part2(bingo))

