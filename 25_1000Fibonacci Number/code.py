import math

def count_length(fibb, length):
    taille = len(str(fibb))
    if (taille >= length):
        return (1)
    return (0)

def find_fibonacci_length(length):
    n = 1
    i = 2
    fibb = 0
    index = 3
    while (1):
        fibb = i + n
        index += 1
        n = i
        i = fibb
        if (count_length(fibb, length) == 1):
            break
    return (index)

def main():
    result = find_fibonacci_length(1000)
    print(f"result : {result}")

if __name__ == "__main__":
    main()