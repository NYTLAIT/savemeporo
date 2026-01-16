from datetime import datetime
from logics.general_logic import *
from logics.view_logic import day_log

# ENTER NEW LOG
def enter_adjust(adjust_id: int, action: str, amount: float, user, data_file='data.json'):
    """
    Create a log adjustment entry and return the updated 
    day statement.

    :param adjust_id: id of needed adjustment log
    :param action: 'in' for adding or 'out' for subtracting
    :param amount: amount of the adjustment
    :param user: discord user
    :param data_file: path to data file
    :return day_statement: dict of day_statement
    """
    user_id, data, timestamp = check_account(user)
    ledger_module = data.get('ledger_module')

    original_amount = 0
    other_adjustments = []

    for log in ledger_module:
        if log['user_id(FK)'] != user_id:
            continue
        if log['ledger_id(PK)'] == adjust_id:
            original_amount = log['amount']
            original_action = log['action']
            if original_action == 'out':
                original_amount = -original_amount
        if log['adjust_id(FK)'] == adjust_id:
            adjustment = log['amount']
            if log['action'] == 'out':
                adjustment = -adjustment
            other_adjustments.append(adjustment)

    if action == 'in':
        correct_amount = +amount
    elif action == 'out':
        correct_amount = -amount

    current_total = original_amount + sum(other_adjustments)
    adjust_amount = correct_amount - current_total 

    adjust_data = {
        "adjust_id": adjust_id,
        "original_amount": original_amount,
        "correct_amount": correct_amount,
    }

    new_adjust_ledger_entry = {
        "ledger_id(PK)": len(ledger_module) + 1, 
        "user_id(FK)": user_id,
        "date": timestamp.date().isoformat(),
        "time": timestamp.time().isoformat(),
        "amount": abs(adjust_amount),
        "action": 'in' if adjust_amount >= 0 else 'out',
        "method": None,
        "adjust_id(FK)": adjust_id,
        "note": "adjustment"
    }
    ledger_module.append(new_adjust_ledger_entry)

    write_data(data_file, data)

    return adjust_data
# ^^^END