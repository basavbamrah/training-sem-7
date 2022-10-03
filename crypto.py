from cryptography.fernet import Fernet

print("Enter 10 username and password:")
with open('data.txt', 'w') as fl:
    with open('key.txt', 'w') as fk:
        for i in range(2):
            un = input('Enter  username: ').encode()
            ps = input('Enter password: ').encode()
            key = Fernet.generate_key()
        # fk.seek(i)
            print(key)
            fk.write(key.decode())
            fk.write(' ')
            obj = Fernet(key)
            un = obj.encrypt(un)
            ps = obj.encrypt(ps)
            # fl.seek(i)

            fl.write(un.decode())
            fl.write(':')
            fl.write(ps.decode())
            fl.write(' ')
