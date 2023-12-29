from termcolor import colored

while True:
    idade = int(input("Por favor, insira sua idade ou digite 0 para sair: "))
    if idade >= 18:
        print(colored("Você tem idade suficiente para votar!", "blue"))
    if idade == 0:
        print("Obrigado por usar nosso sistema!")
else:
    print(colored("Desculpe você ainda não pode votar", "red"))