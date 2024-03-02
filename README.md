# Conversão de Bases Numéricas
[![NPM](https://img.shields.io/badge/LICENSE-MIT-MIT
)](https://github.com/matheuszsh/conversaoBasesNumericas/blob/main/LICENSE)

# Sobre o projeto

O projeto é um script simples para realizar conversões entre diferentes bases numéricas. Conta com um menu simples que exibe '4' opções de de bases numéricas: Decimal, Binério, Hexadecimal e Octal. Ao selecionar a opção, o programa exibe todas as conversões para as outras bases não selecionadas.

# Contribuição

O projeto é livre para todos que quiserem contribuir. Veja as implementações pendentes para contribuir.

# Requisitos

Para rodar este projeto, é necessário ter instalado o python3.

'''bash
  git clone https://github.com/matheuszsh/conversaoBasesNumericas
  
  sudo apt install python3
'''

# Funcionalidades

As funcionalidades são divididas em função principal e funções secundárias com suas subfunções(presentes dentro das funções secundárias) e funções auxiliares.

## Função principal

### Função: main()

Dentro desta função, foi inserido o controle de fluxo para acessar cada função secundária/funções de conversão. Após fazer uma chamada da função **menu()** e guardar na variável **resp** para que possa ser utilizada na estrutura de controle de fluxo e acesse as funções de conversão. Ao terminar a sessão das funções de conversão, o programa retorna ao menu chamando a si próprio como uma chamada recursiva. O programa também trata os dados de entrada.

## Funções secundárias/Funções de conversão

### Função: funcDecimal()

A função **funcDecimal** pede para que o usuário digite um número decimal e exibe/print as conversões em: Binário, Octal, Hexadecimal. Dentro desta função, estão presentes outras '3' subfunções: **deParaBi(), deParaOctal(), deParaHexa**. As subfunções presentes na função funcDecimal, convertem o decimal digitado para cada uma das bases numéricas definidas no projeto.

**deParaBi**: Traduz de decimal para binário.  
  
**deParaOctal**: Traduz de decimal para octal.  
  
**deParaHexa**: Traduz de decimal para Hexadecimal.  

### Função: funcBinario()

A função **funcBinario** pede para que o usuário digite um número em binário e exibe/print as conversões em: Decimal, Octal, Hexadecimal. Dentro desta função, estão presentes outras '3' subfunções: **biParaDec(), biParaOctal(), biParaHexa()**. As subfunções presentes na função funcDecimal, convertem o decimal digitado para cada uma das bases numéricas definidas no projeto.

**biParaDec()**: Traduz de binário para decimal  
  
**biParaOctal()**: Traduz de binário para octal  
  
**biParaHexa()**: Traduz de binário para hexadecimal  
  
## Funções pendentes

### Função: funcBinario().biParaOctal()

Esta função deve definir um parâmetro de entrada chamado **argBi** que será passado como argumento o binário digitado pelo usuário guardado na variável **bi**. Deve conter um algoritmo que realize a conversão correta de um número em binário para o seu equivalente em octal. O desenvolvimento do algoritmo fica a critério do desenvolvedor.

### Função: funcOctal()

Esta função está em fase de protótipo e ainda não foi previamente implementada. Deve conter '3' funções denomidadas: octalParaDecimal(), octalParaBi(), octalParaHexa().

**octalParaDecimal**: Traduz de octal para decimal  
**octalParaBi**: Traduz de octal para binério  
**octalParaHexa**: Traduz de octal para hexadecimal  

### Função: funcHexadecimal()

Esta função está em fase de protótipo e ainda não foi previamente implementada. Deve conter '3' funções denomidadas: hexaParaDecimal(), hexaParaBi(), hexaParaOctal().

**hexaParaDecimal**: Traduz de hexadecimal para decimal
**hexaParaBi**: Traduz de hexadecimal para binário
**hexaParaOctal**: traduz de hexadecimal para octal
