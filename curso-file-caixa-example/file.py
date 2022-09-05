import os
import bank_account_variables

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def open_file_bank(mode):
    return open(BASE_DIR + '/_bank_file.dat', mode)


def write_money_slips(file):
    for money_bill, value in bank_account_variables.money_slips.items():
        file.write(money_bill + '=' + str(value) + ';')


def write_bank_accounts(file):
    for account, account_data in bank_account_variables.accounts_list.items():
        file.writelines((
            account, ';',
            account_data['name'], ';',
            account_data['password'], ';',
            str(account_data['value']), ';',
            str(account_data['admin']), ';',
            '\n'
        ))


def read_money_slips(file):
    line = file.readline()  # 20=5;50=5;100=5;
    while line.find(';') != -1:
        semicolon_pos = line.find(';')
        money_bill_value = line[0: semicolon_pos]
        set_money_bill_value(money_bill_value)
        if (semicolon_pos + 1 == len(line)):
            break
        else:
            line = line[semicolon_pos + 1: len(line)]


# 1111-01;Fulano de tal;01;100.1;False;
# 1111-02;Fulano de tal;02;60.6;False;
def read_bank_accounts(file):
    lines = file.readlines()
    lines = lines[1: len(lines)]
    for account_line in lines:
        extract_bank_account(account_line)


# 1111-01;Fulano de tal;01;100.1;False;
def extract_bank_account(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolon_pos = account_line.find(';')
        data = account_line[0: semicolon_pos]
        account_data.append(data)
        if (semicolon_pos + 1 == len(account_line)):
            break
        else:
            account_line = account_line[semicolon_pos + 1: len(account_line)]
    add_bank_account(account_data)


def add_bank_account(account_data):
    bank_account_variables.accounts_list[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'value': float(account_data[3]),
        'admin': True if account_data[4] == 'True' else 'False'
    }


def set_money_bill_value(money_bill_value):
    equal_pos = money_bill_value.find('=')
    money_bill = money_bill_value[0: equal_pos]
    value = money_bill_value[equal_pos + 1: len(money_bill_value)]
    bank_account_variables.money_slips[money_bill] = value


def load_bank_data():
    file = open_file_bank('r')
    read_money_slips(file)
    file.close

    file = open_file_bank('r')
    read_bank_accounts(file)
    file.close


# 20=5;50=5;100=5;
# 1111-01;Fulano de tal;01;100.1;False;
# 1111-02;Fulano de tal;02;60.6;False;
def save_money_slips():

    file = open_file_bank('r')
    lines = file.readlines()
    file.close()
    file = open_file_bank('w')
    print(lines)
    lines[0] = ""
    for money_bill, value in bank_account_variables.money_slips.items():
        lines[0] += money_bill + '=' + str(value) + ';'
    lines[0] += '\n'
    file.writelines(lines)
    file.close()


def delete_files():
    path = BASE_DIR + '/_delete_file.dat'
    file = open(path, 'w')
    file.close()
    if os.path.exists(path):
        # os.unlink(path)
        print("Arquivo existe")
    else:
        print("Arquivo não existe")
