#-Autor: Régis Nyland Bloemer
#-Contado: regisnb1@gmail.com
#
#->new_Window.py
#->Funções que adicionam e removem tasks da interface gráfica
#->Tela gráfica para adicionar task
#
#_Criado em Outubro de 2022________________________________________


import tkinter

def open_new_window(ctrl, list_id):
    new_window = tkinter.Tk()
    new_window.resizable(False, False)
    new_window.title("List Tasks")

    task_ids = []
    
#Função que carrega todas as tasks na GUI quando o programa inicia
    def load_tasks_in_gui():
        tasks = ctrl.get_tasks_from_list(list_id)
        for id in tasks:
            listbox_tasks.insert(tkinter.END, tasks[id])
            task_ids.append(id)

#Funções para adicionar, deletar, carregar e salvar 
    def add_task():
        name = entry_task.get()
        if name != "":
            listbox_tasks.insert(tkinter.END, name)
            entry_task.delete(0, tkinter.END)
            new_id = ctrl.add_task_to_list(name, list_id)
            task_ids.append(new_id)
        else:
            tkinter.messagebox.showwarning(
                title="Aviso!", message="Voce deve digitar o nome da task!")

    def delete_task():
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
            ctrl.remove_task_from_list(task_ids[task_index], list_id)
            del task_ids[task_index]
        except:
            tkinter.messagebox.showwarning(
                title="Aviso!", message="Voce deve selecionar a task!")

#Create de GUI
    frame_tasks = tkinter.Frame(new_window)
    frame_tasks.pack()

    listbox_tasks = tkinter.Listbox(frame_tasks,
                                    height=20, 
                                    width= 50, 
                                    selectbackground="#FFFFFF", 
                                    bg="#F2F5FF")        
    listbox_tasks.pack(side = tkinter.LEFT)

    scrollbar_tasks = tkinter.Scrollbar(frame_tasks, relief="flat", background="#2C1A55")
    scrollbar_tasks.pack(side=tkinter.RIGHT, fill = tkinter.Y)

    listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    entry_task =tkinter.Entry(new_window, bg="#F2F5FF")
    entry_task.pack(ipadx = 95, ipady=10, padx=3)

#Botões de adicionar, deletar, carregar e salvar 
    button_add_task = tkinter.Button(new_window, 
                                    text="Add task", 
                                    width=48, 
                                    command=add_task, 
                                    relief="flat",
                                    fg="#2C1A55", 
                                    bg="#FF700A", 
                                    pady = 10)
    button_add_task.pack()

    button_delete_task = tkinter.Button(new_window, 
                                        text="Excluir task", 
                                        width=48, 
                                        command=delete_task, 
                                        relief="flat",
                                        fg="#2C1A55", 
                                        bg="#FF700A", 
                                        pady = 10)
    button_delete_task.pack()

    load_tasks_in_gui()
    new_window.mainloop()   
    