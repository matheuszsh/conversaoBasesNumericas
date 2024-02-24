import os
'''Programa de conversão de bases numéricas'''

# -----------FUNÇÃO PRINCIPAL-----------
def main():
    resp = menu()
    limparTerminal()

    while resp < 1 or resp > 2:
        resp = menu()
        limparTerminal()

    if resp == 1 :
        decimalParaBi()
        limparTerminal()
        menu()
    elif resp == 2 :
        print()

# ------------FUNÇÕES SECUNDÁRIAS------------

#---------------FUNÇÕES DE CONVERSÃO------------------
        
# Decimal para binário
def decimalParaBi():
    d = int(input("Digite decimal:"))
    limparTerminal()

    dPrint = d

    binario = ""

    while d > 0:
        binario += str (d % 2)
        d = int (d / 2)

    while len (binario) < 8:
        binario += "0"

    if len (binario) > 8:
        print(f"ATENÇÂO: A representação máxima de decimal em binário de 8bits é 255\n\nBinário MAX: 11111111")
        verMais = int(input("Deseja ver mais adiante disso?\nNão(0) | Sim(1)\n>>:"))
        limparTerminal()

        if verMais == 1:
            print("Além de 8bits:\n")
        else:
            exit(0)

    binario = binario[::-1]# técnica Slicing

    print(f"Decimal:{dPrint}\nBinário:{binario}")

#--------------------------------------------------------------
#Binário para decimal
    
def binarioParaDec():
    bi = int(input("Digite o binário:"))
    limparTerminal()
            

# -------------FUNÇÕES AUXILIÁRES-----------------
    
#função para limpar tela
def limparTerminal():
    tipoSistema = os.name

    #Para Windows
    if tipoSistema == "nt":
        os.system("cls") 
    else:
        os.system("clear") # para Linux/Mac

#função menu 
def menu():
    print("PROGRAMA DE CONVERSÂO DE BASES:\n")
    print("(1) - DECIMAL PARA BINÁRIO")
    print("(2) - BINÁRIO PARA DECIMAL")
    respM = int(input(">>>:"))
    return respM

if __name__ == "__main__":
    main()

