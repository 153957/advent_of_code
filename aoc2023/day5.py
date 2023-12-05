from itertools import pairwise
from math import inf
from operator import itemgetter
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    locations = []

    map_names = [
        'seed-to-soil map:',
        'soil-to-fertilizer map:',
        'fertilizer-to-water map:',
        'water-to-light map:',
        'light-to-temperature map:',
        'temperature-to-humidity map:',
        'humidity-to-location map:',
        '',
    ]

    seeds = [int(seed) for seed in data[0].partition(':')[2].split()]
    maps = {
        start: sorted([
            [int(value) for value in mapping.split()]
            for mapping in data[data.index(start)+1:(data.index(end)-1 if end else None)]
        ], key=itemgetter(1))
        for start, end in pairwise(map_names)
    }

    for seed in seeds:
        value = seed
        for mapper in maps.values():
            for destination, source, length in mapper:
                if value < source:
                    break
                elif source <= value < source + length:
                    value = destination + (value - source)
                    break
        locations.append(value)

    return min(locations)


def part2(data):
    result = {'location': inf}

    map_names = [
        'seed-to-soil map:',
        'soil-to-fertilizer map:',
        'fertilizer-to-water map:',
        'water-to-light map:',
        'light-to-temperature map:',
        'temperature-to-humidity map:',
        'humidity-to-location map:',
        '',
    ]

    maps = {
        start: sorted([
            [int(value) for value in mapping.split()]
            for mapping in data[data.index(start)+1:(data.index(end)-1 if end else None)]
        ], key=itemgetter(1))
        for start, end in pairwise(map_names)
    }

    def do_mapping(remaining_maps, start_value, current_length):
        if len(remaining_maps) == 0:
            result['location'] = min(start_value, result['location'])
            return

        for destination, source, length in remaining_maps[0]:
            if start_value + current_length < source:
                # between this and previous range
                # not inside this range
                do_mapping(
                    remaining_maps[1:],
                    start_value,
                    current_length,
                )
                break

            if start_value < source:
                # between this and previous range
                # also inside this range
                do_mapping(
                    remaining_maps[1:],
                    start_value,
                    source - start_value,
                )
                start_value, current_length = source, current_length - (source - start_value)

            if start_value + current_length < source + length:
                # inside this range
                # does not extend beyond this range
                offset = start_value - source
                do_mapping(
                    remaining_maps[1:],
                    destination + offset,
                    current_length,
                )
                break

            if start_value < source + length:
                # inside this range
                # extends beyond this range
                offset = start_value - source
                do_mapping(
                    remaining_maps[1:],
                    destination + offset,
                    length - offset,
                )
                start_value, current_length = source + length, current_length - (length - offset)

        else:
            # fully beyond all ranges
            do_mapping(
                remaining_maps[1:],
                start_value,
                current_length,
            )

    for i, (start_seed, length) in enumerate(pairwise(data[0].partition(':')[2].split())):
        if i % 2:
            continue
        do_mapping(list(maps.values()), int(start_seed), int(length))

    return result['location']


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
