from datetime import date

month = int(raw_input("month #>  "))
day = int(raw_input("day #>  "))
date_given = date(2017, month, day)
print("Day is #{} of year.".format(date_given.timetuple().tm_yday))
