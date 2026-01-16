from datetime import datetime
from logics.general_logic import *

# ENTER NEW LOG
def enter_log(action: str, amount: float, note: str, user, data_file='data.json'):
    """
    Check if user exists and create account if not.
    Create new ledger log entry including given info and timestamp,
    identifiable by the given user's user_id marked by user_id

    :param user: user's discord account found through 
    interactions.user
    :type user: str
    :param action: available values [in, out] - in for adding
    and out for subtracting
    :type action: str
    :param amount: amount gained or spent
    :type amount: float
    :param note: recommended to write item spent for action out,
    optional for action in
    :type note: str
    :return:
    """
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    new_ledger_entry = {
        "ledger_id(PK)": len(ledger_module) + 1, 
        "user_id(FK)": user_id,
        "date": timestamp.date().isoformat(),
        "time": timestamp.time().isoformat(),
        "amount": amount,
        "action": action,
        "method": "null",
        "adjust_id": "null",
        "note": note
    }
    ledger_module.append(new_ledger_entry)

    write_data(data_file, data)
# ^^^END
