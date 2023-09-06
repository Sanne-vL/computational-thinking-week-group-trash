import datetime

def solution_station_2(date_str):
 
    weekday_names = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

    date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

    day_of_week = date.weekday()

    day_name = weekday_names[day_of_week]

    return str(day_name)
   
#input_date = input()
#day = get_day_of_week(input_date)
#print(f"{day}")




