import nepali_datetime
from datetime import time

now = nepali_datetime.datetime.now()

# setting the working day and time for nepse
start_time = time(11,00)
end_time = time(15,00)
working_day = [6, 0, 1, 2, 3]

# getting the current time and day
today = now.weekday()
current_time = nepali_datetime.datetime.time(now)


def check_time():
	# validating if it is working day
	if today in working_day:
		# validating if it is working time
		if current_time >= start_time and current_time <= end_time:
			return True
		else:
			return False		
	else:
		return False
		