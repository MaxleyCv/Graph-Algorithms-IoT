INPUT_FILE = open("career.in")
OUTPUT_FILE = open("career.out")


def get_input():
    result = []
    income = INPUT_FILE.readlines()
    for i in range(len(income)):
        income[i] = str.replace(income[i], '\n', '')
    length = int(income.pop(0))
    for i in range(length):
        result.append(list(map(int, income[i].split(' '))))
    return result


def get_max_career(items):
    print(items)
    indexes = range(1, len(items))
    indexes = reversed(indexes)
    for i in indexes:
        print(items[i])
        for new_index in range(len(items[i]) - 1):
            items[i - 1][new_index] += max(items[i][new_index], items[i][new_index + 1])
    return items[0][0]


print(get_max_career(get_input()))