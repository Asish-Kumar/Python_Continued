import string


def word_counter(line: list) -> dict:
    word_count = dict()
    for word in line:
        try:
            word_count[word] += 1
        except KeyError:
            word_count[word] = 1
    return word_count


def main():
    file_name = input("Enter the full file name: ")
    with open(file_name, 'r+') as file:
        read_lines = file.readlines()
        # remove /n character from end of each line
        lines = []
        for line in read_lines:
            punctuations = set(string.punctuation)
            line = ''.join(ch.lower() for ch in line if ch not in punctuations)
            # print(line)
            lines.extend(line.split())
        # print(lines)
        word_dict = word_counter(lines)
        # print(word_dict)
        word_dict_list = []
        for key,value in zip(word_dict.keys(),word_dict.values()):
            word_dict_list.append((key,value))
        # print(word_dict_list)
        temp_sorted = sorted(word_dict_list, key=lambda k: k[0], reverse=False)
        final_sorted = sorted(temp_sorted, key=lambda k:k[1], reverse=True)
        # print(final_sorted)
        final_sorted_list = []
        for x in final_sorted:
            final_sorted_list.append(x[0])
        # print(final_sorted_list)
        # assumed: there are more than 9 elements in the final_sorted_list
        print(final_sorted_list[:10])  # printing first 10 of sorted list
        print(final_sorted_list[-10:])  # printing last 10 of sorted list


if __name__ == '__main__':
    main()


