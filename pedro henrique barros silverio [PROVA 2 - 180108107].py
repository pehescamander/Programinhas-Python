print ("""
Programado por Pedro Henrique (18/108107) - Lingua e Programação.
Insira uma frase e ele contará os espaços e vogais. 
""")
continuar = "1"
while continuar == "1":
    vogais = 0
    espaços = 0
    frase = input("Digite a frase: ")
    frase = frase.lower();
    for p in range(0, len(frase)):
        if frase[p] in ("aáâeéêiíoôóuú"):
            vogais = vogais + 1;
        elif frase[p] in (" "):
            espaços = espaços + 1;
    print("Na frase", frase.upper(), "temos", vogais, "vogais e", espaços, "espaços.")
    continuar = input("Digite 1 para continuar ou só aperte enter para sair... ")
    if continuar != "1":
        exit