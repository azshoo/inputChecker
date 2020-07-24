def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def days_in_month(month_number, year):
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month_number in [4, 6, 9, 11]:
        return 30
    else:
        if is_leap_year(year): return 29
        else: return 28

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def validate_input(numbers):
    if numbers[2] < 1:
        return False
    else:
        year = numbers[2]

    if numbers[1] < 1 or numbers[1] > 12 :
        return False
    else:
        month = numbers[1]
    if numbers[0] < 1 or numbers[0] > days_in_month(month, year):
        return False
    else:
        return True

def check_input_is_date(input):
    numbers = input.split()
    if len(numbers) != 3:
        # return "Invalid input, number of elements is not equal to three"
        return False
    for num in numbers:
        if not is_integer(num):
            # return "Input is not whole number, cant be a valid date."
            return False
    numbers = [int(x) for x in numbers]
    if validate_input(numbers):
        ## return "Date seems to be valid"
        return True
    else:
        ## return "The input is not valid date"
        return False
