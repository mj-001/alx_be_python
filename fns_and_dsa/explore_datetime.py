from datetime import datetime, timedelta

def display_current_datetime():
    current_date=datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time and date is {formatted_date}")

display_current_datetime()

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    current_date=datetime.now()
    future_date= current_date + timedelta(number_of_days)
    formatted_date = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Future time and date will be {formatted_date}")

calculate_future_date()



