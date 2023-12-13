# Solicita que o usúario digite um número
escolha_de_numero = int(input("Qual tabuada você quer saber ? Digite Aqui: "))

funcaoContador = 0


# O Bloco abaixo verifica se o número escolhido é negativo. Se for, o código multiplica o número por -1 para torná-lo positivo e armazena o sinal de negativo na variável `negativo`.
if escolha_de_numero < 0:
    escolha_de_numero *= -1
    negativo = "-"
else:
    negativo = ""


# O Bloco abaixo entra em um loop while que continuará enquanto `funcaoContador` for menor ou igual a 10. Isso significa que o loop será executado 11 vezes, começando em 0 e terminando em 10.
while funcaoContador <= 10:
    resultado = escolha_de_numero * funcaoContador
    print(f"{negativo}{escolha_de_numero} x {funcaoContador} = {negativo}{resultado}")
    funcaoContador += 1 #  Esta linha incrementa o valor da variável `funcaoContador` em + 1
