import random

def generate_pairings(n):
    selectedNums = []
    pairs = []

    for i in range(int(n/2)):
        num1 = random.randint(0, n)
        while num1 in selectedNums:
            num1 = random.randint(0, n)
        selectedNums.append(num1)

        num2 = random.randint(0, n)
        while num2 in selectedNums:
            num2 = random.randint(0, n)
        selectedNums.append(num2)

        newPair = (num1, num2)
        pairs.append(newPair)

    return pairs

if __name__ == '__main__':
    f = open('abstract_pairings_16.txt', 'w')
    pairs = generate_pairings(16)
    f.write(str(pairs))
    f.close()
    print(pairs)
