from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    result = 0
    for mirror in '\n'.join(data).split('\n\n'):
        mirror_lines = mirror.splitlines()
        number_of_lines = len(mirror_lines)

        # row reflection
        for reflection in range(1, number_of_lines):
            if all(
                top_line == bottom_line
                for top_line, bottom_line in zip(reversed(mirror_lines[:reflection]), mirror_lines[reflection:])
            ):
                result += 100 * reflection
                break
        else:
            mirror_columns = list(zip(*mirror_lines))

            # column reflection
            for reflection in range(1, len(mirror_columns)):
                if all(
                    top_line == bottom_line
                    for top_line, bottom_line in zip(reversed(mirror_columns[:reflection]), mirror_columns[reflection:])
                ):
                    result += reflection
                    break

    return result


def part2(data):
    ...


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
