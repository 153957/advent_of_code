from collections import deque

from .get_inputs import get_inputs


def part1(crates_and_moves):
    crates = crates_and_moves[:crates_and_moves.index('')]
    moves = crates_and_moves[crates_and_moves.index('') + 1:]
    stacks = [deque() for _ in crates[-1].split('   ')]

    for column, stack in enumerate(stacks):
        column_index = 1 + column * 4
        for crate_row in crates[:-1]:
            if len(crate_row) > column_index and crate_row[column_index].strip():
                stack.appendleft(crate_row[column_index])

    for move in moves:
        _, amount, _, origin, _, destination = move.split(' ')
        for _ in range(int(amount)):
            stacks[int(destination) - 1].append(stacks[int(origin) - 1].pop())

    return ''.join(stack.pop() for stack in stacks)


def part2(crates_and_moves):
    crates = crates_and_moves[:crates_and_moves.index('')]
    moves = crates_and_moves[crates_and_moves.index('') + 1:]
    stacks = [deque() for _ in crates[-1].split('   ')]

    for column, stack in enumerate(stacks):
        column_index = 1 + column * 4
        for crate_row in crates[:-1]:
            if len(crate_row) > column_index and crate_row[column_index].strip():
                stack.appendleft(crate_row[column_index])

    for move in moves:
        _, amount, _, origin, _, destination = move.split(' ')
        moved_crates = reversed([stacks[int(origin) - 1].pop() for _ in range(int(amount))])
        stacks[int(destination) - 1].extend(moved_crates)

    return ''.join(stack.pop() for stack in stacks)



if __name__ == '__main__':
    measurements = get_inputs('day5.txt')
    print(part1(measurements))
    print(part2(measurements))
