import csv 

class User:
    def __init__(self,username,email,password) -> None:
        self.username = username
        self.email = email
        self.password = password

    def signup(self):
        confirmpassword = input('Confirm password: ')
        if confirmpassword == self.password:
            inputdata = [self.username, self.email, self.password]
            with open('userdata.csv', 'a') as userdata:
                writer = csv.writer(userdata)
                writer.writerow(inputdata)
                print('Account created')
        else:
            print('passwords do not match')

    def signin(self):
        with open('userdata.csv', 'r') as userdata:
            reader = csv.DictReader(userdata)
            for row in reader:
                if (self.username,self.password) == (row['username'],row['password']):
                    print('Signed in')
                    break
            else:
                print('Credentials do not match')

                
                