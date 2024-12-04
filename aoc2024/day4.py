from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    number_of_lines = len(data)
    line_length = len(data[0])

    horizontal = '\n'.join(data)
    vertical = '\n'.join(''.join(line[i] for line in data) for i in range(line_length))

    prepared_diagonal = [' ' * i + line + ' ' * (number_of_lines - i) for i, line in enumerate(data)]
    prepared_other_diagonal = [' ' * (number_of_lines - i) + line + ' ' * i for i, line in enumerate(data)]

    diagonal = '\n'.join(''.join(line[i] for line in prepared_diagonal) for i in range(line_length + number_of_lines))
    other_diagonal = '\n'.join(''.join(line[i] for line in prepared_other_diagonal) for i in range(line_length + number_of_lines))

    full_text = '|'.join([
        horizontal,
        vertical,
        diagonal,
        other_diagonal,
    ])

    return full_text.count('XMAS') + full_text.count('SAMX')


def part2(data):
    return sum(
        character == 'A' and (
            (
                (data[i][j] == 'S' and data[i+2][j+2] == 'M')
                or (data[i][j] == 'M' and data[i+2][j+2] == 'S')
            )
            and (
                (data[i][j+2] == 'S' and data[i+2][j] == 'M')
                or (data[i][j+2] == 'M' and data[i+2][j] == 'S')
            )
        )
        for i, line in enumerate(data[1:-1])
        for j, character in enumerate(line[1:-1])
    )


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
