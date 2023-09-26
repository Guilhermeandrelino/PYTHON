preco = float(input("digite o preço"))
codigo= int (input("digite seu codigo"))
if codigo==1:
    valor_pago= preco-(preco*0.10)
elif codigo==2:
    valor_pago= preco-(preco *0.15)
elif codigo==3:
    valor_pago= preco
elif codigo==4:
    valor_pago = preco+(preco*0.10)
else:
    print("codigo invalido, use 1, 2, 3 ou 4")