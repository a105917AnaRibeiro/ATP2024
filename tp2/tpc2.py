
# jogo utilizador adivinha número gerado  pelo computador

import random

def utilizador_adivinha():
    numero_computador = random.randint(0, 100) 
    tentativas = 0  
    
    while True:
        numero_utilizador = int(input("Advinha um número entre 0 e 100: ")) 
        tentativas += 1  
    
        if numero_utilizador < 0 or numero_utilizador > 100:
                print("Número é inválido")
        elif numero_utilizador < numero_computador:
                print("O número que pensei é maior...")
        elif numero_utilizador > numero_computador:
                print("O número que pensei é menor...")
        else:
                print(f"Parabéns! O número que pensei foi {numero_computador}. Tentativas: {tentativas}")
                break 



# jogo computador adivinha número gerado pelo utilizador

def computador_adivinha():
       tentativas=0
       menor=0
       maior=100
       print("Pense num número entre 0 e 100")

       while True:
        tentativas=tentativas+1
        palpite_computador=(menor+maior)//2
        print(f"Acho que o número é {palpite_computador}")
        resposta = input("Responda com 'Acertou', 'Maior' ou 'Menor': ").strip().lower()

        if resposta=="acertou":
              print(f"Resposta correta! O número era {palpite_computador}. Tentativas: {tentativas}")
              break
        elif resposta == "maior":
            menor = palpite_computador + 1
        elif resposta == "menor":
            maior = palpite_computador - 1
        else:
            print("Por favor, responda com 'Acertou', 'Maior' ou 'Menor'.")
        


def jogo_adivinha_numero():
    print("Bem-vindo ao jogo 'Adivinha o Número'. Opção 1: Computador escolhe, utilizador adivinha. Opção 2: Utilizador escolhe, computador adivinha") 

    while True:
        opcao = input("Digite 1 ou 2 para escolher a modalidade: ").strip()

        if opcao == "1":
            utilizador_adivinha()  # Inicia o jogo utilizador adivinha
            break
        elif opcao == "2":
            computador_adivinha()  # Inicia o jogo computador adivinha
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    jogo_adivinha_numero()
