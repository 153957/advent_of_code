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
    diagnostics.sort()

    n_bits = len(diagnostics[0])

    oxygen_candidates = diagnostics
    co2_candidates = diagnostics

    for bit in range(n_bits):
        oxygen_groups = {key: list(group) for key, group in groupby(oxygen_candidates, key=itemgetter(bit))}
        if len(oxygen_groups) == 1:
            oxygen_candidates = list(oxygen_groups.values())[0]
        elif len(oxygen_groups['0']) > len(oxygen_groups['1']):
            oxygen_candidates = oxygen_groups['0']
        else:
            oxygen_candidates = oxygen_groups['1']

        co2_groups = {key: list(group) for key, group in groupby(co2_candidates, key=itemgetter(bit))}
        if len(co2_groups) == 1:
            co2_candidates = list(co2_groups.values())[0]
        elif len(co2_groups['1']) < len(co2_groups['0']):
            co2_candidates = co2_groups['1']
        else:
            co2_candidates = co2_groups['0']

    oxygen = oxygen_candidates[0]
    co2 = co2_candidates[0]

    return int(oxygen, 2) * int(co2, 2)


if __name__ == '__main__':
    diagnostics = get_inputs('day3.txt')
    print(part1(diagnostics))
    print(part2(diagnostics))

