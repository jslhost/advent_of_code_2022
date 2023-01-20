if __name__ == '__main__':
    from collections import defaultdict
    from itertools import accumulate
    import re
    import numpy as np

    with open('input.txt') as file:
        data = file.read().splitlines()

    # Part 1 ---------------------------------------------------
    path = []
    sizes = defaultdict(int)

    for cmd_line in data:
        if '$ cd' in cmd_line and not '..' in cmd_line:
            if cmd_line == '$ cd /':
                path.append(cmd_line[5:])
            else:
                path.append(cmd_line[5:] + "/")
        elif '..' in cmd_line:
            path.pop()

        try:
            if type(int(cmd_line[0])) == int:
                file_size = [int(s) for s in re.findall(r'\b\d+\b', cmd_line)][0]
                for file_path in accumulate(path):
                    sizes[file_path] += file_size
        except:
            pass

    values = np.array([value for value in sizes.values()])
    print(np.sum(values[values <= 100_000]))

    # Part 2 ---------------------------------------------------
    space_needed = 30_000_000 - (70_000_000 - sizes['/'])
    print(np.min(values[values >= space_needed]))