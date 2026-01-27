import math

def is_prime(number):
    if (number < 2):
        return False
    if (number == 2):
        return (True)
    if (number % 2 == 0):
        return False
    square = int(math.sqrt(number))
    for i in range(3, square + 1, 2):
        if (number % i == 0):
            return False
    return True

#we put counter to two because
#we will miss the 2 as a prime number
#in the for boucle
def count_sum_all_prime_numbers(limit):
    counter = 2
    for i in range(1, limit + 1, 2):
        if (is_prime(i) == True):
            counter += i
    return (counter)

def main():
    result = count_sum_all_prime_numbers(2000000)
    print(f"Result : {result}")
    
    
if __name__ == "__main__":
    main()