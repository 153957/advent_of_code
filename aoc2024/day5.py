from collections import defaultdict
from functools import cmp_to_key
from pathlib import Path

from .get_inputs import get_inputs


def part1(data):
    order_items, page_lists = data[:data.index('')], data[data.index('') + 1:]

    order = defaultdict(set)
    for line in order_items:
        early, _, later = line.partition('|')
        order[early].add(later)

    middle_sum = 0
    for pages in page_lists:
        pages = pages.split(',')
        relevant_order = {early: later for early, later in order.items() if early in pages}
        for page in pages:
            if page in relevant_order:
                del relevant_order[page]
            if any(page in laters for laters in relevant_order.values()):
                break
        else:
            middle_sum += int(pages[len(pages) // 2])

    return middle_sum


def part2(data):
    order_items, page_lists = data[:data.index('')], data[data.index('') + 1:]

    order = defaultdict(set)
    for line in order_items:
        early, _, later = line.partition('|')
        order[early].add(later)

    def order_by_order(a, b):
        if b in order[a]:
            return -1
        elif a in order[b]:
            return 1
        return -1

    sorter = cmp_to_key(order_by_order)

    middle_sum = 0
    for pages in page_lists:
        pages = pages.split(',')
        relevant_order = {early: later for early, later in order.items() if early in pages}
        for page in pages:
            if page in relevant_order:
                del relevant_order[page]
            if any(page in laters for laters in relevant_order.values()):
                break
        else:
            continue
        sorted_pages = sorted(pages, key=sorter)
        middle_sum += int(sorted_pages[len(pages) // 2])

    return middle_sum


if __name__ == '__main__':
    data = get_inputs(f'{Path(__file__).stem}.txt')
    print(part1(data))
    print(part2(data))
