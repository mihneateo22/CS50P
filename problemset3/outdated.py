months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
        else:
            month_name, day, year = date.split(" ")
            if not day.endswith(","):
                continue
            day = day.removesuffix(",")
            month = months.index(month_name) + 1
        day = int(day)
        year = int(year)
    except ValueError:
        continue
    
    if 1 <= month <= 12 and 1 <= day <= 31:
        break

print(f"{year}-{month:02}-{day:02}")