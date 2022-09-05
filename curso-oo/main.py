from operation import CashMachineConsole
from utils import clear_screen, header


def main():
    clear_screen()
    header()

    CashMachineConsole.call_operation()


if __name__ == '__main__':
    while True:
        main()
        
        input("Precione <ENTER> para continuar ...")
