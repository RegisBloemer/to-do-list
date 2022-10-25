#Autor: Régis Nyland Bloemer
#Contado: regisnb1@gmail.com
#
#->control.py
#->Funções que fazem a conecção entre o banco de dados e a interface gráfica
#
#_Criado em Outubro de 2022_________________________________________________________

import data_base

class List:

    #Inicializa os atributos name(string) e tasks(dicionário)  
    def __init__(self, name: str, tasks: dict):
        self.name: str = name
        self.tasks: dict = tasks

    #Função que adiciona a descrição da task com o id da task
    def add_task(self, description: str, id: int):
        self.tasks[id] = description

    #Função que remove a task pelo seu id
    def remove_task(self, id: int):
        del self.tasks[id]

    #Funções que que retorna as tasks e nome da lista
    def get_tasks(self):
        return self.tasks
    
    #Função que retorna o nome da lista
    def get_name(self):
        return self.name

class Control:

    #Inicializa o dicionário de listas 
    def __init__(self):
        self.lists = {}

    #Lê tabelas do banco de dados e converte para Listas de Tasks em Python
    def load_all(self):
        list_table = data_base.get_list_data_base() # [name, list_id]

        for line in list_table:
            task_table = data_base.get_task_from_list_data_base(line["list_id"])
            self.lists[line["list_id"]] = List(line["name"], task_table)

    #Funções de adição de listas e tasks na lista 
    def add_list(self, name: str):
        data_base.add_list_data_base(name)
        new_id = data_base.get_last_list_id()
        self.lists[new_id] = List(name, {})
        return new_id

    def add_task_to_list(self, description: str, list_id: int):
        data_base.add_task_data_base(description, list_id)
        new_task_id = data_base.get_last_task_id()
        self.lists[list_id].add_task(description, new_task_id)
        return new_task_id

    #Funções de remoção da lista e task 
    def remove_list(self, list_id: int):
        data_base.remove_list_data_base(list_id)
        del self.lists[list_id]

    def remove_task_from_list(self, task_id: int, list_id: int):
        data_base.remove_task_data_base(task_id)
        self.lists[list_id].remove_task(task_id)

    #Funções para pegar as listas e task para a GUI
    def get_lists(self):
        list_table = {}
        for id in self.lists:
            list_table[id] = self.lists[id].get_name()
        return list_table # {list_id: name, ...}

    def get_tasks_from_list(self, list_id: int):
        return self.lists[list_id].get_tasks()
