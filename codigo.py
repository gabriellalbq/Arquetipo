import os
os.system("cls")
import os
import random
import datetime

treinos = []
def exibir_menu():
    print("\n====== SISTEMA DE TREINOS ======")
    print("1. Adicionar Treino")
    print("2. Visualizar Treinos")
    print("3. Editar Treino")
    print("4. Excluir Treino")
    print("5. Acompanhemento da Evolução Pessoal")
    print("6. Sugestões Personalizadas")
    print("7. Confira aqui seu IMC")
    print("8. Sair")
    print("================================")
    return input("Escolha uma opção: ")
def cadastrar_exercicio():
    lista_exercicio = []
    while True:
        nome_ex = input("\nDigite o nome do exercício (ou 'sair' para finalizar): ").lower().strip()
        if nome_ex == "sair":
            break
        
        dado_exercicio = {"Nome": nome_ex.capitalize()}
        
        if nome_ex in ["agachamento", "supino", "abdominal"]:
            dado_exercicio["Séries"] = int(input(" - Digite a quantidade de séries: "))
            dado_exercicio["Repetições"] = int(input(" - Digite o número de repetições: "))
        elif nome_ex in ["natação", "corrida", "ciclismo"]:
            dado_exercicio["Distância"] = int(input(" - Digite a distância percorrida (km): "))
            dado_exercicio["Tempo"] = int(input(" - Digite o tempo total (min): "))
        else:
            dado_exercicio["Detalhes"] = input(" - Informe os detalhes (séries ou tempo): ")
            
        lista_exercicio.append(dado_exercicio)
        print(f" - {dado_exercicio['Nome']} foi adicionado com sucesso!")

    return lista_exercicio
