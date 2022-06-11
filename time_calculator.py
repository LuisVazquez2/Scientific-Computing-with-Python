def add_time(start, end,day=""):
    n_days = 0
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    meridiano = start[-2:]
    start = start[:-2]
    start = start.split(":")
    end = end.split(":")
    hours = int(start[0]) + int(end[0])
    minutes = int(start[1]) + int(end[1])
    hours += minutes // 60
    minutes %= 60
    times = hours // 12
    n_days = times//2
    hours %= 12
    times %= 2
    hours = 12 if hours == 0 else hours
    
    if times == 1:
        if meridiano == "AM": 
            meridiano = "PM"
        else:
            n_days += 1
            meridiano = "AM"
    complement = ""
    if n_days > 0:
        complement = " (next day)" if n_days == 1 else f" ({n_days} days later)"
    if day != "":
        day = day.capitalize()
        position = days.index(day)
        return f"{hours}:{minutes:02d} {meridiano}, {days[(position + n_days) % 7]}{complement}"
        
    return f"{hours}:{minutes:02d} {meridiano}{complement}"

print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)