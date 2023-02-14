def load_data():
    with open('input.txt') as file:
        return file.read()

def find_marker(data, char_length):
    for i in range(len(data) - char_length):
        marker = data[i : i+char_length]
        if len(set(marker)) == char_length:
            start_of_packet = i+char_length
            break
    return start_of_packet

def main(char_length):
    data = load_data()
    start_of_packet = find_marker(data, char_length)
    return start_of_packet

if __name__ == '__main__':
    print(main(4))
    print(main(14))