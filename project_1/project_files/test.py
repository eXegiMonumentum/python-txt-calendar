import datetime

chosen_month = datetime.datetime.now().strftime("%B")
current_day_int = datetime.datetime.now().day
print(type(current_day_int))