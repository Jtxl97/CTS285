#CTS-285-0001
#M1HW
#Jonathan Lopresto
#8/30/2022
def mainmenu():
    print(' -----------MENU-----------')
    print('1) Add Numbers')
    print('2) Multiply Numbers')
    print('3) Subtract Numbers')
    print('4) Divid Numbers')
    print('5) Exit')
    print('---------------------------')
    menu_choice = input('Choose from the menu above by entering a number 1-5: ')
    if menu_choice == "1":
        addition()
    elif menu_choice == "2":
        multiplication()
    elif menu_choice == "3":
        substraction()
    elif menu_choice == "4":
        division()
    elif menu_choice == "5":
        print('Exiting program...')
    else:
        print('Invalid input, returning to main menu...')
        mainmenu()
        
def returnchoice():
    askreturn = input('Return to main menu? (y/n): ')
    if askreturn == 'y':
        print('Returning to main menu...\n')
        mainmenu()
    elif askreturn == 'n':
        print('Exiting program...')
    else:
        print('Invalid input, returning to main menu...')
        mainmenu()

def addition():
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    num_sum = num_1 + num_2
    print(num_sum)
    returnchoice()

def substraction():
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    num_difference = num_1 - num_2
    print(num_difference)
    returnchoice()
    
def multiplication():
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    num_product = num_1 * num_2
    print(num_product)
    returnchoice()
    
def division():
    num_1 = float(input('Enter the first number: '))
    num_2 = float(input('Enter the second number: '))
    num_quotient = num_1 / num_2
    print(num_quotient)
    returnchoice()
    
mainmenu()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    