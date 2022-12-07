from collections import deque

from .get_inputs import get_inputs


def part1(datastream):
    message_length = 4
    marker = deque(datastream[0][0] * message_length)
    return next(
        i
        for i, datum in enumerate(datastream[0], 1)
        if marker.popleft() and marker.append(datum) or len(set(marker)) == message_length
    )


def part2(datastream):
    message_length = 14
    marker = deque(datastream[0][0] * message_length)
    return next(
        i
        for i, datum in enumerate(datastream[0], 1)
        if marker.popleft() and marker.append(datum) or len(set(marker)) == message_length
    )


if __name__ == '__main__':
    datastream = get_inputs('day6.txt')
    print(part1(datastream))
    print(part2(datastream))
