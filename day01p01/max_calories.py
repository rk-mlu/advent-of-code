import numpy as np

# read input
with open('input', 'r') as file:
    data = file.read()

# split at every empty line (= two new lines)
split_data = data.split('\n\n')

max_i = 0
max_cal = 0

# for part 2:
max_i_list = [0, 0, 0]
max_cal_list = [0, 0, 0]

for n, cal_list in enumerate(split_data, start=1):
    # extract list of calories of n-th Elf  
    cal_array = np.fromstring(cal_list, dtype=int, sep='\n')
    # total amount of calories of n-th Elf
    cal_sum = np.sum(cal_array)
    
    # determine Elf with most calories
    if max_cal < cal_sum:
        max_i = n
        max_cal = cal_sum

        max_i_list.pop()
        max_i_list.insert(0, n)

        max_cal_list.pop()
        max_cal_list.insert(0, cal_sum)
    
    print(f'{n}: {cal_sum}')

# solution to part 1:
print(f'Elf {max_i} carries with {max_cal} most calories of all!')

# solution to part 2:
print(f'The top three elves carry {max_cal_list} calories.')
print(f'In total they carry {np.sum(max_cal_list)} calories.')
