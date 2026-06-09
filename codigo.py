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

def salvar_treino(treinos):
    with open("treinos.txt", "w", encoding="utf-8") as arquivo:
        for i, t in enumerate(treinos):
            arquivo.write(f"{i+1}º Treino - {t['nome']}\n")
            arquivo.write(f"Tipo: {t['tipo']} \nData: {t['data']} \nDuração: {t['duracao']} min \nObjetivo: {t['objetivo']}\n")
            
            if len(t["exercicios"]) > 0:
                arquivo.write("Exercícios: ")
                for ex in t['exercicios']:
                    arquivo.write(f"\n  - {ex['Nome']}")
                    if "Distância" in ex: arquivo.write(f" | Distância: {ex['Distância']} km")
                    if "Tempo" in ex: arquivo.write(f" | Tempo: {ex['Tempo']} min")
                    if "Séries" in ex: arquivo.write(f" | Séries: {ex['Séries']}")
                    if "Repetições" in ex: arquivo.write(f" | Repetições: {ex['Repetições']}")
                    if "Detalhes" in ex: arquivo.write(f" | Detalhes: {ex['Detalhes']}")

            if "metas" in t and len(t["metas"]) > 0:
                arquivo.write("\nMetas: ")
                for j, met in enumerate(t['metas'], start=1):
                    arquivo.write(f"\n  - {j}ª Meta: {met['Nome']} | Objetivo: {met['Objetivo']} | Progresso: {met['Progresso']}%")
            
            arquivo.write("\n" * 3)

        arquivo.write("====== 📈 EVOLUÇÃO PESSOAL 📉 ======\n")
        if not treinos:
            arquivo.write(" - Sem dados suficientes! Adicione treinos primeiro.\n")
        else:
            total_treinos = len(treinos)
            arquivo.write(f"• Total de treinos realizados: {total_treinos}\n")
            
            soma_progresso = 0
            total_metas = 0
            for t in treinos:
                if "metas" in t:
                    for m in t["metas"]:
                        soma_progresso += m["Progresso"]
                        total_metas += 1
                        
            if total_metas > 0:
                media_progresso = soma_progresso / total_metas
                arquivo.write(f"• Progresso médio das suas metas: {media_progresso:.1f}%\n")
            else:
                arquivo.write("• Progresso de metas: Nenhuma meta vinculada aos treinos cadastrados.\n")
            
            arquivo.write(f"• Dias ativos com registro no Arquétipo: {len(treinos)} dia(s)\n")
        
        if treinos:
            arquivo.write("\n======💡 SUGESTÃO PERSONALIZADA ATUAL 💡======\n")
            ultimo_treino = treinos[-1]
            tipo_treino = ultimo_treino['tipo'].lower()
            arquivo.write(f"Com base no seu último treino de ({ultimo_treino['tipo']}):\n")

            if "musculação" in tipo_treino or "funcional" in tipo_treino:
                sugestoes = [
                    "• Sugestão: Que tal variar com Supino Reto, Leg Press ou Prancha Abdominal?",
                    "• Sugestão: Como você fez força hoje, amanhã foque em um treino de Cardio para descanso muscular.",
                    "• Sugestão: Entre as séries de força, descanse de 60 a 90 segundos."
                ]
            elif "cardio" in tipo_treino or "aeróbico" in tipo_treino or "emagrecimento" in tipo_treino:
                sugestoes = [ 
                    "• Sugestão: Aumente suas atividades do dia a dia -> prefira escadas ao elevador.",
                    "• Sugestão: Comece com 3 dias na semana: 2 dias de Cardio Alternado + 1 dia de Fortalecimento.",
                    "• Sugestão: Mantenha descansos curtos (30 a 45 segundos) para manter batimentos altos."
                ]
            elif "corrida" in tipo_treino:
                sugestoes = [
                    "• Sugestão: Iniciante na corrida? Intercale (corre 1min / anda 2min).",
                    "• Sugestão: Pelo menos um dia focado no fortalecimento da panturrilha!",
                    "• Sugestão: Deixe pelo menos 48h de descanso entre treinos intensos de corrida."
                ]
            else:
                sugestoes = ["• Sugestão: Continue firme nos seus treinos e alimente-se bem!"]

            arquivo.write(f"{sugestoes[0]}\n")
        
        if dados_usuario["imc"] > 0:
            arquivo.write("\n====== ⚖️ DADOS DE IMC ⚖️ ======\n")
            arquivo.write(f"• Altura: {dados_usuario['altura']:.2f}m\n")
            arquivo.write(f"• Peso: {dados_usuario['peso']:.1f}kg\n")
            arquivo.write(f"• IMC: {dados_usuario['imc']:.1f}\n")
            arquivo.write(f"• Status: {dados_usuario['status_imc']}\n")

