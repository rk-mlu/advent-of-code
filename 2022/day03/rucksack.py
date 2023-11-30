""" Advent of Code 2022 -- Day 03 """

def prio(c):
    # get ascii code for char
    p = ord(c)
    # return correct priority for item
    if p > 96:
        p -= 96
    else :
        p += 26 -64

    return p 

def content(s):
    num_items = len(s)
    compart1 = s[:num_items//2]
    compart2 = s[num_items//2:]
    return num_items, compart1, compart2

def compare(comp1, comp2):
    # check if two strings contain the same character
    for c in comp1:
        ind = comp2.find(c)
        if ind != -1:
            return c

def grouping(data):
    # create groups out of list of rucksacks
    groups = []
    group = []
    for n, line in enumerate(data.splitlines()):
        group.append(line)
        if (n + 1) % 3 == 0:
            groups.append(group.copy())
            group = []
    return groups

def find_badge(r1, r2, r3):
    # find badge
    for c in r1:
        ind2 = r2.find(c)
        if ind2 != -1:
            ind3 = r3.find(c)
            if ind3 != -1:
                return c

if __name__ == '__main__':
    # read input
    with open('input.txt', 'r') as file:
        data = file.read()

    total_prio = 0
    for line in data.splitlines():
        num_items, comp1, comp2 = content(line)
        c = compare(comp1, comp2)
        total_prio += prio(c)
        print(num_items, comp1, comp2, c, prio(c))

    print(f'Part I: Total priority is {total_prio}.')

    grps = grouping(data)
    total_prio2 = 0
    for n, group in enumerate(grps):
        badge = find_badge(group[0], group[1], group[2])
        total_prio2 += prio(badge)
        print(n, badge, prio(badge))
    
    print(f'Part II: Total priority is {total_prio2}.')
