import math

def est_premier(nombre):
    i = 2
    while (i != nombre):
        if (nombre % i == 0):
            return False
        i += 1
    return True

def check_if_same_restes(restes, divided):
    valeur = restes.get(divided)
    if (valeur == None):
        return (False)
    return (True)

#division euclidienne
def count_repetition(nombre):
    restes = {}
    divided = 10
    i = 0
    while True:
        divided = (divided % nombre) * 10
        if (divided == 0):
            return 0

        if divided in restes:
            return (i - restes[divided])
        restes[divided] = i
        i += 1

def find_biggest_repetitions_divisor(length):   
    i = 2
    result = 0
    biggest = 0
    while (i <= length):
        if (est_premier(i) == True):
            repetition = count_repetition(i)  
            if biggest < repetition:
                biggest = repetition
                result = i
        i += 1
    return result

def main():
    result = find_biggest_repetitions_divisor(1000)
    print(f"result : {result}")

if __name__ == "__main__":
    main()