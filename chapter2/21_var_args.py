def print_cities(*cities):
    if not cities:
        print("No cities available")
    else:
        print("Cities:" , " , " .join(cities))

def main():
    print_cities("Napoli, London, Calgary")
    print_cities("Sydney")
    print_cities("")
    print_cities()

if __name__ == "__main__":
    main()