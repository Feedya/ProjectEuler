import math

def is_abundant(nombre):
    sum = 0
    i = 1
    while (i <= nombre / 2):
        if (nombre  % i == 0):
            sum += i
        i += 1
    if (sum > nombre):
        return True
    return False

def create_abundant_dict(number):
    i = 12
    abundant_dist = {}
    while (i <= number):
        if (is_abundant(i) == True):
            abundant_dist[i] = True
        i += 1
    return abundant_dist

def is_it_abundant(number, abundant_dict):
    i = 0
    c = 0
    while (i <= number):
        c = number - i
        value1 = abundant_dict.get(i)
        if (value1 != None):
            value2 = abundant_dict.get(c)
            if (value2 != None):
                return False
        i += 1
    return True

def count_sum_numbers():
    abundant_dict = create_abundant_dict(28123)
    result = 0
    i = 0
    result = 0
    while (i <= 28123):
        if (is_it_abundant(i, abundant_dict) == True):
            result += i
        i += 1
    return (result)

def main():
    result = count_sum_numbers()
    print(f"result : {result}")

if __name__ == "__main__":
    main()