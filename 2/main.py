if __name__ == "__main__":
    # Part 1 ----------------------------------------     
    import pandas as pd
    df = pd.read_csv("input.txt", sep=" ", header=None)

    opponent_shape = {'A' : 1, 'B' : 2, 'C' : 3}
    my_shape = {'X' : 1, 'Y' : 2, 'Z' : 3}
    conclusion = {'lost' : 0, 'draw' : 3, 'win' : 6}
    losing = [1, -2]
    winning = [-1, 2]
    score = 0

    for idx in df.index:
        diff_score = opponent_shape[df.iloc[idx,0]] - my_shape[df.iloc[idx,1]]

        if diff_score in losing:
            score += conclusion['lost'] + my_shape[df.iloc[idx,1]]
        elif diff_score in winning:
            score += conclusion['win'] + my_shape[df.iloc[idx,1]]
        else:
            score += conclusion['draw'] + my_shape[df.iloc[idx,1]]

    print(score)

    # Part 2 ---------------------------------------- 
    import pandas as pd
    df = pd.read_csv("input.txt", sep=" ", header=None)

    opponent_shape = {'A' : 1, 'B' : 2, 'C' : 3}
    conclusion = {'lost' : 0, 'draw' : 3, 'win' : 6}
    losing = [1, -2]
    winning = [-1, 2]
    shape = [1, 2, 3]
    score= 0

    for idx in df.index:
            if df.iloc[idx,1] == 'X': #lost
                    for score_shape in shape:
                            diff = opponent_shape[df.iloc[idx,0]] - score_shape
                            if  diff in losing:
                                    score += conclusion['lost'] + score_shape
            elif df.iloc[idx,1] == 'Y': # draw
                    score += conclusion['draw'] + opponent_shape[df.iloc[idx,0]]
            elif df.iloc[idx,1] == 'Z': # win
                    for score_shape in shape:
                            diff = opponent_shape[df.iloc[idx,0]] - score_shape
                            if  diff in winning:
                                    score += conclusion['win'] + score_shape

    print(score)