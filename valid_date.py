def is_leap_year(yyyy):
    return (yyyy % 4 == 0 and yyyy % 100 != 0) or yyyy % 400 == 0


# print(is_valid_date(input()))
if __name__ == '__main__':
    date_string = '1900-2-30'
    year, month, day = map(int, date_string.split('-'))
    if year < 1000 or year > 9999:
        print('False')
    if month < 1 or month > 12:
        print('False')
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day < 1 or day > 31:
            print('False')
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day < 1 or day > 30:
            print('False')
    elif month == 2:
        if is_leap_year(year):
            if day < 1 or day > 29:
                print('False')
        else:
            if day < 1 or day > 28:
                print('False')
    else:
        print('True')
