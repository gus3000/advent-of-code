from advent_lib.advent_lib import *

symbols_labels = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
}

# answer_symbols = {
#     'X': 'A',
#     'Y': 'B',
#     'Z': 'C',
# }

answer_score = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

symbol_values = {
    'A': 1,
    'B': 2,
    'C': 3,
}

score = {
    'A': {
        'A': 3,
        'B': 6,
        'C': 0,
    },
    'B': {
        'A': 0,
        'B': 3,
        'C': 6,
    },
    'C': {
        'A': 6,
        'B': 0,
        'C': 3,
    },
}


def compute_score(opponent_symbol: str, my_symbol: str) -> int:
    return symbol_values[my_symbol] + score[opponent_symbol][my_symbol]


guide = read_input()

score_grid = []
for line in guide:
    # print(f'=> {l}')
    l = line.split()
    opponent_symbol = l[0]
    result = l[1]
    possible_symbols = score[opponent_symbol]
    my_symbol = [s for s in possible_symbols if score[opponent_symbol][s] == answer_score[result]][0]
    # print(f'{l} => {my_symbol}')
    # my_symbol = answer_symbols[l[1]]
    score_grid.append(compute_score(opponent_symbol, my_symbol))
    # print(f'opponent will play {opponent_symbol} => answer with {my_symbol}')
    # print(f'score : {compute_score(opponent_symbol, my_symbol)}')

print(f"total score : {sum(score_grid)}")