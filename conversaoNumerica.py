import os
'''Programa de conversão de bases numéricas'''

# -----------FUNÇÃO PRINCIPAL-----------
def main():
    try :
        resp = menu()
        limparTerminal()

        while resp < 1 or resp > 2:
            resp = menu()
            limparTerminal()

        if resp == 1 :
            decimalParaBi()
            input("Aperte a tecla ENTER para prosseguir")
            limparTerminal()
            main()
            
        elif resp == 2 :
            binarioParaDec()
            input("Aperte a tecla ENTER para prosseguir")
            limparTerminal()
            main()
    
    except:
        input("Erro: algo deu errado. Aperte ENTER para voltar ao menu.")
        limparTerminal()
        main()
        

# ------------FUNÇÕES SECUNDÁRIAS------------

#---------------FUNÇÕES DE CONVERSÃO------------------
        
# Decimal para binário
def decimalParaBi():
    d = int(input("Digite decimal:"))
    limparTerminal()

    dPrint = d

    binario = ""

    # calcula o decimal diluindo (/) o binário após obter o primeiro resto da divisão (0 ou 1) (%)
    while d > 0:
        binario += str (d % 2)
        d = int (d / 2)

    # Adiciona ao binário o numero '0' caso esteja faltando, para completar 8 bits
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

    binario = binario[::-1]# técnica Slicing / inverte a string

    print(f"Decimal:{dPrint}\nBinário:{binario}")

#--------------------------------------------------------------
#Binário para decimal
    
def binarioParaDec():
    # pede o número em binário
    bi = str(input("Digite o binário:"))
    limparTerminal()
    
    # inverte a string para ler da direita pra esquerda
    bi = bi[::-1]# técnica Slicing
    
    decimal = 0
    n = 0
    
    # verifica se cada caracter é igual a '1', e caso for, realiza o calculo binário
    for b in bi:
        if (b == '1'):
            decimal += 2 ** n
    
        n += 1
            
    print(f"Binário:{bi}\nDecimal:{decimal}")
            

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

