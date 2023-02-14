if __name__ == "__main__":
    # Part 1 ---------------------------------------- 
    import pandas as pd

    with open('input.txt') as file:
        data = file.read()

    data_liste = data.split('\n')
    df = pd.DataFrame(data_liste, columns=['calories'])
    hole_index = df.loc[df['calories']==""].index

    base_index = 0
    calories_sum_list = []

    for idx in hole_index:
        elf_carrying = df.iloc[base_index:idx].astype("int")
        calories_sum = elf_carrying.sum().values[0]
        calories_sum_list.append(calories_sum)
        base_index = idx + 1

    print(max(calories_sum_list))

    # Part 2 ---------------------------------------- 
    import numpy as np
    sum_top_3 = np.sum(sorted(calories_sum_list)[-3:])
    print(sum_top_3)
