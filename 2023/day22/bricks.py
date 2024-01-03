""" Advent of Code 2023 -- Day 22 -- """
year = 2023
day = 22     # set day!

import sys
sys.path.append('../../aux')
import aoc
import numpy as np
import heapq
import random

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()

    coords = []
    for line in lines:
        start, end = line.split('~')
        start = np.array([int(c) for c in start.split(',')])
        end = np.array([int(c) for c in end.split(',')])

        coords.append((start, end))

    return coords

class Brick:
    def __init__(self, num, coords):
        self.id = num
        self.start = coords[0]
        self.end = coords[1]
        self.resting = False
        self.supporting = set()
        self.supported = set()

        self.axis = 0
        for d in range(3):
            if coords[1][d] - coords[0][d] < 0:
                print('error')

            if coords[1][d] - coords[0][d] != 0:

                self.axis = d
                break

        self.min_h = min(coords[0][2], coords[1][2])

    def __str__(self):
        dim = {0: 'x', 1: 'y', 2: 'z'}
        s = f'Brick {self.id}: {self.start}~{self.end} '
        s += f'extds along {dim[self.axis]}-axis '
        status = {True: 'resting', False: 'falling'}
        s += f'and is {status[self.resting]}.'
        return s
    
    def fall1(self):
        self.start[2] -= 1
        self.end[2] -= 1
        self.min_h -= 1
        
    def rests_on(self, rbr):
        # checks if self is supported by rbr
        
        for x in range(rbr.start[0],rbr.end[0]+1):
            for xx in range(self.start[0],self.end[0]+1):
                if x == xx:
                    for y in range(rbr.start[1],rbr.end[1]+1):
                        for yy in range(self.start[1],self.end[1]+1):
                            if y == yy:
                                for z in range(rbr.start[2],rbr.end[2]+1):
                                    for zz in range(self.start[2],self.end[2]+1):
                                        if z + 1 == zz:
                                            return True

        return False

def part1(snapshot):
    
    Q = []

    for n, coords in enumerate(snapshot):
        br = Brick(n, coords)
        heapq.heappush(Q, (br.min_h, random.random(), br))
    
    resting = []
    falling = []

    while len(Q)>0:
        h, r, br = heapq.heappop(Q)
        if h == 1:
            br.resting = True
        else :
            for _,_,rbr in resting:
                if br.rests_on(rbr):
                    rbr.supporting.add(br)
                    br.resting = True
                    br.supported.add(rbr)
        if br.resting:
            heapq.heappush(resting, (-br.min_h, r, br)) 
        else : 
            heapq.heappush(falling, (br.min_h, r, br))
    
    while len(falling) > 0:
        h,r,br = heapq.heappop(falling)
        br.fall1()

        if h-1  == 1:
            br.resting = True
        else :
            for _,_,rbr in resting:
                if br.rests_on(rbr):
                    rbr.supporting.add(br)
                    br.resting = True
                    br.supported.add(rbr)
                    break
        if br.resting:
            heapq.heappush(resting, (-br.min_h, r, br)) 
        else : 
            heapq.heappush(falling, (br.min_h, r, br))
    
    all_bricks = resting.copy()    

    while len(all_bricks)>0:
        _,_,br = heapq.heappop(all_bricks)

        for _,_,rbr in resting:
            if br is rbr:
                continue
            if br.rests_on(rbr):
                rbr.supporting.add(br)
                br.supported.add(rbr)

    ans1 = 0
    for _,_,br in resting:
        j = 1
        for sbr in br.supporting:
            if len(sbr.supported) == 1:
                j = 0
        br.safe_disint = j
        ans1 += j

    return ans1, resting


def part2(all_bricks):
    ans2 = 0
    while len(all_bricks)>0:
        _,_,br = heapq.heappop(all_bricks)

        if br.safe_disint:
            continue
        else :
            falling = set()
            falling.add(br)
           
            cands = []
            
            for sbr in br.supporting:
                heapq.heappush(cands, (sbr.min_h, random.random(), sbr))

            while len(cands)>0:
                _,_,cand = heapq.heappop(cands)

                if len(cand.supported.difference(falling)) == 0:
                    falling.add(cand)
                    for sbr in cand.supporting:
                        heapq.heappush(cands, (sbr.min_h, random.random(), sbr))

            ans2 += len(falling) - 1

    return ans2

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input2.txt')
    
    snapshot = parsing(data)

    # Part I    

    ans1, resting = part1(snapshot)

    print(f'Answer to part 1: {ans1}')

    # Part II

    ans2 = part2(resting.copy())
    
    print(f'Answer to part 2: {ans2}')
