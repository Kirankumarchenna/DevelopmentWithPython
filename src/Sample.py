import datetime


input_value = "2024-04-17 00:00:00"

if input_value is None:
    print(None)

if input_value is not None:
    if input_value is not isinstance(input_value, int):
        try:
            input_value = int(input_value)
            if isinstance(input_value, int):
                print(datetime.datetime.utcfromtimestamp(input_value / 1000))
            else:
                print(input_value)
        except:
            print(input_value)
