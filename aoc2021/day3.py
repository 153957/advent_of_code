from itertools import groupby
from operator import itemgetter

from .get_inputs import get_inputs


def part1(diagnostics):
    n_diagnostics = len(diagnostics)
    n_bits = len(diagnostics[0])

    bin_gamma = ''.join(
        str(int(
            n_diagnostics < sum(
                2 * int(diagnostic[bit])
                for diagnostic in diagnostics
            )
        ))
        for bit in range(n_bits)
    )

    gamma = int(bin_gamma, 2)
    epsilon = int(bin_gamma.translate({ord('0'): '1', ord('1'): '0'}) , 2)

    return gamma * epsilon


def part2(diagnostics):
    ...


if __name__ == '__main__':
    diagnostics = get_inputs('day3.txt')
    print(part1(diagnostics))
    print(part2(diagnostics))

