def print_cities(*cities , seperator=", " , end="\t") -> str:
    """
    Returns a string, representing *cities".

    Args:
        :param cities: a string of cities
        :param seperator: the seperator " , "
        :param end: the end " \t "
        :return: a string
    """
    if not cities:
        print("No cities available")
    else:
        print("Cities:", ", " .join(cities), sep=seperator, end=end)

def main():
    print_cities("Napoli", "London", "Calgary" , seperator=" | " , end=".")
    print_cities("Sydney")
    print_cities("")
    print_cities()

if __name__ == "__main__":
    main()