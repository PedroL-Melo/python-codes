text = input('informe uma frase: ')
print(text.rstrip())# remove do lado direito
# para remover permanentemente é nescessário utilizar o metodo direto na variavel
# text = text.rstrip()
# print(text)
print(text.lstrip())# remove do lado esquerdo
print(text.strip())# remove de todos os lados
print(text.replace(' ', '' ))# remove todos os espaços
