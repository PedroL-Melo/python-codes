favorite_languages = { #a ordem é key, value
#chave: valor
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name, language in favorite_languages.items():
    print("A linguage favorita de " + name.title() + " é " + language.title() + ".")

for names in favorite_languages.keys():
    print(names.title())