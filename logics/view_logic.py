from logics.general_logic import *

def view_option_gateway(user, scope):
    if scope == 'year':
        return year_log(user)
    elif scope == 'month':
        return month_log(user)
    elif scope == 'day':
        user_id = None
        data = None
        timestamp = None
        return day_log(user, user_id, data, timestamp)

def year_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'year'
    year_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)
    
    monthly_data = {}
    total_added = 0
    total_spent = 0

    for log in year_log_list:
        log_date_datetime = datetime.fromisoformat(log['timestamp']).date()

        if log_date_datetime.month not in monthly_data:
            monthly_data[log_date_datetime.month] = {
                "month": log_date_datetime.strftime("%B"),
                "added": 0,
                "spent": 0,
                "net_change": 0,
                "logs": []
            }
        monthly_data[log_date_datetime.month]['logs'].append(log)

    for month in monthly_data:
        month_totals = log_totals(monthly_data[month]['logs'])
        monthly_data[month].update(month_totals)

        total_added += month_totals['added']
        total_spent += month_totals['spent']

    year_statement = {
        "year": timestamp.date().year,
        "monthly_data": monthly_data,
        "total_added": total_added,
        "total_spent": total_spent,
        "net_change": total_added - total_spent,
        "balance": total_balance(timestamp, ledger_module)
    }
        
    year_statement['monthly_data'] = sort_log_data(year_statement['monthly_data'], numeric=True)
    
    return year_statement

def month_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'month'
    month_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)

    weekly_data = {}
    total_added = 0
    total_spent = 0

    for log in month_log_list:
        log_date_datetime = datetime.fromisoformat(log['timestamp']).date()
        log_date_weeknum = log_date_datetime.isocalendar()[1]

        if log_date_weeknum not in weekly_data:
            weekly_data[log_date_weeknum] = {
                "week_start_date": log_date_datetime,
                "week_end_date": log_date_datetime,
                "added": 0,
                "spent": 0,
                "net_change": 0,
                "logs": []
            }
        else:
            if log_date_datetime < weekly_data[log_date_weeknum]['week_start_date']:
                weekly_data[log_date_weeknum]['week_start_date'] = log_date_datetime
            if log_date_datetime > weekly_data[log_date_weeknum]['week_end_date']:
                weekly_data[log_date_weeknum]['week_end_date'] = log_date_datetime

        weekly_data[log_date_weeknum]['logs'].append(log)

    for week in weekly_data:
        week_totals = log_totals(weekly_data[week]['logs'])
        weekly_data[week].update(week_totals)

        total_added += week_totals['added']
        total_spent += week_totals['spent']

    month_statement = {
        "month": timestamp.date().month,
        "weekly_data": weekly_data,
        "total_added": total_added,
        "total_spent": total_spent,
        "net_change": total_added - total_spent,
        "balance": total_balance(timestamp, ledger_module)
    }

    month_statement['weekly_data'] = sort_log_data(month_statement['weekly_data'], numeric=True)
            
    return month_statement

def day_log(user, user_id, data, timestamp):
    if user_id == None:
        user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'day'
    day_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)

    timely_data = {}
    total_added = 0
    total_spent = 0

    for log in day_log_list:
        log_date_time = datetime.fromisoformat(log['timestamp']).time()

        if log_date_time not in timely_data:
            timely_data[log_date_time] = {
                "time": log_date_time.strftime("%H:%M:%S"),
                "added": 0,
                "spent": 0,
                "net_change": 0,
                "logs": []
            }
        
        timely_data[log_date_time]['logs'].append(log)

    for time in timely_data:
        time_totals = log_totals(timely_data[time]['logs'])
        timely_data[time].update(time_totals)

        total_added += time_totals['added']
        total_spent += time_totals['spent']

    day_statement = {
        "day": timestamp.date().isoformat(),
        "timely_data": timely_data,
        "total_added": total_added,
        "total_spent": total_spent,
        "net_change": total_added - total_spent,
        "balance": total_balance(timestamp, ledger_module)
    }

    day_statement['timely_data'] = sort_log_data(day_statement['timely_data'])

    return day_statement