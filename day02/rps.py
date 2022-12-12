"""
Advent of Code 2022
Day 02
"""

def score(strategy):
    """ calculating scores for part 1 """

    # read choices
    strats = strategy.split()
    
    opp = {}
    opp['A'] = 1
    opp['B'] = 2
    opp['C'] = 3
    opp_strat = opp[strats[0]]
    
    my = {}
    my['X'] = 1
    my['Y'] = 2
    my['Z'] = 3
    my_strat = my[strats[-1]]
    
    # points for choice of strategy
    pts = my_strat

    # determine outcome of round
    if  my_strat - opp_strat == 0:
        # it is a draw
        pts += 3
    if my_strat - opp_strat % 3 == 1:
        # it is a win
        pts += 6

    return pts

def score2(strategy):
    """ calculating scores for part 2 """

    # read choices
    strats = strategy.split()
    
    strat = {}
    strat['A'] = 1
    strat['B'] = 2
    strat['C'] = 3
    opp_strat = strat[strats[0]]
    
    outc = {}
    outc['X'] = -1
    outc['Y'] = 0
    outc['Z'] = 1
    outcome = outc[strats[-1]]
    
    # points for choice of outcome of round
    pts = (outcome + 1)*3

    # add points for my strat
    pts += (opp_strat - 1 + outcome) % 3 + 1

    return pts

if __name__ == '__main__':
    # read input
    with open('input.txt', 'r') as file:
        data = file.read()

    total_score = 0
    total_score2 = 0
    
    for line in data.splitlines():
        pts = score(line)
        pts2 = score2(line)
        total_score += pts
        total_score2 += pts2
        print(line.split(), pts, pts2)
    
    print(f'Part 1: Total score is {total_score}')
    print(f'Part 2: Total score is {total_score2}')
