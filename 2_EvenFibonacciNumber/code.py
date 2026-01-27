

 #1 2 3 5 8 13 21 34
def fibonacci_pair(limite):
    paire = 0
    a = 1
    b = 2
    
    while a <= limite:
        if a % 2 == 0:
            print(f"a l interieru {a}")
            paire += a
        tmp = a + b
        a = b
        b = tmp
    return (paire)


def main():
    result = fibonacci_pair(4000000)
    print(f"resultats : {result}")

if (__name__ == "__main__"):
    main()