import datetime
import sys

def int2day(i):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]
    return days[i]

if __name__ == '__main__':
    try:
        day = int(sys.argv[1])
        month = int(sys.argv[2])
        year = int(sys.argv[3])

        time = datetime.date(year, month, day)
        print(int2day(time.weekday()))
    except IndexError as e:
        print("ERROR: Missing day, month or year.")
    except ValueError as e:
        print("ERROR: Day/month/year must be ints within appropriate value ranges.")
