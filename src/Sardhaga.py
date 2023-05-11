import datetime

input_value = "1713312000000"

if input_value is not None:
    try:
        input_value = int(input_value)
        print(datetime.datetime.utcfromtimestamp(input_value / 1000))
    except ValueError:
        print(input_value)
else:
    print(None)
