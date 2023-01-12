if __name__ == "__main__":
    # Part 1 -----------------------------------------------------------  
    with open('input.txt') as file:
        data = file.read()
    rucksacks = data.split('\n')[0:-1]

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = {letter : value for letter, value in zip(alphabet, range(1, len(alphabet)+1))}
    score_total = 0

    for rucksack in rucksacks:
        length = int(len(rucksack)/2)
        first_half = rucksack[0:length]
        second_half = rucksack[length:None]

        for letter in first_half:
            if letter in second_half:
                error = letter

        score = priorities[error]
        score_total = score_total + score

    print(score_total)

    # Part 2 -----------------------------------------------------------  
    with open('input.txt') as file:
        data = file.read()
    rucksacks = data.split('\n')[0:-1]

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = {letter : value for letter, value in zip(alphabet, range(1, len(alphabet)+1))}
    score_total = 0
    departure, end = 0, 3

    for i in range(len(rucksacks)//3):
        team = rucksacks[departure:end]

        for letter in team[0]:
            if letter in team[1] and letter in team[2]:
                error = letter

        score = priorities[error]
        score_total = score_total + score
        departure += 3
        end += 3

    print(score_total)