
from ui.assign_ui import menu as a_ui
from ui.make_voyage_ui import menu as mv_ui
from ui.employee_ui import menu as emp_ui

def MainMenu():
    print("\n\n  .-----------------. .----------------.  .-----------------.      .----------------.  .----------------.  .----------------. \n| .--------------. || .--------------. || .--------------. |     | .--------------. || .--------------. || .--------------. |\n| | ____  _____  | || |      __      | || | ____  _____  | |     | |      __      | || |     _____    | || |  _______     | |\n| ||_   \|_   _| | || |     /  \     | || ||_   \|_   _| | |     | |     /  \     | || |    |_   _|   | || | |_   __ \    | |\n| |  |   \ | |   | || |    / /\ \    | || |  |   \ | |   | |     | |    / /\ \    | || |      | |     | || |   | |__) |   | |\n| |  | |\ \| |   | || |   / ____ \   | || |  | |\ \| |   | |     | |   / ____ \   | || |      | |     | || |   |  __ /    | |\n| | _| |_\   |_  | || | _/ /    \ \_ | || | _| |_\   |_  | |     | | _/ /    \ \_ | || |     _| |_    | || |  _| |  \ \_  | |\n| ||_____|\____| | || ||____|  |____|| || ||_____|\____| | |     | ||____|  |____|| || |    |_____|   | || | |____| |___| | |\n| |              | || |              | || |              | |     | |              | || |              | || |              | |\n| '--------------' || '--------------' || '--------------' |     | '--------------' || '--------------' || '--------------' |\n '----------------'  '----------------'  '----------------'       '----------------'  '----------------'  '----------------'   \n \n")
    choice_str = ''
    while choice_str != 'q':
        print('Welcome!')
        print('Press "1" for Voyage menu')
        print('Press "2" to Assign eployees to a voyage')
        print('Press "3" to register or list employees ')
        print('Press "q" to Quit\n')
        choice_str = input('Choose an option: ')

        if choice_str == 'q':
            choice_str = 'q'
        elif choice_str == '1':
            choice_str = mv_ui()
        elif choice_str == '2':
            choice_str = a_ui()
        elif choice_str == '3':
            choice_str = emp_ui()
###Vantar að geta breytt tengiliðaupplýsingum fyrir destination
