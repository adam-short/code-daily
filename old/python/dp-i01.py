from operator import itemgetter

class TimeTaken(Exception):
    def __init__(self, time):
        context = "Time {} is already taken.".format(time)
        Exception.__init__(self, context)
        self.time = time

class TimeNotTaken(Exception):
    def __init__(self, time):
        context = "There is no event at {}.".format(time)
        Exception.__init__(self, context)
        self.time = time

def print_cal(cal):
    if not len(cal):
        print("No events!")

    for time, event in sorted(cal.iteritems(), key=itemgetter(0)):
        print("{} : {}".format(time, event))

def add_to_cal(cal, hour, event):
    if cal.get(hour):
        raise TimeTaken(hour)
    else:
        new_cal = cal.copy()
        new_cal.update({hour: event})
        return new_cal

def edit_date_in_cal(cal, hour, new):
    if not cal.get(hour):
        raise TimeNotTaken(hour)
    else:
        new_cal = cal.copy()
        new_cal[hour] = new
        return new_cal

def delete_date_in_cal(cal, hour):
    if not cal.get(hour):
        raise TimeNotTaken(hour)
    else:
        new_cal = cal.copy()
        del new_cal[hour]
        return new_cal


def intinput(message):
    try:
        return int(raw_input(message + " >  "))
    except ValueError:
        print("Must enter an integer.")
        return intinput(message)

def stringinput(message):
    return raw_input(message + " >  ")

if __name__ == '__main__':
    calendar = {}
    while True:
        print_cal(calendar)
        print("[1] Add")
        print("[2] Edit")
        print("[3] Delete")
        selection = intinput("Enter number")

        if selection == 1:
            hour = stringinput("Enter hour in 24hr format")
            event = stringinput("Enter event name")
            try:
                calendar = add_to_cal(calendar, hour, event)
            except TimeTaken as e:
                print(e)
            else:
                print("Added event!")
        elif selection == 2:
            hour = stringinput("Enter existing hour in 24hr format")
            new_event = stringinput("Enter new event name")
            try:
                calendar = edit_date_in_cal(calendar, hour, new_event)
            except TimeNotTaken as e:
                print(e)
            else:
                print("Edited event!")
        elif selection == 3:
            hour = stringinput("Enter existing hour in 24hr format")
            try:
                calendar = delete_date_in_cal(calendar, hour)
            except TimeNotTaken as e:
                print(e)
            else:
                print("Hour deleted!")
        else:
            print("Must be 1, 2 or 3.")
