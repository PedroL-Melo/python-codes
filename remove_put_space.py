name = input('Insira um nome: ')
name  = ' ' + name + ' '
print('\nNome com espaços:')
print('\t"{}"'.format(name))
print('\nNome sem espaço na direita:')
print('\t"{}"'.format(name.rstrip()))
print('\nNome sem espaço na esquerda:')
print('\t"{}"'.format(name.lstrip()))
print('\nNome sem espaços nos lados:')
print('\t"{}"'.format(name.strip()))
print('\nNome sem espaços:')
print('\t"{}"'.format(name.replace(' ', '')))


