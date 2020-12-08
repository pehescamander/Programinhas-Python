continuar = "1"
x = 0
print("CALCULADORA DE REGRA DE 3 PRAS NOTA")
print("Programado por Pedro Henrique Barros Silvério")
print("\n")
print("Ola cansado estudante!!")
print("Como vai?")
while continuar == "1":
    try:
        print("\n")
        n1 = input("Vamos precisar saber quanto vale essa prova/teste/controle/simulado (essa coisa kkkk): ")
        n2 = input("Agora digite quantas questões isso tem: ")
        n3 = input("Pode me dizer quantas vc acertou? ")
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        x = n3 * n1
        x1 = x / n2
        print("\n")
        print("Obrigado, deixa eu descobrir esse bentito X")
        print("\n")
        print("Calculando . . . Nao, nao da tempo nem de respirar!")
        print("\n")
        print("Essa eh facil o Valor de X eh", x1)
        print("\n")
        print("Te desejo um ótimo dia!!")
        print("\n")
    except:
        print("\n")
        print("AAAAAAAAAAAAAAAAAAAAAAH")
        print("Vc deve ter digitado letras e nao me ensinaram a ler NADA.")
        print("Soh sei faze regra de 3 poxa :(")
        print("Vc deve ser um estudante muito cansado mesmo pra fazer isso comigo q SOH CALCULO. :(")
        print("Podemos tentar de novo digitando 1, mas lembre-se sao 3 NUMEROS e soh NUMEROS.")
        print("Os numeros sao 12345678910...")
        print("\n")
    continuar = input("Digite 1 para repetir ou aperte enter pra fechar... ")
    if continuar != "1":
        exit