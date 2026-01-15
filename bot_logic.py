from datetime import datetime
import json

data_file = 'data.json'
entry = {}
entry_location = ''

timestamp = datetime.now()

# WRITE/SAVE AND READ/LOAD JSON FILE
def read_data(data_file):
    '''
    acess previous data
    '''
    with open(data_file, 'r') as infile:
        return json.load(infile)

def write_data(data_file, entry_location):
    '''
    write into the json using entry variable
    '''
    with open(data_file, 'w') as outfile:
        json.dump(entry, outfile, indent=4)



def enter_log(action: str, amount: float, note: str):

    entry = {
        "ledger_id(PK)": "",
        "user_id(FK)": "",
        "date": "",
        "amount": "",
        "action": "",
        "method": "",
        "adjust_id": "",
        "note": ""
    }

    return entry, entry_location

    


# MATCH DATA FOR DAYS AND WEEKS AND ETC

#JUST TO SEE IF WORKING
print(json.dumps(read_data(data_file), indent=4))
print (timestamp)