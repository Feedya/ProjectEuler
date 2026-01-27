import math

def read_file(file_name):
    try:
        with open(file_name, "r") as file_handler:
            string = file_handler.read()
    except FileNotFoundError:
        print("name of file is false retry with a differenet name")
        exit(0)
    string = string.replace("\n", "")
    string = string.replace(" ", "")
    return (string)

def count_sum_of_multipl(string, start, end):
    result = 1
    while (start != end):
        i = int(string[start])
        result = result * i
        start += 1
    return (result)


def greatest_product(string, taille):
    start = 0
    end = 13
    biggest = 0
    for i in range(0, len(string), 1):
        result = count_sum_of_multipl(string, start, end)
        if (biggest < result):
            biggest = result        
        start += 1
        end += 1
        if (end == len(string) + 1):
            break
    return (biggest)

def main():
    string = read_file("numbers.txt")
    biggest = greatest_product(string, 13)
    print(f"result : {biggest}")
    
    
if __name__ == "__main__":
    main()