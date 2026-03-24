vehicles = ['Carro', 'Moto', 'Bicicleta']
print(vehicles)
vehicles.append('Avião')# concatena
print(vehicles)
vehicles.insert(0, 'Helicoptero')# insere no lugar que voce quiser
print(vehicles)
del vehicles[0]# exclui permanentemente
print(vehicles)
popped_vehicles = vehicles.pop()# remove o ultimo item da lista, no caso, avião. Se botar um numero ele remove tbm ex .pop(0) 1 2 3 etc
print(vehicles)
print(popped_vehicles)
too_dangerous = 'Moto'
vehicles.remove(too_dangerous)# remove de acordo com o valor
print(vehicles)
print(too_dangerous + ' é muito perigoso pra mim!')
#Nota: o metodo remove() remove apenas a primeira ocorrencia do valor

