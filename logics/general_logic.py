import json

data_file = 'data.json'

# WRITE/SAVE AND READ/LOAD JSON FILE
def read_data(data_file):
    with open(data_file, 'r') as infile:
        return json.load(infile)

def write_data(data_file, data):
    with open(data_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)
# ^^^END

data = read_data(data_file)

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
    :return user_id(PK):
    """
    user_module = data.get('user_module')
    monthly_statement_module = data.get('monthly_statement_module')

    for account in user_module:
        if user == account['user']:
            return account.get('user_id(PK)')
        
    new_account_entry = {
        "user_id(PK)": len(user_module) + 1, 
        "user": user
    }
    user_module.append(new_account_entry)
    new_first_month_statement_entry = {
        "month_id(PK)": "",
        "user_id(FK)": "",
        "opening_balance": "",
        "closing_balance": "",
            "total_spent": "",
            "total_saved": "",
            "year": "",
            "month": ""
        }

    write_data(data_file, data)
    return new_account_entry['user_id(PK)']
# ^^^END

# FILTERING LEDGERS
def user_and_time_ledger_filter(user_id, filter_type):
    pass