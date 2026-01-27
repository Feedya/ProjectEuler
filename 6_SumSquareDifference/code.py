import math

def all_square(limit):
    i = 0
    result = 0
    while (i <= limit):
        result += i ** 2
        i += 1
    return result

def sum_square(limit):
    result = 0
    i = 0
    while (i <= limit):
        result += i
        i += 1
    result1 = result ** 2
    return (result1)

def main():
    result_all_square = all_square(100)
    print(f"{result_all_square}")
    result_sum_square = sum_square(100)
    print(f"{result_sum_square}")
    final_result = result_sum_square - result_all_square
    print(f"result : {final_result}")

if __name__ == "__main__":
    main()