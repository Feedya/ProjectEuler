import math

def is_prime(number):
    root = int(math.sqrt(number))
    i = 3
    if (number < 2):
        return (False)
    if (number == 2):
        return (True)
    if (number % 2 == 0):
        return (False)
    for i in range (3, root + 1, 2):
        if (number % i == 0):
            return (False)
    return (True)

def find_prime(prime_place):
    counter = 0
    i = 0
    while (1):
        if (counter == 10001):
            break
        i += 1
        if (is_prime(i) == True):
            counter += 1
    return (i)

def main():
    premier = find_prime(10001)
    print(f"result : {premier}")

if __name__ == "__main__":
    main()