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
        
        if log.get['action'] == 'in':
            monthly_data[log_date_datetime.month]['added'] += log['amount']
            monthly_data[log_date_datetime.month]['net_change'] += log['amount']
        elif log.get['action'] == 'in':
            monthly_data[log_date_datetime.month]['spent'] += log['amount']
            monthly_data[log_date_datetime.month]['net_change'] -= log['amount']
            
    return monthly_data

def month_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'month'
    month_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)

    weekly_data = {}

    for log in month_log_list:
        log_date_datetime = datetime.fromisoformat(log['date']).date().isocalendar()

        if log_date_datetime.month not in weekly_data:
            weekly_data[log_date_datetime.month] = {
                "week": log_date_datetime.strftime("%B"),
                "added": 0,
                "spent": 0,
                "net_change": 0,
                "logs": []
            }
        
        if log.get['action'] == 'in':
            weekly_data[log_date_datetime.month]['added'] += log['amount']
            weekly_data[log_date_datetime.month]['net_change'] += log['amount']
        elif log.get['action'] == 'in':
            weekly_data[log_date_datetime.month]['spent'] += log['amount']
            weekly_data[log_date_datetime.month]['net_change'] -= log['amount']
            
    return weekly_data

def day_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    filter_type = 'day'
    day_log_list = user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type)

    timely_data = {}

    