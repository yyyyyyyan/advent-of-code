def trebuchet(puzzle_input):
    input_lines = puzzle_input.strip().split("\n")
    result = 0
    for line in input_lines:
        line_digits = [char for char in line if char.isdigit()]
        if line_digits:
            calibration = int(line_digits[0] + line_digits[-1])
            result += calibration
    return result


def trebuchet_final(puzzle_input):
    spelled_out_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for number, spelled_out_number in enumerate(spelled_out_numbers, start=1):
        puzzle_input = puzzle_input.replace(
            spelled_out_number, spelled_out_number + str(number) + spelled_out_number
        )
    return trebuchet(puzzle_input)
