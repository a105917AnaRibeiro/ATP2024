cinema=[]
sala=(int, list, str)

def inserirsala( cinema, sala ):
    for s in cinema:
        if s[2] == sala[2]:  # Compara o nome do filme
            print(f"Sala já existe para o filme: {sala[2]}.")
            return cinema
    cinema.append(sala)
    return cinema

def listar(cinema):
    print("................ Lista de Filmes em Exibição ................")
    for sala in cinema:
        print(f"- {sala[2]}")

def disponivel( cinema, filme, lugar ):
    cond=True
    for sala in cinema:
        if sala[2]==filme:
            if lugar in sala[1]:
                cond= False
    return cond

def vendebilhete( cinema, filme, lugar):
    for sala in cinema:
        if sala[2]==filme:
            if disponivel(cinema, filme, lugar):
                sala[1].append(lugar)
    return cinema

def listardisponibilidade(cinema):
    for sala in cinema:
        n_lugares=sala[0]
        n_vendidos=len(sala[1])
        n_disponiveis=n_lugares-n_vendidos
    print(f"filme: {sala[2]}, lugares disponíveis: {n_disponiveis}")

def menu():
    cinema=[]
    while True:
        print("\n Menu:") 
        print("(1) Inserir Sala")
        print("(2) Listar Filmes")
        print("(3) Verificar Disponibilidade")
        print("(4) Vender Bilhete")
        print("(5) Listar Disponibilidade")
        print("(0) Sair")
   
        opcao=int("escolha uma opção: ")

        if opcao==1:
            n_lugares=int(input("Número de Lugares: "))
            filme=input("Nome de Filme: ")
            sala=(n_lugares, [], filme)
            cinema=inserirsala(cinema, sala)
        
        if opcao==2:
            listar(cinema)

        if opcao==3:
            filme=input("Nome do Filme: ")
            lugar=int(input("Número do Lugar: "))
            if disponivel(cinema, filme, lugar):
                print("lugar disponível")
            else:
                print("lugar não disponível")

        if opcao==4:
            filme=input("Nome do Filme: ")
            lugar=int(input("Número do Lugar: "))
            cinema=vendebilhete(cinema, sala, lugar)

        if opcao==5:
            listardisponibilidade(cinema)

        if opcao==6:
            break

        else:
            print("Opção inválida...")


# Execução do menu
if __name__ == "__main__":
    menu()


