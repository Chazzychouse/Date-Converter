from database import months

def main():
    while True:
        date = get_date_from_user()
        try:
            month, day, year = handle_date(date)
        except ValueError or TypeError:
            print("Invalid Date")
        else:
            if month != " ":
                break

    print(year, f"{month:02}", f"{day:02}", sep = "-")


def get_date_from_user():
    while True:
        date = input("Date:")
        if date.find("/") != -1 or date.find(",") != -1:
            return date


def get_seperator(date):
    if date.find("/") != -1:
        return "/"
    if date.find(",") != -1:
        return ","


def handle_date(date):
    seperator = get_seperator(date)
    if seperator == "/":
        month = int(date[:date.find(seperator)])
        day = int(date[date.find(seperator) + 1: date.rfind(seperator)])
        year = int(date[date.rfind(seperator) + 1:])
        return month, day, year
        
    elif seperator == ",":
        month = date[:date.find(seperator)]
        month = month.title()
        day = int(date[(date.find(" ")) + 1: date.rfind(" ")])
        year = int(date[date.rfind(" ") + 1:])
        output_month = get_month_from_string(month)
        return output_month, day, year


def get_month_from_string(input_month):
    for month in months:
        if input_month == month:
            return (months[month])

    return " "

main()