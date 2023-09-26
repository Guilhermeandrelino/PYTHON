nome =input("digite seu nome")
sexo =input("digite F ou M")
ec =input("digite CASADA ou S") 
if sexo =="F" and ec == "CASADA":
    tempo_casada = int(input("digite o tempo de casada em anos"))
    print (nome ("é uma mulher casada há {tempo_casada}"))
else:
    print(nome("não é uma mulher casada"))