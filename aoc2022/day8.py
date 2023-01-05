from .get_inputs import get_inputs


def part1(trees):
    return sum(
        1
        for x in range(len(trees))
        for y in range(len(trees[0]))
        if any(
            all(int(trees[x][y]) > int(tree_in_front) for tree_in_front in trees_in_front)
            for trees_in_front in [
                trees[x][:y],
                trees[x][y + 1:],
                [trees[k][y] for k in range(x)],
                [trees[k][y] for k in range(x + 1, len(trees))],
            ]
        )
    )


def part2(trees):
    return max(
        (
            len(list(reversed(trees[x][:y])))
            if all(int(trees[x][y]) > int(tree_in_front) for tree_in_front in list(reversed(trees[x][:y])))
            else [int(trees[x][y]) > int(tree_in_front) for tree_in_front in list(reversed(trees[x][:y]))].index(False) + 1
        ) * (
            len(trees[x][y + 1:])
            if all(int(trees[x][y]) > int(tree_in_front) for tree_in_front in trees[x][y + 1:])
            else [int(trees[x][y]) > int(tree_in_front) for tree_in_front in trees[x][y + 1:]].index(False) + 1
        ) * (
            len(list(reversed([trees[k][y] for k in range(x)])))
            if all(int(trees[x][y]) > int(tree_in_front) for tree_in_front in list(reversed([trees[row][y] for row in range(x)])))
            else [int(trees[x][y]) > int(tree_in_front) for tree_in_front in list(reversed([trees[row][y] for row in range(x)]))].index(False) + 1
        ) * (
            len([trees[k][y] for k in range(x + 1, len(trees))])
            if all(int(trees[x][y]) > int(tree_in_front) for tree_in_front in [trees[row][y] for row in range(x + 1, len(trees))])
            else [int(trees[x][y]) > int(tree_in_front) for tree_in_front in [trees[row][y] for row in range(x + 1, len(trees))]].index(False) + 1
        )
        for x in range(len(trees))
        for y in range(len(trees[0]))
    )


if __name__ == '__main__':
    trees = get_inputs('day8.txt')
    print(part1(trees))
    print(part2(trees))
