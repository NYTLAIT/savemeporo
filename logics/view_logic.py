from logics.general_logic import *

def year_log(user):
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')
    
    filter_type = 'year'

    user_and_time_log_filter(user_id, )

    