""" Advent of Code 2022  -- Helper functions """

def get_input(fname='input.txt'):
    """ read input file and return it as string """
    with open(fname, 'r') as file:
        data = file.read()

    return data
