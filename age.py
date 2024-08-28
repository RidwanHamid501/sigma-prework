import datetime as dt


def calculate_age(date):
    current = dt.datetime.now()
    conv_date = dt.datetime.strptime(date, "%d-%m-%Y")

    val = current.year - conv_date.year
    if current < conv_date.replace(year=current.year):
        val -= 1

    return val


def main():
    date = input("Enter a date in the form 'dd-mm-yyyy': ")
    age = calculate_age(date)

    print(f"Age: {age}")


if __name__ == "__main__":
    main()
