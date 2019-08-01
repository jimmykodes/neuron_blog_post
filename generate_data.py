import json
import random


def generate_data(length):
    data = {
        'X': [],
        'y': []
    }
    for _ in range(length):
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        label = -1 if x > y else 1
        data['X'].append([x, y])
        data['y'].append(label)
    return data


def main():
    data = generate_data(500)
    with open('data.json', 'w+') as f:
        f.write(json.dumps(data))

if __name__ == '__main__':
    main()
