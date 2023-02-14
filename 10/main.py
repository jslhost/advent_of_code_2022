if __name__ == '__main__':
    import re

    with open('input.txt') as f:
        data = f.read().splitlines()

    # Part 1 ----------------------------------------------------
    i = X = 1
    signal_strength_sum = 0
    callbacks = [20, 60, 100, 140, 180, 220]

    def check_i(i):
        return i*X if i in callbacks else 0

    for instruction in data:
        if 'addx' in instruction:
            value = int(re.findall(r'\b\d+\b', instruction)[0])
            for n in range(2):
                signal_strength_sum += check_i(i)  
                if n == 1:
                    X += -value if '-' in instruction else value
                i += 1
        else:
            signal_strength_sum += check_i(i)        
            i += 1
        if i > 220:
            break
    print(signal_strength_sum)

    # Part 2 ----------------------------------------------------

    def replacer(s, newstring, index):
        return s[:index] + newstring + s[index + 1:]

    i = 0
    X = 1
    row = ' ' * 40

    for instruction in data:
        if 'addx' in instruction:
            value = int(re.findall(r'\b\d+\b', instruction)[0])
            for n in range(2):
                sprite_range = range(X-1, X+2)
                row = replacer(row, '#', i) if i in sprite_range else replacer(row, '.', i)

                if n == 1:
                    X += -value if '-' in instruction else value

                if i == 39:
                    print(row)
                    i = 0
                    row = ' ' * 40
                    continue
                i += 1
        else: 
            sprite_range = range(X-1, X+2)
            row = replacer(row, '#', i) if i in sprite_range else replacer(row, '.', i)

            if i == 39:
                print(row)
                i = 0
                row = ' ' * 40
                continue
            i += 1