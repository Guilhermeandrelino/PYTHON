n_ident=int(input("digite um numero de identificaçao"))
n1=float(input("digite uma nota"))
n2=float(input("digite uma nota"))
n3=float(input("digite uma nota"))
m_exe=int(input("digite uma nota"))
MA =(n1 + n2 * 2 + n3 * 3 + m_exe)/7 
if MA>=90:
    print("aprovado")
elif MA >=75:
    print("aprovado")
elif MA >=60:
    print("aprovado")
elif MA >=40:
    print("reprovado")
else:
    print("reprovado")