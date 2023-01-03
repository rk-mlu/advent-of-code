""" Advent of Code 2022 -- Day 15 -- """

import aoc
import numpy as np

def parsing(data):
    lines = data.splitlines()
    
    sensors = []
    beacons = []
    
    for line in lines:
        words = line.split()
        sens_x = words[2]
        sens_x = int(sens_x[2:-1])
        sens_y = words[3]
        sens_y = int(sens_y[2:-1])
        sensors.append([sens_x, sens_y])

        beac_x = words[-2]
        beac_x = int(beac_x[2:-1])
        beac_y = words[-1]
        beac_y = int(beac_y[2:])
        beacons.append((beac_x, beac_y))

    return sensors, beacons

def cmp_radius(sens, beac):
    return abs(sens[0] - beac[0]) + abs(sens[1] - beac[1])

def dist2sens(z, sens):
    s = np.array(sens, dtype=int)
    s_mat = np.outer(np.ones(z.shape[0], dtype=int), s)
    d = np.array(np.linalg.norm(s_mat - z, ord=1, axis=1), dtype=int)
    return d

if __name__ == '__main__':
    data, y, le, b = aoc.get_input('input.txt'), 2000000, 10000000, 4000001
    # data, y, le, b = aoc.get_input('input2.txt'), 10, 100, 21
    
    # Part I    
    sensors, beacons = parsing(data)
    radii = []
    for sens, beac in zip(sensors, beacons):
        radii.append(cmp_radius(sens, beac))
        # if beac[1] == y:
        #     print(beac[0], beac[1])
    radii = np.array(radii)
    num_beac_in_y = 1
    
    z = np.ones( (le, 2), dtype=int)
    z[:, 1] = y
    z[:, 0] = np.arange(-le//2, le//2) 
    
    res = np.zeros(le, dtype=int)
    for sens, r in zip(sensors, radii):
        d = dist2sens(z, sens)
        l = np.array(d <= r)
        res += l
    res = np.array(res > 0, dtype=int)

    print(f'Part I: Number of covered position is {np.sum(res) - num_beac_in_y}')
    
    # Part II
    
    for sens, r in zip(sensors, radii):
        # it is enough to use z1 if uncovered pos is SE of one sensor
        z1 = np.zeros( (r+2, 2), dtype=int)
        z1[:, 0] = sens[0] + np.arange(r+2)
        z1[:, 1] = sens[1] + r + 1 - np.arange(r+2)

        ## may be needed for other input:
        # z2 = np.zeros( (r+2, 2), dtype=int)
        # z2[:, 0] = sens[0] - (r + 1) + np.arange(r+2)
        # z2[:, 1] = sens[1] - np.arange(r+2)
        # z1 = z2
        
        res = np.ones(r+2, dtype=int)
        
        for sens2, r2 in zip(sensors, radii):
            d = dist2sens(z1, sens2)
            inside = np.array(z1[:,0] < b) * np.array(z1[:,1] < b)
            inside = inside * np.array(z1[:,0] >= 0) * np.array(z1[:,1] >= 0)
            l = np.array(d > r2) * inside
            res = res*l
        
        if np.amax(res) == 1:
            k = np.argmax(res)
            xx = sens[0] + k
            yy = sens[1] + r + 1 - k

            ## needed for z2
            # xx = sens[0] - (r+1) + k
            # yy = sens[1] - k
            break

    tunfreq = 4000000*xx + yy
    print(f'Part II: Coordinate of beacon is {xx, yy}')
    print(f'Part II: Tuning frequency is {tunfreq}')
