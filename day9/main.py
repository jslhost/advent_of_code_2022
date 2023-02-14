if __name__ == '__main__':

    import numpy as np
    import re

    with open('input.txt') as file:
        data = file.read().splitlines()

    def compute_distance(head_coordinates, tail_coordinates):
        return np.sqrt((tail_coordinates[0] - head_coordinates[0])**2 + (tail_coordinates[1] - head_coordinates[1])**2)    

    commands = {'U' : [1, 1], 'D' : [1, -1], 'R' : [0, 1], 'L' : [0, -1]}
    log = []
    head_coordinates = [0, 0]
    tail_coordinates = [0, 0]

    for instruction in data:
        direction = instruction[0]
        step = int(re.findall(r'\b\d+\b', instruction)[0])
        for i in range(step):
            select_coordinate = commands[direction][0]
            head_coordinates_copy = head_coordinates.copy()
            head_coordinates[select_coordinate] += commands[direction][1]
            distance = compute_distance(head_coordinates, tail_coordinates)
            if distance >= 2:
                tail_coordinates = head_coordinates_copy
            log.append(tuple(tail_coordinates))

    print(len(set(log)))
