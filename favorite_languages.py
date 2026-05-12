favorite_languages = { #a ordem é key, value
#chave: valor
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name, language in favorite_languages.items():
    print("A linguage favorita de " + name.title() + " é " + language.title() + ".")

#percorrer as chaves é um comportamento padrão de um dicionário, então não é necessário usar o método keys() para obter as chaves. O código abaixo tem o mesmo resultado do código acima.
#for name in favorite_languages:
for names in favorite_languages.keys():
    print(names.title())