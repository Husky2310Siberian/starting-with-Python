def get_average(*numbers):
    """

    :param numbers:
    :return:
    """
    if not numbers:
        print("No numbers available")

    average = sum(numbers) / len(numbers)
    return average

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Average is", get_average(*numbers))

if __name__ == "__main__":
    main()