available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for topping in requested_toppings:
    if topping in available_toppings:
        print('Adicionando {} na pizza'.format(topping))
    else:
        print('O topping que voce pediu, nao estã disponivel!')