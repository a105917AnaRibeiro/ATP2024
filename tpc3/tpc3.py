# tpc3
# jogo dos 21 fósforos

import random

def jogo():
    print("Bem-vindo ao jogo dos 21 fósforos")
    print("Regras:Cada jogador (computador ou utilizador), pode tirar 1, 2, 3 ou 4 fósforos quando for a sua vez de jogar")
    print("Os jogadores jogam alternadamente")
    print("**Quem tirar o último fósforo perde!**")

    modo=input("Escolha o modo do jogo: 1-utilizador começa primeiro; 2-jogador começa primeiro")
    while modo not in ['1','2']:
        modo=input("Escolha o modo do jogo: 1-utilizador começa primeiro; 2-jogador começa primeiro")
        

    fosforos=21


    def utilizador_joga(fosforos):
            n=int(input("Utilizador primeiro! Escolha o número de fósforos que deseja retirar"))
            if n in [1, 2, 3, 4] and n<= fosforos:
                return n
            else:
                print("Não é possíivel retirar esse número de fósforos")

    
    def computador_joga(fosforos):
        n=(fosforos-1)%5
        if n==0:
            n = random.randint(1, 4)
        print(f"O computador retirou {n} fósforos.")
        return n
        


# Modo 1: utilizador joga primeiro
    if modo=="1":
        #joga o utilizador
        print("Você começa!!")
        while fosforos>0:
            n=utilizador_joga(fosforos)
            fosforos=fosforos-n 
            print(f"Restam {fosforos} fósforos")

            if fosforos==0:
                print("Você perdeu!")
                break

        #joga o computador
            n=computador_joga(fosforos)
            fosforos=fosforos-n
            print(f"Restam {fosforos} fósforos")

            if fosforos==0:
                print("O computador perdeu!!")
                break 
        
        
# Modo 2: computador joga primeiro 
    else: 
        print("O computador começa primeiro!")
        while fosforos > 0:
            n = computador_joga(fosforos)
            fosforos -= n
            print(f"Restam {fosforos} fósforos.")
            
            if fosforos == 0:
                print("O computador perdeu!")
                break
            
            # Jogada do jogador
            n = utilizador_joga(fosforos)
            fosforos -= n
            print(f"Restam {fosforos} fósforos.")
            
            if fosforos == 0:
                print("Você perdeu! O último fósforo foi seu.")
                break

jogo()