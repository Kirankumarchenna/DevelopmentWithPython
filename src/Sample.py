import datetime

# input Values:
# 1713312000000   "2024-04-17 00:00:00"
#
# Cases:
# 1) Int value convert to human readable time format
# 2) String value conversion to Human readable time format
# 3) None value to be return none
# 4) If parsing fails then it should return original value

input_value =   1713312000000

if input_value is not None:
    try:
        input_value = int(input_value)
        print(datetime.datetime.utcfromtimestamp(input_value / 1000))
    except:
        print(input_value)