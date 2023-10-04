salario = float(input("Informe o salário:")) #float usado para numeros decimais

if salario <=3000:
    print("Programador junior")
    #elif em outras linguagens e o else e if, porém no python usamos elif combinado com and,(elif=entao)
elif salario>3000 and salario<=6000:
    print("Programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador Senior")
else:
    print("Gerente de projetos")
