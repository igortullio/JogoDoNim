def computador_escolhe_jogada(n, m):
    return valor

def usuario_escolhe_jogada(n, m):
    valor = int(input("\nQuantas peças você vai tirar? "))
    while valor > m or valor < 0:    
        print("Oops! Jogada inválida! Tente de novo.")
        valor = int(input("\nQuantas peças você vai tirar? "))        
    return valor

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    valor = 0
    
    if (n % m+1) == 0:
        print("Você pode começar...")
        valor = usuario_escolhe_jogada(n, m)
    else:
        print("O computador começa!")
            

def campeonato():
    quantidade_partida = 1
    placar_computador = placar_usuario = 0
    
    while quantidade_partida < 4:
        print("**** Rodada", quantidade_partida ,"****\n")
        partida()
        quantidade_partida = quantidade_partida + 1
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você", placar_usuario, "X", placar_computador, "Computador")

def main():
    print("Bem-vindo ao jogo do NIM!")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    
    escolha = int(input("Escolha: "))    
    while escolha != 1 and escolha != 2:
        print("Escolha uma opção válida!")
        escolha = int(input("Escolha: "))
        
    if escolha == 1:
        print("\nVocê escolheu uma partida isolada!\n")
        partida()
    else:
        print("\nVocê escolheu um campeonato!\n")
        campeonato()
    
    
