def FirstFactorial(num):
    total = 1

    for number in range(1, num + 1):
        total = total * number

    return total


if __name__ == '__main__':
    FirstFactorial(4)
