
import random

def menu():
    print("\n Menu: ")
    print("(1) Criar Lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")


def crialista():
   N=int(input("insira o número de dígitos da lista:"))
   lis=[random.randint(0,100) for _ in range(N)] 
   print(f"lista criada: {lis} ")
   return lis

def lelista():
    N = int(input("Insira o número de dígitos da lista: "))
    lis = []
    for i in range(1, N + 1):
        num = int(input(f"Introduza o número {i} a ser adicionado à lista: "))  # f-string corrigida
        lis.append(num)
    print(f"lista introduzida: {lis}")
    return lis


def soma(lis):
    return sum(lis)

def media(lis):
    if len(lis)==0:
        return 0
    return soma(lis)/len(lis)

def maiornumero(lis):
    maior=lis[0]
    i=1
    while i<len(lis):
        if lis[i]>maior:
            maior=lis[i]
        i=i+1
    return maior

def menornumero(lis):
    menor=lis[0]
    i=1
    while i<len(lis):
        if lis[i]<menor:
            menor=lis[i]
        i=i+1
    return menor

def ordem_crescente(lis):
    return lis==sorted(lis)

def ordem_decrescente(lis):
    return lis==sorted(lis, reverse=True)

def procurar_elemento(lis, ele):
    if ele in lis:
        return lis.index(ele)
    else:
        return -1
    
def main():
    lis=[]

    while True:
        menu()
        opcao=int(input("Escolha uma opção: "))

        if opcao==1:
            lis=crialista()
        elif opcao==2:
            lis=lelista()
        elif opcao==3:
            print(f"Soma: {soma(lis)}")
        elif opcao == 4:
            if lis:
                print(f"média: {media(lis)}")
            else:
                print("A lista está vazia.")
        elif opcao == 5:
            if lis:
                maior = maiornumero(lis)
                print(f"maior número: {maior}")
            else:
                print("A lista está vazia.")
        elif opcao == 6:
            if lis:
                menor = menornumero(lis)
                print(f"menor número: {menor}")
        elif opcao==7:
            if ordem_crescente(lis):
                print("a lista está em ordem crescente")
            else:
                print("a lista não está em ordem crescente")
        elif opcao==8:
            if ordem_decrescente(lis):
                print("a lista está em ordem decrescente")
            else:
                print("a lista não está em ordem decrescente")
        elif opcao==9:
            ele=int(input("introduza o elemento que quer encontrar: "))
            posicao=procurar_elemento(lis, ele)
            if posicao== -1:
                print("elemento não encontrado")
            else:
                print(f"elemento encontrado na posição {posicao}")
            
        elif opcao==0:
            print(f"lista final: {lis}")
            break

        else:
            print("opção inválida")

if __name__=="__main__":
    main()