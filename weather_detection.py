# import user_temperature
# import fetch_date_time 

# if fetch_date_time.month >=3 and fetch_date_time.month <=5:
#     season = "summer"
# if fetch_date_time.month >=6 and fetch_date_time.month <=9:
#     season = "rainy"
# if fetch_date_time.month >=10 and fetch_date_time.month <=2:
#     if user_temperature.temperature_int>25:
#         season = "summer"
#     else:
#         season = "winter"

# print(f"The season is: {season}")



import fetch_date_time 
month = fetch_date_time.month


if month >=3 and month <=5:
    season = "summer"
if month >=6 and month <=9:
    season = "rainy"
if month >=10 and month <=2:
    season = "winter"

print(f"The season is: {season}")

