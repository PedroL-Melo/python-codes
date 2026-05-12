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

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print("Ola "+ name.title() + ", eu vej que sua linguagem favrita é " + language.title() + "!")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", obrigado por participar da pesquisa.")