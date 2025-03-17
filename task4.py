from datetime import datetime

def hour_difference(timestamp1, timestamp2):
    timestamp_format = "%Y/%m/%d %H:%M"
    time1 = datetime.strptime(timestamp1, timestamp_format)
    time2 = datetime.strptime(timestamp2, timestamp_format)
    time_difference = abs(time2 - time1)
    hour_difference = round(time_difference.total_seconds() / 3600)
    
    return hour_difference

timestamp1 = "2022/02/15 06:29"
timestamp2 = "2022/02/17 01:00"
print(hour_difference(timestamp1, timestamp2))  
