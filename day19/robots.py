""" Advent of Code 2022 -- Day 19 -- """

import aoc
import numpy as np
from scipy import optimize

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

def comp_geodes(bluep, time):
    # values of objective function (to be minimized)      
    values = np.zeros( 4*(time-1))
    val = np.arange(1,time)
    values[3*(time-1):] = -val[::-1]
    # print(values)

    # total number of linear constraints 
    # b_l <= A @ x <= b_u
    num_constr = 5*(time - 1)
    A = np.zeros( (num_constr, len(values)))
    b_u = np.zeros(num_constr)
    b_l = np.full_like(b_u, -np.inf)
    
    # enforce that only one robot is produced every minute
    for n in range(time-1):
        ind = (np.arange(len(values)) % (time-1)) == n
        A[n, ind] = 1
    b_u[:time-1] = 1.
    
    # enforce ore budget at every minute
    for n in range(time-1):
        prod = np.arange(-1,n)
        prod[0] = 0
        A[time-1 + n,     0     :           n+1] = -prod[::-1]+bluep.ore_rob[0] 
        A[time-1 + n,    time-1 :   time-1 +n+1] = bluep.clay_rob[0]
        A[time-1 + n, 2*(time-1):2*(time-1)+n+1] = bluep.obs_rob[0]
        A[time-1 + n, 3*(time-1):3*(time-1)+n+1] = bluep.geo_rob[0]
        b_u[time-1+n] = n

    # enforce clay budget at every minute
    for n in range(time-1):
        prod = np.arange(-1,n)
        prod[0] = 0
        A[2*(time-1)+n,     0     :           n+1] = bluep.ore_rob[1] 
        A[2*(time-1)+n,    time-1 :   time-1 +n+1] = -prod[::-1]+bluep.clay_rob[1]
        A[2*(time-1)+n, 2*(time-1):2*(time-1)+n+1] = bluep.obs_rob[1]
        A[2*(time-1)+n, 3*(time-1):3*(time-1)+n+1] = bluep.geo_rob[1]

    # enforce clay budget at every minute
    for n in range(time-1):
        prod = np.arange(-1,n)
        prod[0] = 0
        A[3*(time-1)+n,     0     :           n+1] = bluep.ore_rob[2] 
        A[3*(time-1)+n,    time-1 :   time-1 +n+1] = bluep.clay_rob[2]
        A[3*(time-1)+n, 2*(time-1):2*(time-1)+n+1] = -prod[::-1]+bluep.obs_rob[2]
        A[3*(time-1)+n, 3*(time-1):3*(time-1)+n+1] = bluep.geo_rob[2]
    
    # enforce clay budget at every minute
    for n in range(time-1):
        prod = np.arange(-1,n)
        prod[0] = 0
        A[4*(time-1)+n,     0     :           n+1] = bluep.ore_rob[3] 
        A[4*(time-1)+n,    time-1 :   time-1 +n+1] = bluep.clay_rob[3]
        A[4*(time-1)+n, 2*(time-1):2*(time-1)+n+1] = bluep.obs_rob[3]
        A[4*(time-1)+n, 3*(time-1):3*(time-1)+n+1] = -prod[::-1]+bluep.geo_rob[3]

    # print(A)
    # print(b_u)

    # feed objective function and constraints into optimizer
    constr = optimize.LinearConstraint(A, b_l, b_u)
    bounds = optimize.Bounds(0,1)
    integrality = np.full_like(values, True)
    
    res = optimize.milp(c=values, constraints=constr, integrality=integrality,
                        bounds=bounds)
   
    if not res.success:
        print("No success!")

    return -values@res.x, res.x



if __name__ == '__main__':
    data = aoc.get_input('input.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    # Part I    
    blueprints = parsing(data)
    time = 24
    
    quality_lvl = 0
    for k, b in enumerate(blueprints):
        num_geodes, x = comp_geodes(b, time)
        # print(x.reshape((4,time-1)).T)
        quality_lvl += round(num_geodes*(k+1))

    print(f'Part I: The sum of all quality levels is {quality_lvl}')
    
    # Part II
    time = 32
    p = 1
    for k, b in enumerate(blueprints[:3]):
        num_geodes, x = comp_geodes(b, time)
        # print(x.reshape((4,time-1)).T)
        p *= round(num_geodes)

    print(f'Part II: The product of geodes is {p}')
