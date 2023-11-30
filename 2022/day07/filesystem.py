""" Advent of Code 2022 -- Day 07 -- """

import aoc

class File:
    def __init__(self, size, name, wd):
        self.name = name
        self.size = size
        self.directory = wd

    def __str__(self):
        s = 2*self.directory.depth*' '+ '  - ' + self.name
        s += f' (file, size = {self.size})\n'
        return s

class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        if parent is None:
            self.depth = 0
        else :
            self.depth = parent.depth + 1
        self.files = [] 
        self.subdir = []

    def __str__(self):
        s = 2*self.depth*' '+ '- ' + self.name
        s += f' (dir, size = {self.size()})\n'        
        for sdir in self.subdir:
            s += f'{sdir}'
        for file in self.files:
            s += f'{file}'
        return s

    def size(self):
        totsize = 0
        for f in self.files:
            totsize += f.size

        for d in self.subdir:
            totsize += d.size()

        return totsize

    def addfile(self, file):
        self.files.append(file)

    def addsubdir(self, sdir):
        self.subdir.append(sdir)

    def cd(self, cmd):
        if cmd == '..':
            return self.parent
        else :
            for d in self.subdir:
                if d.name == cmd:
                    return d

def part1(working_dir, threshold=100000):
    sizes = 0
    for sdir in working_dir.subdir:
        sizes += part1(sdir, threshold)

    s = working_dir.size() 
    if s <= threshold:
        sizes += s

    return sizes

def part2(working_dir, min2del):
    
    sizes = []

    for sdir in working_dir.subdir:
        sizes.extend(part2(sdir, min2del))
    
    size = working_dir.size()

    if size > min2del:
        sizes.append(size)

    return sizes


if __name__ == '__main__':
    data = aoc.get_input('input.txt')

    root = Dir('/')

    for n, line in enumerate(data.splitlines()):

        if line == '$ cd /':
            # only for first line of input to build root
            working_dir = root
            continue
        
        if line == '$ ls':
            # skipping
            continue
        
        if line[0] != '$':
            # process output of ls
            words = line.split()
            if words[0] == 'dir':
                # add new subdirectory
                sdir = Dir(words[1], working_dir)
                working_dir.addsubdir(sdir)
            else :
                newfile = File(int(words[0]), words[1], working_dir)
                working_dir.addfile(newfile)
            continue
        
        if line.startswith('$ cd '):
            words = line.split()
            working_dir = working_dir.cd(words[-1])

    print(root)
    threshold = 100000
    sizes = part1(root, threshold)
    print(f'Part I : The sum of the total sizes is {sizes}')
    
    # Part II:
    required = 30000000
    used = root.size()
    capacity = 70000000
    free = capacity - used
    min2del = required - free

    s = part2(root, min2del)
    print(f'Part II: The total size of the directory is {min(s)}')
