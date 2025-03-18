def get_formatted_date(day: int = 1 , month: int = 1 , year: int = 2000) -> str:
    """
    Returns a string, representing a date in the format "dd-mm-yyyy".

    Args:
            day: The day of the month , default 1
            month: The month of the year , default 1
            year: The year, default 2000

    Return:
            The formatted date string
    """
    return f"{day:02d}-{month:02d}-{year:04d}"

def main():
    print(get_formatted_date())
    print(get_formatted_date(10))
    print(get_formatted_date(23,10))
    print(get_formatted_date(12,2,2022))

    print(get_formatted_date(year=2025))
    print(get_formatted_date(year=2025 , month=3 , day=18))


if __name__ == "__main__":
    main()