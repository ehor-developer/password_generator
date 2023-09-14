import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + '-_'
    forbidden_strings = ['password', '123456','12345678','1234','qwerty', 'password']
    
    while True:
        password = ''.join(random.choice(characters) for _ in range(random.randint(15, 32)))
        if all(forbidden not in password for forbidden in forbidden_strings):
            return password
passwords = [generate_password() for _ in range(10)]

for i, password in enumerate(passwords, start=1):
    print(f"パスワード候補 {i}: {password}")
