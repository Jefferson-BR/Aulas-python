nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade aqui: "))

if idade > 90:
    print(f"Erro! idade fora de cogitação")

if idade >= 18 and idade <= 90:
    print(f"Olá {nome.title()}, você já tem idade para tirar sua carteira de habilitação!")

if idade >= 0 and idade <= 17:
    print(f"{nome.title()}, infelizmente você ainda não pode tirar sua habilitação por ser menor de idade.")
    
else:
    print('')