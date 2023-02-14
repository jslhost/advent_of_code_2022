if __name__ == '__main__':
    # Part 1 -------------------------------------------------------------------------------
    import pandas as pd
    import re

    # Open the file
    with open('input.txt') as file:
        data = file.read()

    # Playground formatting
    schema = data.split('\n')[0:9]
    rows = [row.split(' ') for row in schema][0:-1]
    for row in rows:
        idx = 0
        while True:
            try:
                if row[idx] == '':
                    del row[idx:idx+3]
                idx += 1
            except:
                break
    array = pd.DataFrame(data=rows).T.to_numpy()
    playground = array.tolist()

    # Instructions formatting
    instructions = data.split('\n')[10:-1]
    instructions_clear = []
    for instruction in instructions:
        instruction = [int(s) for s in re.findall(r'\b\d+\b', instruction)]
        instructions_clear.append(instruction)

    # Crane work
    for instruction in instructions_clear:
        for i in range(instruction[0]):
            for idx, space in enumerate(playground[instruction[1]-1]):
                if space:
                    crate_to_move = space # Selecting the crate to move
                    playground[instruction[1]-1][idx] = '' # Removing the crate
                    break
            for idx, space in enumerate(playground[instruction[2]-1]):
                if space:
                    if idx == 0: # Adding a new space in the pile if necessary
                        playground[instruction[2]-1].insert(0, crate_to_move) # Deposit the crate
                        break
                    else:
                        real_index = idx - 1
                        playground[instruction[2]-1][real_index] = crate_to_move # Deposit the crate
                        break
            if not any(playground[instruction[2]-1]):
                playground[instruction[2]-1][-1] = crate_to_move # Deposit the crate if the pile is empty

    answer = "".join(["".join(row)[1:2] for row in playground])
    print(answer)

    # Part 2 -------------------------------------------------------------------------------
    playground = array.tolist()
    # Crane work
    for instruction in instructions_clear:
        nb_crate = instruction[0]
        for idx, space in enumerate(playground[instruction[1]-1]):
            if space:
                crate_to_move = playground[instruction[1]-1][idx : idx+nb_crate] # Selecting the crate to move
                playground[instruction[1]-1][idx: idx+nb_crate] = ["" for i in range(nb_crate)] # Removing the crate
                break
        for idx, space in enumerate(playground[instruction[2]-1]):
            if space:
                for crate in crate_to_move[::-1]:
                    playground[instruction[2]-1].insert(idx, crate) # Deposit the crate
                break
        if not any(playground[instruction[2]-1]):
            playground[instruction[2]-1][-nb_crate:None] = crate_to_move # Deposit the crate if the pile is empty

    answer = "".join(["".join(row)[1:2] for row in playground])
    print(answer)