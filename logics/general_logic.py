import json
from datetime import datetime

data_file = 'data.json'

# WRITE/SAVE AND READ/LOAD JSON FILE
def read_data(data_file):
    with open(data_file, 'r') as infile:
        return json.load(infile)

def write_data(data_file, data):
    with open(data_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)
# ^^^END

# CHECK USER
def check_account(user):
    """
    Loop through each existing account in data.json.
    If matched with given user, return the user's user_id(PK).
    If given user does not match any, create a new account and
    a new month statment to reference in data.json 
    and return user's new user_id(PK)
    
    :param user: user's discord account found through 
    interactions.user
    :type user: str
    :return user_id(PK): user's id to match objects
    :return data: access to state of data.json of when command 
    was called
    :return timestamp: timestamp for when /command was accessed,
    used for matching log times and entering log data
    """
    data = read_data(data_file)
    user_module = data.get('user_module')
    monthly_statement_module = data.get('monthly_statement_module')

    timestamp = datetime.now()

    for account in user_module:
        if user == account['user']:
            return account.get('user_id(PK)'), data, timestamp
        
    new_account_entry = {
        "user_id(PK)": len(user_module) + 1, 
        "user": user
    }
    new_first_monthly_statement_entry = {
        "month_id(PK)": len(monthly_statement_module) + 1,
        "user_id(FK)": new_account_entry['user_id(PK)'],
        "opening_balance": 0,
        "closing_balance": 0,
        "total_spent": 0,
        "total_saved": 0,
        "year": timestamp.year,
        "month": timestamp.month
        }
    
    user_module.append(new_account_entry)
    monthly_statement_module.append(new_first_monthly_statement_entry)
    write_data(data_file, data)

    return new_account_entry['user_id(PK)'], data, timestamp
# ^^^END

# FILTERING LEDGERS
def user_and_time_log_filter(user_id, ledger_module, timestamp, filter_type):
    """
    filter each log object in the list ledger_module and depending on
    the filter_type append the log to a list on the prerequisite that
    they match the given timestamp's year or year&month or date
    
    :param user_id: match each user 
    :param ledger_module: access to the specific list in data.json
    :param timestamp: datetime object of when /command was called
    :param filter_type: Type of date filter needed for logs year or 
    year&month or date
    :return log_list: filtered list of logs that meet filter specifications
    """   
    log_list = []
    
    for log in ledger_module:
        if log['user_id(FK)'] != user_id:
            continue
        
        log_date = datetime.fromisoformat(log['date'])
        if filter_type == 'year':
            if log_date.year == timestamp.year:
                log_list.append(log)
        elif filter_type == 'month':
            if log_date.year == timestamp.year and log_date.month == timestamp.month:
                log_list.append(log)
        elif filter_type == 'day':
            if log_date.date() == timestamp.date():
                log_list.append(log)

    return log_list
