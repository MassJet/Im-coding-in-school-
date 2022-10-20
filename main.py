from time import sleep
def printheader():
    print("----------------------------------------------------")
    print("   FRENCH TRANSLATOR APP (NO SPECIAL CHARACTERS)")
    print("----------------------------------------------------")


def userinputloop():
    cmdloop = 'Empty'
    while cmdloop != 'x' and cmdloop:
        cmdloop = input('Would you like to [T]ranslate, or E[x]it the app?').lower().strip()
        if cmdloop == 't' or cmdloop == 'translate':
            translate()
        elif cmdloop == 'x' or cmdloop == 'exit':
            print("Thank you for using this translator. ")
            sleep(2)
            print("Closing software.", end='')
            sleep(1)
            print('.',end='')
            sleep(1)
            print('.',end='')
            break
        elif cmdloop != 'x' or cmdloop != 'exit' and cmdloop:
            print(f'Whoops! Invalid documentation occured. "{cmdloop}" is not a valid command.\n')


def main():
    printheader()
    userinputloop()

def translate():
    global cmd
    cmdstr = input('What number will you translate today? Must be number from 1-20.')
    try:
        cmd = int(cmdstr)
    except Exception:
        print(f"Whoops! You have typed in invalid character '{cmdstr}'. input MUST be a number.")
        translate()
    if cmd < 21 and cmd > 0:
        pass
    else:
        print(f"Oops! Number {cmd} is not from 0 to 20. Please try again.")
        translate()
    if cmd == 0:
        print(f'{cmd} in french is zero. ')
        userinputloop()
    if cmd == 1:
        print(f'{cmd} in french is un.')
        userinputloop()
    if cmd == 2:
        print(f'{cmd} in french is deux.')
        userinputloop()
    if cmd == 3:
        print(f'{cmd} in french is trois.')
        userinputloop()
    if cmd == 4:
        print(f'{cmd} in french is quatre.')
        userinputloop()
    if cmd == 5:
        print(f'{cmd} in french is cinq.')
        userinputloop()
    if cmd == 6:
        print(f'{cmd} in french is six.')
        userinputloop()
    if cmd == 7:
        print(f'{cmd} in french is sept.')
        userinputloop()
    if cmd == 8:
        print(f'{cmd} in french is huit.')
        userinputloop()
    if cmd == 9:
        print(f'{cmd} in french is neuf.')
        userinputloop()
    if cmd == 10:
        print(f'{cmd} in french is dix.')
        userinputloop()
    if cmd == 11:
        print(f'{cmd} in french is onze.')
        userinputloop()
    if cmd == 12:
        print(f'{cmd} in french is douze.')
        userinputloop()
    if cmd == 13:
        print(f'{cmd} in french is treize.')
        userinputloop()
    if cmd == 14:
        print(f'{cmd} in french is quatorze.')
        userinputloop()
    if cmd == 15:
        print(f'{cmd} in french is quinze.')
        userinputloop()
    if cmd == 16:
        print(f'{cmd} in french is seize.')
        userinputloop()
    if cmd == 17:
        print(f'{cmd} in french is dix-sept.')
        userinputloop()
    if cmd == 18:
        print(f'{cmd} in french is dix-huit.')
        userinputloop()
    if cmd == 19:
        print(f'{cmd} in french is dix-neuf.')
        userinputloop()
    if cmd == 20:
        print(f'{cmd} in french is vingt.')
        userinputloop()




if __name__ == '__main__':
    main()