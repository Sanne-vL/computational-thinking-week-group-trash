import datetime

def get_day_of_week(date_str):
    # list of Chinese day names
    weekday_names_chinese = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']

    try:
        
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')

        day_of_week = date.weekday()

        chinese_day_name = weekday_names_chinese[day_of_week]

        return chinese_day_name
    #if the format is wrong ask again
    except ValueError:
        return "This date format is not working, please use this format instead YYYY-MM-DD ."




