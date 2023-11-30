""" Advent of Code 2022 -- Day 05 -- """

import copy

# arange cargo as list
cargo_ini = [['Z', 'P', 'B', 'Q', 'M', 'D', 'N'], 
         ['V', 'H', 'D', 'M', 'Q', 'Z', 'L', 'C'],
         ['G', 'Z', 'F', 'V', 'D', 'R', 'H', 'Q'],
         ['N', 'F', 'D', 'G', 'H'],
         ['Q', 'F', 'N'],
         ['T', 'B', 'F', 'Z', 'V', 'Q', 'D'],
         ['H', 'S', 'V', 'D', 'Z', 'T', 'M', 'Q'],
         ['Q', 'N', 'P', 'F', 'G', 'M'],
         ['M', 'R', 'W', 'B']]

# correct order of crates
cargo = []

for n, stack in enumerate(cargo_ini):
    s = stack.copy()
    s.reverse()
    cargo.append(s)

cargo2 = copy.deepcopy(cargo)

def print_cargo(cargo):
    solution = []
    for j, stack in enumerate(cargo, start=1):
        print(f'Stack {j}: {stack}')
        solution.append(stack[-1])
    print(f'The solution is {solution}')

def move_crate(cargo, fr, to, num):
    for i in range(num):
        crate = cargo[fr-1].pop()
        cargo[to-1].append(crate)

def move_crates(carg, fr, to, num):
    carg[to-1].extend(carg[fr-1][-num:].copy())
    carg[fr-1] = carg[fr-1][:-num]


def parse_moves(data):
    moves = []
    for line in data.splitlines():
        words = line.split()
        move = []
        for word in words:
            if word.isnumeric():
                move.append(int(word))
        moves.append(move)
    return moves

print_cargo(cargo)

with open('moves.txt', 'r') as file:
    data = file.read()

moves = parse_moves(data)

for move in moves:
    move_crate(cargo, move[1], move[2], move[0])
     
print_cargo(cargo)

print('Part II')

print_cargo(cargo2)

for move in moves:
    move_crates(cargo2, move[1], move[2], move[0])
    
# print(cargo2)
print_cargo(cargo2)


