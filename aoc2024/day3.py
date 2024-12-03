import re

from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    return sum(int(x) * int(y) for x, y in re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', '\n'.join(data)))


def part2(data):
    enabled = True
    result = 0
    for match in re.finditer(r"(do(n't)?\(\)|mul\((?P<x>\d{1,3}),(?P<y>\d{1,3})\))", '\n'.join(data)):
        if match.group(0) == 'do()':
            enabled = True
        elif match.group(0) == "don't()":
            enabled = False
        elif enabled:
            result += int(match.group('x')) * int(match.group('y'))
    return result


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
