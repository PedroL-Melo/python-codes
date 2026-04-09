current_users = ['pedro', 'renato', 'estevão', 'ester', 'arthur']
new_users = ['PEDRO', 'esther', 'Aline', 'Arthur']
for user in new_users:
    user = user.lower()
    if user not in current_users:
        print('Criando seu usuário...')
        current_users.append(user)
    else:
        print('nome de usuario indisponivel')