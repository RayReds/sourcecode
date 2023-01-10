"""Week 8 Perform - Part 2"""

from typing import TextIO

text = open("sample_games.txt", "r")
def get_game_dict(game_data: TextIO) -> dict[str, list[int]]:
    """Return a dictionary containing the team name and a list of points
    earned in each game for each team in the open file game_data.

    >>> input_file = open('sample_games.txt')
    >>> get_game_dict(input_file)
    {'Toronto Maple Leafs': [2, 2, 1, 0, 0, 2], 'Grande Prairie Storm': [], \
    'Montreal Canadiens': [1, 2, 1, 0, 2]}
    >>> input_file.close()
    """
    output = {}
    names = []
    for i in game_data:
        a = i.rstrip()
        if a.isdigit():
            output[names[-1]].append(int(a))
        else:
            if a not in names:
                names.append(a)
                output[names[-1]] = []
                continue
            names.append(a)
    return output
print(get_game_dict(text))
