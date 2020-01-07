def leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


def get_month_days(year, month):
    days = 31
    if 2 == month:
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif month in [4, 6, 9, 11]:
        days = 30
    return days


def get_total_days(year, month):
    total_days = 0
    for i in range(1900, year):
        if leap_year(year):
            total_days += 366
        else:
            total_days += 365
    for i in range(1, month):
        total_days += get_month_days(year, i)
    return total_days




def month_cal (year,month):

    print(month, end="\n")
    print("日\t一\t二\t三\t四\t五\t六")

    count = 0

    for c in range(get_total_days(year, month) % 7 + 1):
        print(end="\t")
        count += 1

    for day in range(1, get_month_days(year, month) + 1):
        print(day, end="\t")
        count += 1
        if 0 == count % 7:
            print("\n")


def year_cal(year): #这个是有问题的！！！

    year_cal={}

    for i in range(1, 13):
        year_cal = year_cal + dict(month_cal(year, i))
        i += 1
    return year_cal


if __name__ == '__main__':
    while True:
        print("calendar is available")
        year = input("year：")
        month = input("month: ")
        try:
            year = int(year)
            month = int(month)
            if month < 1 or month > 12:
                print("wrong input")
                continue
        except:
            print("wrong input")
            continue
        break



print(month_cal(year,month))
