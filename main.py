from cryptography.fernet import Fernet

'''
Andres Yengle
Password Manager
12/7/21
Semester project
'''

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key =  load_key()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            nick, user, passw = data.split()
            print(fer.decrypt(nick.encode()).decode(), ":", "Username:", fer.decrypt(user.encode()).decode(), "Password:", fer.decrypt(passw.encode()).decode())

def add():
    nick_name = input("What would you like the nick name for the account to be? ")
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write( fer.encrypt(nick_name.encode()).decode() + " " + fer.encrypt(name.encode()).decode() + " " + fer.encrypt(pwd.encode()).decode() + "\n" )



while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? press q t quit ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    if mode == "add":
        add()