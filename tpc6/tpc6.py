
def inserir_aluno(nome, id, notas):
    return(nome, id, notas)

def listar_aluno(turma):
    print("\nLista de Alunos: ")
    for aluno in turma:
        print(f"Nome:{aluno[0]}, ID: {aluno[1]}, Notas {aluno[2]}")

def aluno_por_id(turma, id):
    for aluno in turma:
        if aluno[1]==id:
            return aluno
    return None

def guardar_ficheiro_turma(turma, filename):
        with open(filename, 'w') as f:
            for aluno in turma:
                f.write(f"{aluno[0]},{aluno[1]},{aluno[2][0]},{aluno[2][1]},{aluno[2][2]}\n")
        print("Turma guardada com sucesso.")

def carregar_turma(filename):
    turma = []
    with open(filename, 'r') as f:
        for line in f:
            nome, id, nota1, nota2, nota3 = line.strip().split(',')
            notas = [float(nota1), float(nota2), float(nota3)]
            turma.append(inserir_aluno(nome, id, notas))
    
    print("Turma carregada com sucesso.")
    return turma

def main():
    turma = []

    while True:
        print("\nMenu de Opções:")
        print("1: Criar uma turma")
        print("2: Inserir um aluno na turma")
        print("3: Listar a turma")
        print("4: Consultar um aluno por ID")
        print("8: Guardar a turma em ficheiro")
        print("9: Carregar uma turma de um ficheiro")
        print("0: Sair da aplicação")
        
        opcao = int(input("Opção: "))

        if opcao == 1:
            turma = []  # Reinicia a turma
            print("Turma criada...")

        elif opcao == 2:
            nome = input("Nome do aluno: ")  # Corrigido para string
            id = input("ID do aluno: ")
            notas = []
            for i in range(3):
                nota = float(input(f"Nota {i + 1}: "))
                notas.append(nota)
            turma.append(inserir_aluno(nome, id, notas))  # Adiciona aluno à turma
            print(f"Aluno {nome} inserido com sucesso.")

        elif opcao == 3:
            listar_aluno(turma) 

        elif opcao == 4:
            id = input("ID do aluno que deseja encontrar: ")
            aluno = aluno_por_id(turma, id)
            if aluno:
                print(f"Aluno encontrado: Nome: {aluno[0]}, ID: {aluno[1]}, Notas: {aluno[2]}")
            else:
                print("Aluno não encontrado.") 
        
        elif opcao == 8:
            filename = input("Digite o nome do ficheiro para guardar a turma: ")
            guardar_ficheiro_turma(turma, filename)
        
        elif opcao == 9:
            filename = input("Digite o nome do ficheiro para carregar a turma: ")
            turma = carregar_turma(filename)
        
        elif opcao == 0:
            print("Saindo da aplicação.")
            break

        else:
            print("Opção inválida.")



if __name__ == "__main__":
    main()
