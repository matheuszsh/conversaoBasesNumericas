import os
'''Programa de conversão de bases numéricas'''

# -----------FUNÇÃO PRINCIPAL-----------
def main():
    try :
        resp = menu()
        limparTerminal()


        while resp < 1 or resp > 4:
            resp = menu()
            limparTerminal()

        if resp == 1 :
            funcDecimal()
            
        elif resp == 2 :
            funcBinario()

        elif resp == 3 :
            funcOctal()
        
        elif resp == 4 :
            funcHexadecimal()
        
        # Reuso de recurso
        input("Aperte a tecla ENTER para prosseguir")
        limparTerminal()
        main()
    
    except:
        input("Erro: algo deu errado. Aperte ENTER para voltar ao menu.")
        limparTerminal()
        main()

# ------------FUNÇÕES SECUNDÁRIAS------------

#---------------FUNÇÕES DE CONVERSÃO------------------
        
# FUNÇÃO DECIMAL
def funcDecimal():
    d = int(input("Digite decimal:"))
    limparTerminal()

    # SUBFUNÇÃO - DECIMAL PARA BINÁRIO
    def deParaBi(argDe):

        binario = ""

        # calcula o decimal diluindo (/) o binário após obter o primeiro resto da divisão (0 ou 1) (%)
        while argDe > 0:
            binario += str (argDe % 2)
            argDe = int (argDe / 2)

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
        return binario

    # SUBFUNÇÃO - DECIMAL PARA OCTAL
    def deParaOctal(argDe):
        
        octal = ""

        while argDe > 0:
            octal += str (argDe % 8)
            argDe = int (argDe / 8)

        octal = octal[::-1]

        return octal

    # SUBFUNÇÃO - DECIMAL PARA HEXADECIMAL
    def deParaHexa(argDe):
        hexAuxiliar = "0123456789ABCDEF"
        hexadecimal = ""

        while argDe != 0:
            hexadecimal += hexAuxiliar[(argDe % 16)] # pega a posição em hexAuxiliar
            argDe = int (argDe / 16)

        hexadecimal = hexadecimal[::-1]

        return hexadecimal

    print(f"Decimal:{d}\n\nBinário:{deParaBi(d)}\n\nOctal:{deParaOctal(d)}\n\nHexadecimal:{deParaHexa(d)}\n\n")


#--------------------------------------------------------------
# FUNÇÃO BINÁRIO
    

def funcBinario():
    # pede o número em binário
    bi = str(input("Digite o binário:"))
    limparTerminal()
    
    # SUBFUNÇÃO - BINÁRIO PARA DECIMAL
    def biParaDec(argBi):
        # inverte a string para ler da esquerda para direita >>>>
        argBi = argBi[::-1]# técnica Slicing
        
        decimal = 0
        n = 0
        
        # verifica se cada caracter é igual a '1', e caso for, realiza o calculo binário
        for b in argBi:
            if (b == '1'):
                decimal += 2 ** n
        
            n += 1
        
        return decimal

    # EM DESENVOLVIMENTO - DESFUNCIONAL           
    """def biParaOctal(argBi):
        argBi = argBi[::-1]

        octalAuxiliar = ""
        octal = 0
        n = 0

        for b in argBi:
            if b == '1':
                if n < 3:
                    octal += 2 ** n

            if (n == 3):
                octalAuxiliar += str (octal)
                octal = 0
                n = 0

            n += 1
            
        octalAuxiliar = str (octal) + octalAuxiliar

        return octalAuxiliar"""

    def biParaHexa(argBi):
        argBi = argBi[::-1]

        # Separando Strings em blocos de 4 bits
        argBi2 = argBi[0:4]
        argBi1 = argBi[4:8]

        # Variáveis auxiliares
        hexAuxiliar = "0123456789ABCDEF"
        hexadecimalN = 0

        hexaFinal = ""

        n = 0

        # Transformando primeiro bloco
        for b1 in argBi1:
            if (b1 == '1'):
                hexadecimalN += 2**n

            n += 1

        hexaFinal += hexAuxiliar[hexadecimalN]

        hexadecimalN = 0

        n = 0

        # Transformando o segundo bloco
        for b2 in argBi2:
            if (b2 == '1'):
                hexadecimalN += 2**n

            n += 1

        hexaFinal += hexAuxiliar[hexadecimalN]

        return hexaFinal
    

    print(f"Binário:{bi}\n\nDecimal:{biParaDec(bi)}\n\nHexadecimal: {biParaHexa(bi)}\n\n")

#----------------------------------------------------------------
# FUNÇÃO OCTAL          

def funcOctal():
    print(f"Octal: Em desenvolvimento.")

#----------------------------------------------------------------
# FUNÇÃO HEXADECIMAL

def funcHexadecimal():
    print(f"Hexadecimal: Em desenvolvimento.")

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
    print("<---> PROGRAMA DE CONVERSÂO DE BASES <--->\n")
    print("Deseja transformar:")
    print("(1) - DECIMAL")
    print("(2) - BINÁRIO")
    print("(3) - OCTAL")
    print("(4) - HEXADECIMAL")
    respM = int(input(">>>:"))
    return respM

if __name__ == "__main__":
    main()

