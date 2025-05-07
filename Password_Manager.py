from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open('key.key', 'rb') as key_file:
        return key_file.read()

# Run this ONCE to generate the key
write_key()

key = load_key()
fer = Fernet(key)

def view():
    with open('password.txt', 'r') as f:
        for line in f:
            user, encrypted_pass = line.strip().split('|')
            decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
            print('User:', user, '| Password:', decrypted_pass)

def add():
    user = input('User name: ')
    password = input('Password: ')
    encrypted_password = fer.encrypt(password.encode()).decode()

    with open('password.txt', 'a') as f:
        f.write(user + '|' + encrypted_password + '\n')

while True:
    mode = input('Add a password or view passwords? (add/view) or q to quit: ').lower()

    if mode == 'q':
        break
    elif mode == 'add':
        add()
    elif mode == 'view':
        view()
    else:
        print('Invalid choice.')
