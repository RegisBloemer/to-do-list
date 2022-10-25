#-Autor: Régis Nyland Bloemer
#-Contado: regisnb1@gmail.com
#
#->data_base.py
#->Criação do modelo físico gerado pelo Modelo Lógico usando freeware brModelo (2.0.0)
#->Funções que adicionam e removem diretamente do banco de dados 
#->Funções de busca de listas e tasks diretamente no banco de dados
#
#_Criado em Outubro de 2022_____________________________________________

import sqlite3

#Conexão com o banco de dados
data_base = sqlite3.connect('data_base')
cursor = data_base.cursor()

# ps é a função para preparação de strings para a query impedindo SQL injection (Prepared Statement)
def ps(_str: str):
    # return _str
    var_str = _str.replace("\\", "\\\\")
    var2_str = var_str.replace("\'", "\'\'")
    return var2_str

#Funções de adição
# Função que adiciona a lista pelo nome na tabela lista ao banco de dados
def add_list_data_base(_name):
    cursor.execute(
        f"INSERT INTO List (name) VALUES ('{ps(_name)}');")
    data_base.commit()

#Função que adiciona a task na tabela Task no banco de dados
def add_task_data_base(description, list_id: int):
    cursor.execute(
        f"INSERT INTO Task (description, list_id) VALUES ('{ps(description)}', {list_id});")
    data_base.commit()

#Funções de remoção
#Função que deleta a task pelo seu task_id da tabela task no banco de dados
def remove_task_data_base(task_id: int):
    cursor.execute(f"DELETE FROM Task WHERE task_id = {task_id};")
    data_base.commit()

#Função que remove todas as task da tabela Task para que se possa excluir a Lista
def remove_all_task_from_list_data_base(list_id: int):
    cursor.execute(f"DELETE FROM Task WHERE list_id = {list_id}")
    data_base.commit()

#Função que remove a lista pelo seu list_id na tabela List
def remove_list_data_base(list_id: int):
    remove_all_task_from_list_data_base(list_id)
    cursor.execute(f"DELETE FROM List WHERE list_id = {list_id};")
    data_base.commit()

#Funções para pegar as listas diretamente do banco de dados
def get_list_data_base():
    data_lists = cursor.execute(f"SELECT name, list_id FROM List")
    table = data_lists.fetchall() # table = [ (name, list_id), ... ]
    dict_table = []
    for line in table: # line = (name, list_id)
        dict_table.append({"name": line[0], "list_id": line[1]}) # [{"name":name, "list_id":list_id}, ...]
    return dict_table #table foi trasformado em dicionário para facilitar o entendimento

#Funções que buscam no banco de dados
#Função que pega task das suas respectiva lista 
def get_task_from_list_data_base(list_id: int):
    data_tasks = cursor.execute(
        f"SELECT description, task_id FROM Task WHERE list_id = {list_id}")    # Traduzindo tabela para um dicionário
    table = data_tasks.fetchall() # table = [ (description, task_id), ... ]
    task_table = {}
    for line in table: # line = (description, task_id)
        task_table[line[1]] = line[0] # {task_id: description, ...}
    return task_table

#Função para buscar o maior id na tabela Task
def get_last_task_id():
    data_tasks = cursor.execute(f"SELECT MAX(task_id) FROM Task")
    res = data_tasks.fetchall() # Sempre vai retornar isso, uma lista de tuplas : [(id)]
    if len(res) == 0:
        return 0
    return res[0][0] # Tupla 0 item 0
 
#Função para buscar o maior id na tabela List
def get_last_list_id():
    data_tasks = cursor.execute(f"SELECT MAX(list_id) FROM List")
    res = data_tasks.fetchall()  #Sempre vai retornar isso, uma lista de tuplas : [(id)]
    if len(res) == 0:
        return 0
    return res[0][0] # Tupla 0 item 0
