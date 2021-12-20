from .get_inputs import get_inputs


def part1(digits):
    return sum(
        len(output_value.strip()) in [2, 3, 4, 7]
        for line in digits
        for output_value in line.partition(' | ')[2].split(' ')
    )


def part2(digits):
    sum_output = 0

    for line in digits:
        input_values, _, output_values = line.partition(' | ')
        input_values = [frozenset(input_value) for input_value in input_values.split(' ')]
        output_values = [frozenset(output_values) for output_values in output_values.split(' ')]

        length_sorted = sorted(input_values, key=len)

        eight = length_sorted.pop(9)
        four = length_sorted.pop(2)
        seven = length_sorted.pop(1)
        one = length_sorted.pop(0)

        remainder = set(length_sorted)

        three = next(
            input_value
            for input_value in remainder
            if len(input_value) == 5 and input_value.issuperset(seven)
        )
        remainder.remove(three)

        two = next(
            input_value
            for input_value in remainder
            if len(input_value) == 5 and len(input_value - four) == 3
        )
        remainder.remove(two)

        five = next(input_value for input_value in remainder if len(input_value) == 5)
        remainder.remove(five)

        zero = next(
            input_value
            for input_value in remainder
            if input_value.issuperset(one) and not input_value.issuperset(four)
        )
        remainder.remove(zero)

        six = next(
            input_value
            for input_value in remainder
            if not input_value.issuperset(seven)
        )
        remainder.remove(six)

        nine = remainder.pop()

        mapping = {
            zero: 0,
            one: 1,
            two: 2,
            three: 3,
            four: 4,
            five: 5,
            six: 6,
            seven: 7,
            eight: 8,
            nine: 9,
        }

        for position, number in enumerate(output_values):
            sum_output += mapping[number] * 10 ** (3 - position)

    return sum_output


if __name__ == '__main__':
    digits = get_inputs('day8.txt')
    print(part1(digits))
    print(part2(digits))
