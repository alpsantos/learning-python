from file import load_bank_data
import operations
import utils
import bank_account_variables


def main():
    load_bank_data()
    print(bank_account_variables.accounts_list)
    utils.header()
    account_auth = operations.auth_account()

    if account_auth:
        utils.clear_screen()
        utils.header()

        option_typed = operations.get_menu_options_typed(account_auth)
        operations.do_operation(account_auth, option_typed)
    else:
        print('Conta Inválida')

if __name__ == '__main__':
    while True:

        main()

        input('Presione <ENTER> para continuar')

        utils.clear_screen()
