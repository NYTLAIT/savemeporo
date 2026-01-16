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
# ^^^END

# SORT FILTERED_LOG_LIST
def sort_log_data(statement_log_data, numeric=False):
    """
    Convert the value of the key (the return function type 
    pointing to the value the list item will be compared and
    sorted by which works for year and month only as they are
    numerics in strings. Else python knows how to compare 
    .strftime("%H:%M:%S").

    :param numeric: bool of whether statement_log_data is numeric,
    default false
    :return sorted_statement_log_data: sorted statement_log_data
    from earliest to latest
    :type sorted_statement_log_data: dict
    """
    def sort_key(log):
        """
        sorts the key of the log by turning defined integer key string 
        into actual integers
        
        :param log: indiv each log in the statement_log_data dictionary
        key: value pair turned (key, value) tuple
        :type log: (key, value) tuple
        """
        key, value = log
        if numeric:
            return int(key)
        return key

    sorted_log_list = sorted(statement_log_data.items(), key=sort_key)

    return dict(sorted_log_list)
# ^^^END

# ALL LEDGER TOTAL BALANCE
def total_balance(timestamp_date, ledger_module):
    total_balance = 0

    for log in ledger_module:
        log_datetime = datetime.fromisoformat(log.get('date'))
        if log_datetime <= timestamp_date:
            if log.get('action') == 'in':
                total_balance += log['amount']
            elif log.get('action') == 'out':
                total_balance -= log['amount']
    
    return total_balance
# ^^^END

# FILTERED_LOG TOTAL CALC
def log_totals(log_list):
    totals = {
        "added": 0,
        "spent": 0,
        "net_change": 0
    }

    for log in log_list:
        action = log['action']
        amount = log['amount']
    
        if action == 'in':
            totals['added'] += amount
            totals['net_change'] += amount
        elif action == 'out':
            totals['spent'] += amount
            totals['net_change'] -= amount

    return totals
# ^^^END