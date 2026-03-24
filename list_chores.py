from add_list import vehicles

guests = ['Leon', 'Nilce', 'Linus', 'Álvaro']
print('Olá {}! Você foi convidado pra a minha festa'.format(guests[0]))
print('Olá {}! Você foi convidado pra a minha festa'.format(guests[1]))
print('Olá {}! Você foi convidado pra a minha festa'.format(guests[2]))
print('Olá {}! Você foi convidado pra a minha festa'.format(guests[3]))

i = 2
cannot_go = guests.pop(i)
guests.insert(i, 'Breno')
print('\n' + cannot_go + ' Não poderá comparecer')
print('\nNova lista de convidados:')
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[0]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[1]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[2]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[3]))

print('\nEncontrei uma mesa maior!')
guests.insert(2, 'AuthenticGames')
guests.insert(2, 'JazzGhost')
guests.append('Mikethelink')
# Eu só queria usar um laço de repetição
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[0]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[1]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[2]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[3]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[4]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[5]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[6]))

print('\nA mesa de jantar não vai chegar a tempo!')
removed_guest = guests.pop()
print('\tSinto muito {}! a mesa não vai chegar a tempo' .format(removed_guest))
removed_guest = guests.pop()
print('\tSinto muito {}! a mesa não vai chegar a tempo' .format(removed_guest))
removed_guest = guests.pop()
print('\tSinto muito {}! a mesa não vai chegar a tempo' .format(removed_guest))
removed_guest = guests.pop()
print('\tSinto muito {}! a mesa não vai chegar a tempo' .format(removed_guest))
removed_guest = guests.pop()
print('\tSinto muito {}! a mesa não vai chegar a tempo' .format(removed_guest))

print('\nNova lista de convidados:')
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[0]))
print('\tOlá {}! Você foi convidado pra a minha festa'.format(guests[1]))

del vehicles[0]
del vehicles[1]

print(vehicles)