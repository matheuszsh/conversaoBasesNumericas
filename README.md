# Conversão de Bases Numéricas
[![NPM](https://img.shields.io/badge/LICENSE-MIT-MIT
)](https://github.com/matheuszsh/conversaoBasesNumericas/blob/main/LICENSE)

# Sobre o projeto

O projeto é um script simples para realizar conversões entre diferentes bases numéricas. Conta com um menu simples que exibe '4' opções de de bases numéricas: Decimal, Binério, Hexadecimal e Octal. Ao selecionar a opção, o programa exibe todas as conversões para as outras bases não selecionadas.

# Funcionalidades

As funcionalidades são divididas em função principal e funções secundárias com suas subfunções(presentes dentro das funções secundárias) e funções auxiliares.

## Função principal

## Função: main()

Dentro desta função, foi inserido o controle de fluxo para acessar cada função secundária/funções de conversão. Após fazer uma chamada da função *menu()* e guardar na variável *resp* para que possa ser utilizada na estrutura de controle de fluxo e acesse as funções de conversão. Ao terminar a sessão das funções de conversão, o programa retorna ao menu chamando a si próprio como uma chamada recursiva. O programa também trata os dados de entrada.
