pizzas = ['calabresa', 'bacon', 'queijo']
for pizza in pizzas:
    print('Eu gosto de pizza de '+ pizza +'!\n')
print('Eu realmente gosto de pizza!')
new_pizzas = pizzas[:]
new_pizzas.append('peperoni')
pizzas.append('pistache')
print(pizzas)
print(new_pizzas)