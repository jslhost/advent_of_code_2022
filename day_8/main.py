if __name__ == '__main__':
    import numpy as np
    import pandas as pd

    with open('input.txt') as file:
        data = file.read().splitlines()

    forest = np.array([[int(tree) for tree in row] for row in data])
    df = pd.DataFrame(data=forest)

    # Part 1 ---------------------------------------------------------------
    nb_bordures = (df.shape[0]-1) * 4
    visible_tree_count = 0

    for col in range(1, 98):
        for row in range(1, 98):

            list_of_directions = [
                df.iloc[0:row, col], 
                df.iloc[row+1:None, col][::-1], 
                df.iloc[row, 0:col], 
                df.iloc[row, col+1:None][::-1]
                ]
            target_tree = df.iloc[row, col]
            visible_tree_angle = 0

            for direction in list_of_directions:
                tree_is_visible = True
                for tree in direction:
                    if tree >= target_tree:
                        tree_is_visible = False
                        break
                if tree_is_visible:
                    visible_tree_angle += 1

            if visible_tree_angle > 0:
                visible_tree_count += 1

    print(visible_tree_count + nb_bordures)

    # Part 2 ---------------------------------------------------------------
    list_score_total = []
    for col in range(0, 99):
        for row in range(0, 99):

            list_of_directions = [
                df.iloc[0:row, col][::-1], 
                df.iloc[row+1:None, col], 
                df.iloc[row, 0:col][::-1], 
                df.iloc[row, col+1:None]
                ]
            target_tree = df.iloc[row, col]
            list_score = []

            for direction in list_of_directions:
                visible_tree_angle = 0
                for tree in direction:
                    visible_tree_angle += 1
                    if tree >= target_tree:
                        break
                list_score.append(visible_tree_angle)
            
            prod = np.prod(list_score)
            list_score_total.append(prod)

    print(np.max(list_score_total))