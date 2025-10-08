def add_time(start, duration, start_day=None):
    time_part, period = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))


    if period.upper() == 'PM':
        start_hour += 12
        if start_hour == 24:
            start_hour = 12
    elif start_hour == 12 and period.upper() == 'AM':
        start_hour = 0

 
    dur_hour, dur_minute = map(int, duration.split(':'))

  
    total_minutes = start_minute + dur_minute
    extra_hours = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + dur_hour + extra_hours
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24


    if final_hour_24 == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_period = 'PM'

 
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    result_day = ""
    if start_day:
        start_day = start_day.capitalize()
        start_index = days_of_week.index(start_day)
        result_day_index = (start_index + days_later) % 7
        result_day = f", {days_of_week[result_day_index]}"


    if days_later == 1:
        day_text = " (next day)"
    elif days_later > 1:
        day_text = f" ({days_later} days later)"
    else:
        day_text = ""

 
    new_time = f"{final_hour}:{final_minute:02d} {final_period}{result_day}{day_text}"
    return new_time
