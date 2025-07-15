import funcoes
import questoes
from colorama import Fore, Back, Style, init
init()

print("Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!")

nome = input("Qual seu nome? ")
print("")
nome = nome.upper()

print(f"Ok {nome}, você tem direito a pular 3 vezes e 2 ajudas!")
print("As opções de resposta são ""A"", ""B"", ""C"", ""D"", ""ajuda"", ""pula"" e ""parar""! ")

print("")
enter = input("Aperte ENTER para continuar...")


print('''O jogo já vai começar! Lá vem a primeira questão!
      
Vamos começar com questões do nível FACIL!  
      ''')
enter = input("Aperte ENTER para continuar...")

nivel = 'facil'
lista_jaforam = []
lista_quest = questoes.quest

lista_dinheiro = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000] 
lista_ajudas = [0] * 10 
pulos = 3 
ajudas = 2 
opcoes_validas = ["A", "B", "C", "D", "ajuda", "pula"]
ajuda_pula = ["ajuda", "pula"]
ide = 1 

while ide <= 9:
    dicio_nivel = funcoes.transforma_base(lista_quest)
    nova_questao = funcoes.sorteia_questao_inedita(dicio_nivel, nivel, lista_jaforam)
    formatacao_questao = funcoes.questao_para_texto(nova_questao, ide)
    
    lista_jaforam.append(nova_questao)
    validacao = funcoes.valida_questao(nova_questao)

    if validacao != {}:
        print(Fore.RED + "Questão inválida, encerra-se o programa então")
        exit()
    while True:
        print(Fore.GREEN + formatacao_questao)

        resposta_correta = nova_questao['correta']

        resposta = input(Fore.BLUE + "Qual sua resposta?!")

        while resposta not in opcoes_validas:
            print(Fore.RED + "Opção inválida!")
            print(Fore.LIGHTYELLOW_EX + "As opções de resposta são ""A"", ""B"", ""C"", ""D"", ""ajuda"", ""pula"" e ""parar""! ")
            resposta = input(Fore.BLUE + "Qual sua resposta?!")  

        if resposta == 'ajuda' and ajudas > 0 and lista_ajudas[ide] == 0:
            ajudas -= 1 
            lista_ajudas[ide] += 1 
            dica = funcoes.gera_ajuda(nova_questao)
            if ajudas > 0:
                print(f"Ok, lá vem ajuda! Você ainda tem {ajudas} ajudas!")
            else:
                print(Fore.LIGHTYELLOW_EX + "Ok, lá vem ajuda! ATENÇÃO: Você não tem mais direito a ajudas!")
            enter = input("Aperte ENTER para continuar...")
            print(dica)
            enter = input("Aperte ENTER para continuar...")
            continue


        if resposta == 'ajuda' and ajudas > 0 and lista_ajudas[ide] == 1:
            print(Fore.RED + "Não deu! Você já pediu ajuda nesta questão!")
            enter = input("Aperte ENTER para continuar...")
            continue
        
        if resposta == 'ajuda' and ajudas == 0:
            print(Fore.RED + "Não deu! Você não tem mais direito a ajuda!")
            enter = input("Aperte ENTER para continuar...")
            continue

        if resposta == 'pula' and pulos > 0:
            pulos -= 1 
            if pulos >= 1:
                print(f"Ok, pulando! Você ainda tem {pulos} pulos!")
            else:
                print(Fore.LIGHTYELLOW_EX + "Ok, pulando! ATENÇÃO: Você não tem mais direito a pulos!")
            enter = input("Aperte ENTER para continuar...")
            break 

        if resposta == 'pula' and pulos == 0:
            print(Fore.RED + "Não deu! Você não tem mais direito a pulos!")
            continue
        
        if resposta != "ajuda" and resposta != "pula":

            if resposta == resposta_correta:
                print("")
                print(Fore.GREEN + f"Você acertou! Seu prêmio atual é de R$ {lista_dinheiro[ide - 1]:.2f}")
                print("")
                ide += 1 
                if ide > 3 and ide < 6:
                    nivel = 'medio'
                    if ide == 4:
                        print("HEY! Você passou para o nível MEDIO!")
                if ide > 6:
                    nivel = 'dificil'
                    if ide == 7:
                        print("HEY! Você passou para o nível DIFICIL!")
                break
            elif resposta != resposta_correta:
                print(Fore.RED + "Que pena! Você errou e vai sair sem nada :( ")
                exit()
            enter = input("Aperte ENTER para continuar...")

print("PARABÉNS, você zerou o jogo e ganhou um milhão de reais! ")
