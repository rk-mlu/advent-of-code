""" Advent of Code 2022 -- Day 19 -- """

import aoc
import numpy as np

class Blueprint:
    def __init__(self, costs):
        self.ore_rob = costs[0]
        self.clay_rob = costs[1]
        self.obs_rob = costs[2]
        self.geo_rob = costs[3]

    def __str__(self):
        s = f'Costs: Ore R {self.ore_rob}. Clay R {self.clay_rob}.'
        s += f' Obsidian R {self.obs_rob}. Geode R {self.geo_rob}.'
        return s


def parsing(data):
    blueprints = []

    lines = data.splitlines()

    for line in lines:
        words = line.split()
        costs = []
        cost = np.array([int(words[6]), 0, 0, 0], dtype=int)
        costs.append(cost)
        cost = np.array([int(words[12]), 0, 0, 0], dtype=int)
        costs.append(cost)
        cost = np.array([int(words[18]), int(words[21]), 0, 0], dtype=int)
        costs.append(cost)
        cost = np.array([int(words[27]), 0, int(words[30]), 0], dtype=int)
        costs.append(cost)
        bluep = Blueprint(costs)
        blueprints.append(bluep)

    return blueprints


if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I    
    blueprints = parsing(data)

    for b in blueprints:
        print(b)
    
    # Part II
