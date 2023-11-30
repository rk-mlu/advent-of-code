""" Advent of Code 2022 -- Day 04 -- """

def parse_ranges(data):
    list_pairs = []
    for line in data.splitlines():
        ranges = line.split(',')
        pair = []
        for r in ranges:
            rr = r.split('-')
            pair.append([int(rr[0]), int(rr[1])])
        list_pairs.append(pair.copy())
    return list_pairs

def check_ranges(pair):
    # check if one range is contained in the other
   
    # determine range length
    l = []
    for r in pair:
        l.append(r[1] - r[0])
    
    if l[0] >= l[1]:
        s = 0
    else :
        s = 1

    if pair[s][0] > pair[(s+1)%2][0] or pair[s][1] < pair[(s+1)%2][1]:
        return 0
    else :
        return 1
    
def check_overlap(pair):
    # check if one range overlaps with the other
   
    if pair[0][0] > pair[1][1] or pair[0][1] < pair[1][0]:
        return 0
    else :
        return 1

if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        data = file.read()

    pl = parse_ranges(data)
    s = 0
    s2 = 0
    for j, pair in enumerate(pl):
        m = check_ranges(pair)
        s += m
        n = check_overlap(pair)
        s2 += n
        print(j, pair, m, n)
    print(f'Part 1: the sum of contained ranges is {s}')
    print(f'Part 2: the sum of overlapping ranges is {s2}')


