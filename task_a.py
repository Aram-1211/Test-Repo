day = input("Input a day of the week: ").title().strip()

days = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5, 
    "Saturday": 6,
    "Sunday": 7,
}

if day in days.keys():
    print(f"{day} is day {days[day]}")
else:
    print("Please enter a valid day")