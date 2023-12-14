from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    mirror_columns = list(zip(*data))

    def get_load(column):
        try:
            stop = column.index('#')
        except ValueError:
            stop = None
        n_rocks = column[:stop].count('O')
        result = sum(range(len(column) + 1 - n_rocks, len(column) + 1))
        if stop is None:
            pass
        elif column[stop:]:
            result += get_load(column[stop + 1:])

        return result

    return sum(get_load(column) for column in mirror_columns)


def part2(data):
    ...


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
