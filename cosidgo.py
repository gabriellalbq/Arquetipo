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
