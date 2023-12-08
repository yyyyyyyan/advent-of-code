def gear_ratios(puzzle_input):
    engine = puzzle_input.strip()
    line_length = engine.index("\n") + 1
    engine += "\n" * (line_length - 1)
    numbers = "".join(char if char.isdigit() else " " for char in engine).split()
    start_index = 0
    result = 0
    for number in numbers:
        number_index = engine.index(number, start_index)
        start_index = number_index + len(number)
        adjacent_chars = [
            engine[number_index - 1],
            engine[start_index],
            *[
                engine[char_index - line_length]
                for char_index in range(number_index - 1, start_index + 1)
            ],
            *[
                engine[char_index + line_length]
                for char_index in range(number_index - 1, start_index + 1)
            ],
        ]
        if any(char not in "0123456789.\n" for char in adjacent_chars):
            result += int(number)
    return result
