users = ['pedro', 'renato', 'estevão', 'ester', 'admin']
#users = []
if users:
    for user in users:
            if user == 'admin': print('Olá admin, oq voce gostaria de ver hoje')
            else: print('Seja bem vindo {}'.format(user))
else:
    print('Precisamos encontrar alguns usuarios')