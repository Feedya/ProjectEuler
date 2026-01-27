import math

def see_if_triplet(a, b, c):
    a_square = a ** 2
    b_square = b ** 2
    c_square = c ** 2
    if (a_square + b_square == c_square):
        return True
    return False

#a < b < c
def main():
    a = 0
    b = 1
    while (b != 500):
        a = 0
        while (a != b):
            c = 1000 - a - b
            if (c < a or c < b):
                a += 1
                continue
            elif (see_if_triplet(a, b, 1000 - a - b) == True):
                print(f"Result : a = {a}, b = {b}, c = {c}")
                print(f"Result to give {a * b * c}")
                return
            a += 1
        b += 1

if __name__ == "__main__":
    main()