def adicionar_treino(treinos):
    print("\n--- Novo Treino ---")
    nome = input("Nome do treino: ")
    tipo = input("Tipo (Musculação/Cardio/Funcional/Corrida): ")

    while True:
        data = input("Digite a data (dd/mm/aaaa): ")
        try:
            if len(data) == 10 and data[2] == "/" and data[5] == "/":
                dia = int(data[0:2])
                mes = int(data[3:5])
                ano = int(data[6:10])
                break
            raise ValueError
        except ValueError:
            print(" - Erro: Certifique-se de usar dd/mm/aaaa!")
    
    while True:
        duracao_input = input("Duração (min): ")
        try:
            duracao = int(duracao_input)
            if duracao <= 0:
                raise ValueError
            break 
        except ValueError:
            print(" - Erro: Por favor, digite apenas números inteiros maiores que zero!")
            
    objetivo = input("Objetivo: ")
    exercicio_treino = cadastrar_exercicio()

    meta_treino = []    
    pergunta_meta = input("\nDeseja adicionar uma meta para este treino agora? (sim/não): ").lower().strip()
    if pergunta_meta == 'sim':
        controle_metas(meta_treino)
    
    treino = {
        "nome": nome, "tipo": tipo, "data": data,
        "duracao": duracao, "objetivo": objetivo, 
        "exercicios": exercicio_treino, "metas": meta_treino
    }
    treinos.append(treino)
    print("\n - Treino adicionado com sucesso!")
    salvar_treino(treinos)

def visualizar_treino(treinos):
    print("\n--- Lista de Treinos ---")
    if not treinos:
        print("Nenhum treino cadastrado!")
        return
    for i, t in enumerate(treinos):
        print(f"\n{i+1}º - {t['nome']} | {t['tipo']} | {t['data']} | {t['duracao']}min | {t['objetivo']}")
        if len(t["exercicios"]) > 0:
            print("Exercícios: ")
            for ex in t['exercicios']:
                print(f"  - {ex['Nome']}", end="")
                if "Distância" in ex: print(f" | Distância: {ex['Distância']} km", end="")
                if "Tempo" in ex: print(f" | Tempo: {ex['Tempo']} min", end="")
                if "Séries" in ex: print(f" | Séries: {ex['Séries']}", end="")
                if "Repetições" in ex: print(f" | Repetições: {ex['Repetições']}", end="")
                if "Detalhes" in ex: print(f" | Detalhes: {ex['Detalhes']}", end="")
                print() # quebra de linha

        if "metas" in t and len(t["metas"]) > 0:
            print("Metas vinculadas:")
            for j, met in enumerate(t["metas"], start=1):
                print(f"  - {j}ª Meta: {met['Nome']} | Objetivo: {met['Objetivo']} | Progresso: {met['Progresso']}%")
def editar_treino(treinos):
    visualizar_treino(treinos)
    if not treinos:
        return
    try:
        num_treino = int(input("\nNúmero do treino para editar: ")) - 1
        if 0 <= num_treino < len(treinos):
            print("--- NOVOS DADOS ---\n(use o enter para manter o atual)\n")
            t = treinos[num_treino]
            
            novo_nome = input(f"Novo nome [{t['nome']}]: ") 
            if novo_nome: t['nome'] = novo_nome
            
            novo_tipo = input(f"Novo tipo [{t['tipo']}]: ")
            if novo_tipo: t['tipo'] = novo_tipo
            
            nova_data = input(f"Nova data [{t['data']}]: ")
            if nova_data: t['data'] = nova_data
            
            nova_duracao = input(f"Nova duração [{t['duracao']}]: ")
            if nova_duracao: t['duracao'] = nova_duracao
            
            novo_objetivo = input(f"Novo objetivo [{t['objetivo']}]: ")
            if novo_objetivo: t['objetivo'] = novo_objetivo

            print("\n--- EDITAR EXERCÍCIOS ---")
            for ex in t['exercicios']:
                print(f"\nExercício atual: {ex['Nome']}")
                novo_ex = input(f"Novo exercício [{ex['Nome']}]: ").capitalize()
                if novo_ex: ex['Nome'] = novo_ex
                
                for tipo in ['Séries', 'Repetições', 'Distância', 'Tempo', 'Detalhes']:
                    if tipo in ex:
                        novo_valor = input(f"{tipo} [{ex[tipo]}]: ")
                        if novo_valor:
                            ex[tipo] = int(novo_valor) if tipo != 'Detalhes' else novo_valor

            print("\n--- EDITAR META ---")
            if "metas" in t and len(t["metas"]) > 0:
                for met in t['metas']:
                    print(f"\nMeta atual: {met['Nome']}")

                    nova_meta = input(f"Nova meta [{met['Nome']}]: ")
                    if nova_meta: met['Nome'] = nova_meta
                    
                    novo_obj = input(f"Novo objetivo [{met['Objetivo']}]: ")
                    if novo_obj: met['Objetivo'] = novo_obj
                    
                    while True:
                        novo_prog = input(f"Novo progresso [{met['Progresso']}%]: ")
                        if not novo_prog:
                            break 
                        try:
                            novo_prog = int(novo_prog)
                            if novo_prog < 0 or novo_prog > 100:
                                raise ValueError
                            met['Progresso'] = novo_prog
                            break
                        except ValueError:
                            print("Erro: Digite apenas números inteiros de 0 a 100!")
            else:
                print("Nenhuma meta vinculada a este treino para editar!")

            print("\nTreino e metas atualizados com sucesso!")
            salvar_treino(treinos)
        else:
            print("Treino inválido!")
    except ValueError:
        print("Entrada inválida!")

def excluir_treino(treinos):
    visualizar_treino(treinos)
    if not treinos:
        return
    try:
        while True:
            num_treino = int(input("\nNúmero do treino para excluir: ")) - 1
            try:
                if 0 <= num_treino < len(treinos):
                    treinos.pop(num_treino)
                    print(" - Treino excluído!")
                    salvar_treino(treinos)
                    break
                raise ValueError
            except ValueError:
                print(" - Treino inválido! Insira um número de um treino existente.")
                           
    except ValueError:
        print(" - Entrada inválida!")
