
from ui.assign_ui import AssignUI
from ui.make_voyage_ui import VoyageUI
from ui.employee_ui import EmployeeUI
from ui.destinations_ui import DestinationsUI

class Main:

    def MainMenu(self):
        print("\n\n  .-----------------. .----------------.  .-----------------.      .----------------.  .----------------.  .----------------. \n| .--------------. || .--------------. || .--------------. |     | .--------------. || .--------------. || .--------------. |\n| | ____  _____  | || |      __      | || | ____  _____  | |     | |      __      | || |     _____    | || |  _______     | |\n| ||_   \|_   _| | || |     /  \     | || ||_   \|_   _| | |     | |     /  \     | || |    |_   _|   | || | |_   __ \    | |\n| |  |   \ | |   | || |    / /\ \    | || |  |   \ | |   | |     | |    / /\ \    | || |      | |     | || |   | |__) |   | |\n| |  | |\ \| |   | || |   / ____ \   | || |  | |\ \| |   | |     | |   / ____ \   | || |      | |     | || |   |  __ /    | |\n| | _| |_\   |_  | || | _/ /    \ \_ | || | _| |_\   |_  | |     | | _/ /    \ \_ | || |     _| |_    | || |  _| |  \ \_  | |\n| ||_____|\____| | || ||____|  |____|| || ||_____|\____| | |     | ||____|  |____|| || |    |_____|   | || | |____| |___| | |\n| |              | || |              | || |              | |     | |              | || |              | || |              | |\n| '--------------' || '--------------' || '--------------' |     | '--------------' || '--------------' || '--------------' |\n '----------------'  '----------------'  '----------------'       '----------------'  '----------------'  '----------------'   \n \n")
        choice_str = ''
        while choice_str != 'q':
            print('Welcome!\n')
            print('Press "1" for Voyage menu')
            print('Press "2" to Assign employees to a voyage')
            print('Press "3" to register,list or change employee information ')
            print('Press "4" for Destination Menu')
            #print('Press "4" to create a new destination ') # Breyta þessu í destination menu þar sem hægt er að sja og breyta 
            print('Press "q" to Quit\n')
            choice_str = input('Choose an option: ')

            if choice_str == 'q':
                choice_str = 'q'
            elif choice_str == '1':
                choice_str = VoyageUI().menu()
            elif choice_str == '2':
                choice_str = AssignUI().menu()
            elif choice_str == '3':
                choice_str = EmployeeUI().menu()
            elif choice_str == '4':
                choice_str = DestinationsUI().selectin_dest()
                #choice_str = DestinationsUI().destinations_menu()
    ###Vantar að geta breytt tengiliðaupplýsingum fyrir destination
