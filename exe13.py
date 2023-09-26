salario=float(input("digite o seu salario"))
if salario<=1903:
    print(salario)
elif salario<=2826:
    pag= salario-(salario* 0.075)
    print (pag)
elif salario<=3751:
    pag= salario-(salario* 0.15)
    print (pag)
elif salario<= 4664:
    pag= salario-(salario* 0.225)
    print (pag)
elif salario>= 4664:
    pag= salario-(salario* 0.275)
    print (pag)
else:
    print("recebe mais que o valor")