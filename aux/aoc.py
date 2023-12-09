""" Advent of Code 2021-2023  -- Helper functions """
import os.path

def dl_data(day, year, fname="input1.txt"):

    if not os.path.isfile(fname):
        from aocd import get_data
        
        data = get_data(day=day, year=year)
        
        with open(fname, "w") as file:
            file.write(data)
    else :
        data = get_input(fname)

    return data
    
def get_input(fname='input1.txt'):
    """ read input file and return it as string """

    with open(fname, 'r') as file:
        data = file.read()

    return data
