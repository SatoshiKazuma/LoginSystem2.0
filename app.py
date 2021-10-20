from Fun_class import *

print('''
Welcome!
This is a demonstration of a user account system
Type "su" to sign up and "si" to sign in''')
try:
    initial = input('Signin/Signup: ').lower()
    print(initial)
    if initial in ['si', 'su']:
        if initial == 'su':
            with open('userdata.csv', 'r') as userdata:
                reader = csv.DictReader(userdata)
                accept = False
                while not accept:
                    gusername = input('Enter a username: ')
                    for row in reader:
                        if gusername == row['username']:
                            print('Username already exists')
                            break
                    else:      
                        gemail = input('Enter an email address: ')
                        gpassword = input('Enter your new password: ')
                        nuser = User(gusername,gemail,gpassword)
                        nuser.signup()
                        accept = True

        elif initial == 'si':
            usernameg = input('Username:')
            passwordg = input('Password: ')
            euser = User(usernameg, 0, passwordg)
            euser.signin()
    else:
        print('Invalid input\nType "su" to sign up and "si" to sign in')
except KeyboardInterrupt:
    print('\n\nYou have forcefully quit the program')