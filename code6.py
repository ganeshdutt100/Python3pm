WeekDays = int(input("Enter your Weekday Number :"))

def switch_case(WeekDays):
    match WeekDays:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid Weekday Number"

print( switch_case(WeekDays))