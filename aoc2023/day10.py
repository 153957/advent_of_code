from collections import Counter
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    def get_next(x, y, direction):
        up = (x - 1, y, 'up')
        down = (x + 1, y, 'down')
        left = (x, y - 1, 'left')
        right = (x, y + 1, 'right')
        match data[x][y], direction:
            case '|', 'down':
                return down
            case '|', 'up':
                return up

            case '-', 'right':
                return right
            case '-', 'left':
                return left

            case 'L', 'down':
                return right
            case 'L', 'left':
                return up

            case 'J', 'down':
                return left
            case 'J', 'right':
                return up

            case '7', 'up':
                return left
            case '7', 'right':
                return down

            case 'F', 'up':
                return right
            case 'F', 'left':
                return down

            case _:
                raise Exception('hit ground')

    def get_forward_backward(x, y):
        directions = []
        if data[x - 1][y] in '|7F':
            directions.append((x - 1, y, 'up'))
        if data[x + 1][y] in '|LJ':
            directions.append((x + 1, y, 'down'))
        if data[x][y - 1] in '-FL':
            directions.append((x, y - 1, 'left'))
        if data[x][y + 1] in '-J7':
            directions.append((x, y + 1, 'right'))
        return directions

    start = next((i, j) for i, line in enumerate(data) for j, pipe in enumerate(line) if pipe == 'S')
    forward, backward = get_forward_backward(*start)
    step = 1
    while forward[:-1] != backward[:-1]:
        forward = get_next(*forward)
        backward = get_next(*backward)
        step +=1

    return step


def part2(data):
    def get_next(x, y, direction):
        up = (x - 1, y, 'up')
        down = (x + 1, y, 'down')
        left = (x, y - 1, 'left')
        right = (x, y + 1, 'right')
        match data[x][y], direction:
            case '|', 'down':
                return down, None
            case '|', 'up':
                return up, None

            case '-', 'right':
                return right, None
            case '-', 'left':
                return left, None

            case 'L', 'down':
                return right, 'counter-clockwise'
            case 'L', 'left':
                return up, 'clockwise'

            case 'J', 'down':
                return left, 'clockwise'
            case 'J', 'right':
                return up, 'counter-clockwise'

            case '7', 'up':
                return left, 'counter-clockwise'
            case '7', 'right':
                return down, 'clockwise'

            case 'F', 'up':
                return right, 'clockwise'
            case 'F', 'left':
                return down, 'counter-clockwise'

            case 'S', _:
                return None, 'end'

            case _:
                raise Exception('hit ground')

    def get_forward(x, y):
        if data[x - 1][y] in '|7F':
            return (x - 1, y, 'up')
        if data[x + 1][y] in '|LJ':
            return (x + 1, y, 'down')
        if data[x][y - 1] in '-FL':
            return (x, y - 1, 'left')
        if data[x][y + 1] in '-J7':
            return (x, y + 1, 'right')

    start = next((i, j) for i, line in enumerate(data) for j, pipe in enumerate(line) if pipe == 'S')
    forward = get_forward(*start)
    wise = {'counter-clockwise': 0, 'clockwise': 0, None: 0}
    pipe_loop = {start[:-1]: start[-1], forward[:-1]: forward[-1]}
    while forward[:-1] != start:
        forward, loop_wise = get_next(*forward)
        wise[loop_wise] += 1
        pipe_loop[forward[:-1]] = forward[-1]

    if wise['counter-clockwise'] - wise['clockwise'] > 0:
        wise = 'counter-clockwise'
        # Counter-clockwise: going down via |. or J. or going left via 7.
        left_combos = [('down', '|'), ('down', 'J'), ('left', '7')]
        right_combos = [('up', '|'), ('up', 'F'), ('right', 'L')]
    else:
        wise = 'clockwise'
        # Clockwise: going up via |. or 7. or going right via J.
        left_combos = [('up', '|'), ('up', '7'), ('right', 'J')]
        right_combos = [('down', '|'), ('down', 'L'), ('left', 'F')]

    enclosed_ground = 0

    ground_locations = ((i, j) for i, line in enumerate(data) for j, ground in enumerate(line) if (i, j) not in pipe_loop)
    for x, y in ground_locations:
        # first pipe on left
        for j in range(y, 0, -1):
            if (x, j) in pipe_loop:
                if (pipe_loop[x, j], data[x][j]) in left_combos:
                    # first pipe on right
                    for z in range(y, len(data[0])):
                        if (x, z) in pipe_loop:
                            if (pipe_loop[x, z], data[x][z]) in right_combos:
                                enclosed_ground += 1
                            break
                break

    return enclosed_ground


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
