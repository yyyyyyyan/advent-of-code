def get_adjacent_indexes(start_index, end_index, line_length):
    return (
        start_index - 1,
        end_index + 1,
        *[
            char_index
            for adjacent_index in range(start_index - 1, end_index + 2)
            for char_index in (
                adjacent_index - line_length,
                adjacent_index + line_length,
            )
        ],
    )


def gear_ratios(puzzle_input):
    engine = puzzle_input.strip()
    line_length = engine.index("\n") + 1
    engine += "\n" * (line_length - 1)
    numbers = "".join(char if char.isdigit() else " " for char in engine).split()
    end_index = 0
    result = 0
    for number in numbers:
        number_index = engine.index(number, end_index)
        end_index = number_index + len(number) - 1
        adjacent_chars = [
            engine[char_index]
            for char_index in get_adjacent_indexes(number_index, end_index, line_length)
        ]
        if any(char not in "0123456789.\n" for char in adjacent_chars):
            result += int(number)
    return result


def gear_ratios_final(puzzle_input):
    engine = puzzle_input.strip()
    line_length = engine.index("\n") + 1
    gears_indexes = []
    numbers_by_index = {}
    current_number = ""
    current_indexes = []
    for current_index, char in enumerate(engine):
        if char.isdigit():
            current_number += char
            current_indexes.append(current_index)
        else:
            numbers_by_index |= {
                number_index: (current_number, current_indexes[0])
                for number_index in current_indexes
            }
            current_number = ""
            current_indexes = []
            if char == "*":
                gears_indexes.append(current_index)
    result = 0
    max_adjacent = 2
    for gear_index in gears_indexes:
        adjacent_numbers = {
            numbers_by_index[adjacent_index]
            for adjacent_index in get_adjacent_indexes(
                gear_index, gear_index, line_length
            )
            if adjacent_index in numbers_by_index
        }
        if len(adjacent_numbers) == max_adjacent:
            ratio = 1
            for number in adjacent_numbers:
                ratio *= int(number[0])
            result += ratio
    return result
