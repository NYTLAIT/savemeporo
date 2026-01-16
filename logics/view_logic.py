from logics.general_logic import *

def year_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'year'
    year_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)
    
    monthly_data = {}

    for log in year_log_list:
        log_date_datetime = datetime.fromisoformat(log['date']).date()

        if log_date_datetime.month not in monthly_data:
            monthly_data[log_date_datetime.month] = {
                "month": log_date_datetime.strftime("%B"),
                "added": 0,
                "spent": 0,
                "net_change": 0,
                "logs": []
            }
        
        
            
    return monthly_data

def month_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'month'
    month_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)

    weekly_data = {}

    for log in month_log_list:
        log_date_datetime = datetime.fromisoformat(log['date']).date()
        log_date_weeknum = log_date_datetime.isocalendar()

        if log_date_weeknum[1] not in weekly_data:
            weekly_data[log_date_weeknum[1]] = {
                "week_start_date": log_date_datetime,
                "week_end_date": log_date_datetime,
                "added": 0,
                "spent": 0,
                "net_change": 0,
                "logs": []
            }
        else:
            if log_date_datetime < weekly_data[log_date_weeknum[1]]["week_start"]:
                weekly_data[log_date_weeknum[1]]["week_start_date"] = log_date_datetime
            if log_date_datetime > weekly_data[log_date_weeknum[1]]["week_start"]:
                weekly_data[log_date_weeknum[1]]["week_end_date"] = log_date_datetime
            
    return weekly_data

def day_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'day'
    day_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)

    timely_data = {}

    for log in day_log_list:
        log_date_time = datetime.fromisoformat(log['time']).time()

        if log_date_time not in timely_data:
            timely_data[log_date_time] = {
                "time": log_date_time.strftime("%H:%M:%S"),
                "added": 0,
                "spent": 0,
                "net_change": 0,
                "logs": []
            }
    
    def sorted_func()

    return timely_data
    