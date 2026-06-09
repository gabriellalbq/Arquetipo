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

def cadastrar_meta(metas_do_treino):
    meta = input("\nDigite sua meta: ")
    objetivo = input("Digite seu objetivo: ")
    
    nova_meta = {
        "Nome": meta,
        "Objetivo": objetivo,
        "Progresso": 0
    }
    metas_do_treino.append(nova_meta)
    print("Meta e objetivos cadastrados com sucesso para este treino!")

def listar_metas(metas_do_treino):
    print("\n- METAS ATUAIS DESTE TREINO:")
    if not metas_do_treino:
        print("Nenhuma meta cadastrada para este treino!")
        return False
        
    for i, met in enumerate(metas_do_treino, start=1):
        print(f"{i}ª Meta: {met['Nome']} | Objetivo: {met['Objetivo']} | Progresso: {met['Progresso']}%")
    return True
    def atualizar_progresso(metas_do_treino):
    if not listar_metas(metas_do_treino):
        return
    try:
        opcao_escolhida = int(input("\nEscolha o número da meta que deseja atualizar: ")) - 1

        if 0 <= opcao_escolhida < len(metas_do_treino):
            while True:
                novo_progresso = input("Digite o novo progresso (%): ")
                try:
                    novo_progresso = int(novo_progresso)
                    if novo_progresso < 0 or novo_progresso > 100:
                        print(" - Erro: Digite um valor entre 0 e 100!")
                        continue
                    break 
                except ValueError:
                    print(" - Erro: Digite apenas números inteiros!")
            
            metas_do_treino[opcao_escolhida]["Progresso"] = novo_progresso
            print(" - Progresso atualizado com sucesso!")
        else:
            print(" - Número de meta inválido!")
            
    except ValueError:
        print(" - Entrada inválida! Digite um número.")

def controle_metas(metas_do_treino):
    while True:
        print("\n==== CONTROLE DE METAS ====")
        print("1- Cadastrar Nova Meta")
        print("2- Listar Metas Existentes")
        print("3- Atualizar Progresso")
        print("4- Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_meta(metas_do_treino)
        elif opcao == "2":
            listar_metas(metas_do_treino)
        elif opcao == "3":
            atualizar_progresso(metas_do_treino)
        elif opcao == "4":
            break
        else:
            print(" - Opção inválida!")
