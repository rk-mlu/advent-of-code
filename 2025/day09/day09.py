""" Advent of Code 2025 -- Day 9 -- """
year = 2025
day = 9         # set day!

import sys
sys.path.append('../../aux')
import aoc
from itertools import combinations

def parsing(data):
    # parser for the input data    
    lines = data.splitlines()
    
    coords = []

    for line in lines:
        nums = [int(c) for c in line.split(',')]
        coords.append(tuple(nums))

    return coords

class Polyg:
    def __init__(self, vertices):
        self.vertices = vertices
        self.num_vertices = len(vertices)

    def _check_collinear_and_in_box(self, p1, p2, p_test):
        x1, y1 = p1
        x2, y2 = p2
        p_x, p_y = p_test

        cross_product = (p_y - y1) * (x2 - x1) - (p_x - x1) * (y2 - y1)
        
        if cross_product != 0:
            # p2-p1 and p_test-p1 do not lie on the same line
            return False

        is_x_between = (min(x1, x2) <= p_x <= max(x1, x2))
        is_y_between = (min(y1, y2) <= p_y <= max(y1, y2))
        
        return is_x_between and is_y_between

    def is_on_edge(self, p_test):
        if p_test in self.vertices:
            return True
            
        for i in range(self.num_vertices):
            p1 = self.vertices[i]
            p2 = self.vertices[i-1] 
            if self._check_collinear_and_in_box(p1, p2, p_test):
                return True
        return False

    def is_inside(self, p, include_edges=True):
        """
        Check if point p lies inside the polygon.
        """

        if include_edges and self.is_on_edge(p):
            return True
        
        crossings = 0
        p_x, p_y = p[0], p[1]

        for i in range(self.num_vertices):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[i-1]

            if (y1 <= p_y < y2) or (y2 <= p_y < y1):
                
                if y1 != y2:
                    numerator = (p_y - y1) * (x2 - x1) 
                    denominator = (y2 - y1)

                    if denominator > 0:
                        if numerator > (p_x - x1) * denominator:
                            crossings += 1
                    else: 
                        if numerator < (p_x - x1) * denominator:
                            crossings += 1
        # odd number of crossings => inside
        return crossings % 2 == 1

if __name__ == '__main__':
    data = aoc.dl_data(day, year, 'input1.txt')                                  
    # data = aoc.get_input('input0.txt')
    
    coords = parsing(data)

    # Part I

    max_area = 0

    for coord1, coord2 in combinations(coords, 2):
        h = abs(coord1[0] - coord2[0]) + 1
        w = abs(coord1[1] - coord2[1]) + 1
        area = h*w
        max_area = max(max_area, area)

    ans1 = max_area

    print(f'Answer to part 1: {ans1}')

    # Part II

    P = Polyg(coords)
    
    ans2 = 0
    
    for coord1, coord2 in combinations(coords, 2):

        corners = [coord1, (coord1[0], coord2[1]),
                   coord2, (coord2[0], coord1[1])]
        h = abs(coord1[0] - coord2[0]) + 1
        w = abs(coord1[1] - coord2[1]) + 1
        area = h*w
        if ans2 > area:
            continue
        
        mid = ((coord1[0] + coord2[0])//2, (coord1[1] + coord2[1])//2)
        # print(coord1, coord2, area, mid)

        if not P.is_inside(mid):
            continue
        if not P.is_inside(corners[1]):
            continue
        if not P.is_inside(corners[3]):
            continue
        
        for coord3 in coords:
            inner_vertex = min(coord1[0], coord2[0]) < coord3[0] < max(coord1[0], coord2[0])
            inner_vertex &= min(coord1[1], coord2[1]) < coord3[1] < max(coord1[1], coord2[1])
            # print(inner_vertex, coord3)
            if inner_vertex:
                break

        if inner_vertex:
            continue

        for j in range(len(coords)):
            x1, y1 = coords[j-1]
            x2, y2 = coords[j]
            
            if x1 == x2:
                intersect = min(coord1[0], coord2[0]) < x1 < max(coord1[0], coord2[0])
                intersect &= min(y1, y2) <= min(coord1[1], coord2[1])
                intersect &= max(y1, y2) >= max(coord1[1], coord2[1])
            else :
                intersect = min(coord1[1], coord2[1]) < y1 < max(coord1[1], coord2[1])
                intersect &= min(x1, x2) <= min(coord1[0], coord2[0])
                intersect &= max(x1, x2) >= max(coord1[0], coord2[0])

            if intersect:
                break

            # print(x1,y1)


        if intersect:
            continue
        else :
            print(corners, area)
            ans2 = max(area, ans2)


    
    print(f'Answer to part 2: {ans2}')
