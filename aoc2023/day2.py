from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    in_bag = (12, 13, 14)  # red, green, blue
    game_id_sum = 0

    for game in data:
        game_cubes = {'red': 0, 'green': 0, 'blue': 0}

        hands = game.partition(':')[2].split(';')
        for hand in hands:
            for n_colors in hand.split(','):
                n, _, color = n_colors.strip().partition(' ')
                game_cubes[color] = max(game_cubes[color], int(n))

        if all(seen <= allowed for seen, allowed in zip(game_cubes.values(), in_bag)):
            game_id_sum += int(game.partition(':')[0].partition(' ')[2])

    return game_id_sum


def part2(data):
    game_power_sum = 0

    for game in data:
        game_cubes = {'red': 0, 'green': 0, 'blue': 0}

        hands = game.partition(':')[2].split(';')
        for hand in hands:
            for n_colors in hand.split(','):
                n, _, color = n_colors.strip().partition(' ')
                game_cubes[color] = max(game_cubes[color], int(n))

        game_power_sum += game_cubes['red'] * game_cubes['green'] * game_cubes['blue']

    return game_power_sum


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
