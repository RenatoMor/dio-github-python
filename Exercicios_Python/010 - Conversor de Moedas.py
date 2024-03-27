# Programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

real = float(input("Quanto dinheiro você tem na carteira? R$"))
dólar = real / 3.85
print(("Com R${:.2f} você pode comprar ${:.2f}".format(real, dólar)))
