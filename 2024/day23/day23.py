""" Advent of Code 2024 -- Day 23 -- """
year = 2024
day = 23     # set day!

import sys
sys.path.append('../../aux')
import aoc
from itertools import combinations, repeat
import numpy as np
from scipy.sparse import csr_array
# from scipy.sparse.csgraph import dijkstra, reconstruct_path

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    coord = dict()
    coord_inv = []
    counter = 0
    I = []
    J = []
    
    for line in lines:
        w1, w2 = line.split('-')
        
        i1 = coord.get(w1, -1)
        if i1 == -1:
            i1 = counter
            coord[w1] = counter
            coord_inv.append(w1)
            counter += 1
        i2 = coord.get(w2, -1)
        if i2 == -1:
            i2 = counter
            coord[w2] = counter
            coord_inv.append(w2)
            counter += 1

        I.append(i1)
        J.append(i2)

        I.append(i2)
        J.append(i1)
    
    I = np.array(I, dtype=np.int32)
    J = np.array(J, dtype=np.int32)
    data = np.array(len(I)*[1], dtype=int)
    W = csr_array( (data, (I, J)), dtype=int)

    return lines, coord, coord_inv, W
   
def get_nbs(i, W):
    r = W[[i],:]
    r_nb = r.nonzero()[1]
    return set(r_nb)

def get_3parties(W, N):
    parties = set()

    for i in range(N):
        nbs = get_nbs(i, W)

        for j,k in combinations(nbs, 2):
            if j > i and k > i and W[j,k] > 0:
                parties.add((i,j,k))

    return parties

def find_largest_lan_party(W, parties):

    num_elem = 3
    while True:
        
        new_parties = set()

        for p1,p2 in combinations(parties, 2):
            cap = set(p1) & set(p2)
            if len(cap) == num_elem - 1:
                sym_diff = set(p1) ^ set(p2)
                e1 = sym_diff.pop()
                e2 = sym_diff.pop()
                if W[e1,e2] > 0:
                    cap.add(e1)
                    cap.add(e2)
                    new_party = list(cap)
                    new_party.sort()
                    new_parties.add(tuple(new_party))

        parties = new_parties
        if len(new_parties) > 1:
            num_elem += 1
            print(num_elem, len(new_parties))
        else :
            break

    return parties



if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    lines, coord, coord_inv, W = parsing(data)
    

    # Part I    
    
    N = len(coord)
    parties = get_3parties(W, N)

    ans1 = 0

    for p in parties:
        startT = False
        for n in p:
            name_comp = coord_inv[n]
            if name_comp.startswith('t'):
                startT = True
        if startT:
            ans1 += 1

    print(f'Answer to part 1: {ans1}')

    # Part II

    print('Warning: run time for part 2 is quite extensive! (~60 min)')
    party = find_largest_lan_party(W, parties)
    p = party.pop()
    for n in p:
        comps = [coord_inv[n] + s for (n,s) in zip(p, repeat(','))]
    comps.sort()
    
    ans2 = "".join(comps)
    ans2 = ans2[:-1]
    
    print(f'Answer to part 2: {ans2}')
