import math

#n to n / 2 (n is even)
#n to 3n + 1 (n is odd)

def do_iterative_sequence(nombre):
    counter = 0
    while (nombre != 1):
        if (nombre % 2 == 0):
            nombre = nombre / 2
        else:
            nombre = (nombre * 3) + 1
        counter += 1
    return (counter)

def longest_iterative_sequence(limit):
    counter = 0
    i = 2
    biggest = 0
    biggest_nombre = 0
    while (i != limit):
        counter = do_iterative_sequence(i)
        if (counter > biggest):
            biggest = counter
            biggest_nombre = i
        i += 1
    print(f"iteration : {counter}")
    return (biggest_nombre)
    
def main():
    result = longest_iterative_sequence(1000000)
    print(f"result : {result}")

if __name__ == "__main__":
    main()