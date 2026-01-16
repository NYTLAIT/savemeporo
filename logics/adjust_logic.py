from datetime import datetime
from logics.general_logic import *

# ENTER NEW LOG
def enter_adjust(
    adjust_id: int, 
    action: str, 
    amount: float, 
    user, 
    data_file='data.json'):
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
    original_action = None
    other_adjustments = []
    log_found = False
    
    for log in ledger_module:
        if log['user_id(FK)'] != user_id:
            continue
            
        if log.get('ledger_id(PK)') == adjust_id:
            log_found = True
            original_amount = log['amount']
            original_action = log['action']
            if original_action == 'out':
                original_amount = -original_amount
        
        if log.get('adjust_id(FK)') == adjust_id:
            adjustment = log['amount']
            if log['action'] == 'out':
                adjustment = -adjustment
            other_adjustments.append(adjustment)
    
    if not log_found:
        raise ValueError(f"Missing {adjust_id} for {user}")
    
    if action == 'in':
        correct_amount = +amount
    elif action == 'out':
        correct_amount = -amount
    else:
        raise ValueError(f"Invalid action: {action}. Must be 'in' or 'out'")
    
    current_total = original_amount + sum(other_adjustments)
    adjust_amount = correct_amount - current_total 
    
    new_adjust_ledger_entry = {
        "ledger_id(PK)": len(ledger_module) + 1, 
        "user_id(FK)": user_id,
        "timestamp": timestamp.isoformat(),
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

    adjust_data = {
        "adjust_id": adjust_id,
        "original_amount": original_amount,
        "correct_amount": correct_amount,
        "balance": total_balance(timestamp, ledger_module)
    }
    
    return adjust_data