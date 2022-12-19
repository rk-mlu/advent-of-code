""" Advent of Code 2022 -- Day 09 -- """

import aoc
import numpy as np

class Rope:
    def __init__(self, num_knots=2):
        self.head = np.zeros(2, dtype=int)
        self.tail = np.zeros(2, dtype=int)
        self.posH = {(0,0)}
        self.posT = {(0,0)}
    
    def move(self, line):
        word = line.split()
        
        num = int(word[1])
        
        for i in range(num):
            self.move_H(word[0])
            self.move_T() 
            self.posH.add((self.head[0], self.head[1]))
            self.posT.add((self.tail[0], self.tail[1]))

        
    def move_H(self, d):
        directions = {}
        directions['R'] = np.array([1,0])
        directions['L'] = np.array([-1,0])
        directions['U'] = np.array([0, 1])
        directions['D'] = np.array([0,-1])

        self.head += directions[d]

    def move_T(self):
        if np.linalg.norm(self.head - self.tail, ord=np.inf) > 1:
            if np.linalg.norm(self.head - self.tail, ord=1) == 2:
                self.tail = self.tail + (self.head - self.tail)//2
            else :
                self.tail = self.tail + (self.head -
                        self.tail)//np.abs(self.head - self.tail)
    
    def update_knot(self, head):
        self.head = head.copy()
        self.move_T()
        self.posT.add((self.tail[0], self.tail[1]))

    def __str__(self):
        s = f'H: {self.head}  T: {self.tail}\n'
        s += f'{len(self.posT)}'
        return s

class Rope2:
    def __init__(self, num_knots=2):
        self.num_knots = num_knots
        self.knots = np.zeros((2, num_knots), dtype=int)
        self.posT = {(0,0)}
    
    def move(self, line):
        word = line.split()
        
        num = int(word[1])
        
        for i in range(num):
            self.move_H(word[0])
            for k in range(1,self.num_knots):
                self.move_knot(k) 
            self.posT.add((self.knots[0,-1], self.knots[1,-1]))

    def move_H(self, d):
        directions = {}
        directions['R'] = np.array([1,0])
        directions['L'] = np.array([-1,0])
        directions['U'] = np.array([0, 1])
        directions['D'] = np.array([0,-1])

        self.knots[:,0] += directions[d]

    def move_knot(self, k):
        dk = self.knots[:,k-1] - self.knots[:,k]
        if np.linalg.norm(dk, ord=np.inf) > 1:
            if np.linalg.norm(dk, ord=1) == 2:
                self.knots[:,k] += dk//2
            else :
                self.knots[:,k] += dk // np.abs(dk)


    def __str__(self):
        s = f'H: {self.knots[:,0]}  T: {self.knots[:,-1]}\n'
        s += f'{len(self.posT)}'
        return s


if __name__ == '__main__':                                                      
    R = Rope()

    data = aoc.get_input('input.txt')
    # data = aoc.get_input('input2.txt')
   
    # Part I
    for line in data.splitlines():
        R.move(line)
    print(R)

    # Part II
    num_knots = 10
    R2 = Rope2(num_knots)
    for line in data.splitlines():
        R2.move(line)
    print(R2)
        

