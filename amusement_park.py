age = 19
preco: float
if age <= 4:
    preco = 0.00
elif age <= 18:
    preco = 5.00
else:
    preco = 10.00
print('O valor da sua entrada é R${}' .format(preco))