from datetime import datetime, timedelta

def hour_difference(timestamp1, timestamp2):
    timestamp_format = "%Y/%m/%d %H:%M"
    time1 = datetime.strptime(timestamp1, timestamp_format)
    time2 = datetime.strptime(timestamp2, timestamp_format)
    
    if time1 > time2:
        time1, time2 = time2, time1
    
    total_hours = 0
    current_time = time1
    
    while current_time < time2:
        if current_time.weekday() < 5:  # Only count weekdays (Monday-Friday)
            work_start = current_time.replace(hour=9, minute=0)
            work_end = current_time.replace(hour=17, minute=0)
            
            if current_time < work_start:
                current_time = work_start  # Move to the start of the workday
            
            if current_time >= work_end:
                current_time += timedelta(days=1)
                current_time = current_time.replace(hour=9, minute=0)
                continue
            
            next_time = min(work_end, time2)
            total_hours += (next_time - current_time).total_seconds() / 3600
            current_time = next_time
        
        current_time += timedelta(days=1)
        current_time = current_time.replace(hour=9, minute=0)
    
    return round(total_hours)

# Example usage
timestamp1 = "2025/03/16 17:00"  # Monday
timestamp2 = "2025/03/11 09:00"  # Tuesday
print(hour_difference(timestamp1, timestamp2))