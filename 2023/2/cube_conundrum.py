def is_game_possible(game, **max_colors):
    cube_sets_str = game.split(": ")[1].split("; ")
    for cube_set_str in cube_sets_str:
        cube_set_values = cube_set_str.split()
        cube_set = dict(zip(cube_set_values[1::2], cube_set_values[::2]))
        for color, max_value in max_colors.items():
            if int(cube_set.get(color, 0)) > max_value:
                return False
    return True


def cube_conundrum(puzzle_input, **max_colors):
    input_lines = puzzle_input.replace(",", "").strip().split("\n")
    result = 0
    for game_id, game_line in enumerate(input_lines, start=1):
        if is_game_possible(game_line, **max_colors):
            result += game_id
    return result


def cube_conundrum_final(puzzle_input):
    input_lines = puzzle_input.replace(",", "").replace(";", "").strip().split("\n")
    colors = ["red", "green", "blue"]
    result = 0
    for game in input_lines:
        cube_sets_values = game.split(": ")[1].split()
        min_colors = {}
        for color, value_str in zip(cube_sets_values[1::2], cube_sets_values[::2]):
            value = int(value_str)
            if value > min_colors.get(color, 0):
                min_colors[color] = value
        power = 1
        for color in colors:
            power *= min_colors.get(color, 0)
        result += power
    return result
