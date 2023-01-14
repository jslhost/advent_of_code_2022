if __name__ == "__main__":
    # Part 1 -----------------------------------------------------------  
    import pandas as pd

    with open('input.txt') as file:
        data = file.read()

    pairs = data.split('\n')[0:-1]
    pairs = [pair.split(',') for pair in pairs]
    df = pd.DataFrame(data=pairs, columns=['elf_1', 'elf_2'])

    def create_range(raw):
        range_liste = [int(range_value) for range_value in raw.split('-')]
        range_liste = [i for i in range(range_liste[0], range_liste[1]+1)]
        return range_liste

    for col in df:
        df[col] = df[col].apply(create_range)

    counter = 0
    for idx in df.index:
        if all(item in df.iloc[idx][0] for item in df.iloc[idx][1]):
            counter += 1
        elif all(item in df.iloc[idx][1] for item in df.iloc[idx][0]):
            counter += 1
    print(counter)

    # Part 2 -----------------------------------------------------------  
    counter = 0
    for idx in df.index:
        for num_range in df.iloc[idx][0]:
            if num_range in df.iloc[idx][1]:
                counter += 1
                break
    print(counter)