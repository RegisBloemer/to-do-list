import tkinter
import pickle

def open_new_window():
    new_window = tkinter.Tk()
    new_window.resizable(False, False)
    new_window.title("Tasks")

#Funções para adicionar, deletar, carregar e salvar 
    def add_task():
        task = entry_task.get()
        if task != "":
            listbox_tasks.insert(tkinter.END, task)
            entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(
                title="Aviso!", message="Voce deve digitar o nome da task!")

    def delete_task():
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning(
                title="Aviso!", message="Voce deve selecionar a task!")

    def load_tasks():
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            listbox_tasks.delete(0, tkinter.END)
            for task in tasks:
                listbox_tasks.insert(tkinter.END, task)
        except:
            tkinter.messagebox.showwarning(
                title="Falha na leitura!", message="Não foi possível ler o arquivo")

    def save_tasks():
        tasks = listbox_tasks.get(0, listbox_tasks.size())
        pickle.dump(tasks, open("tasks.dat", "wb"))

#Create de GUI
    frame_tasks = tkinter.Frame(new_window)
    frame_tasks.pack()

    listbox_tasks = tkinter.Listbox(frame_tasks, height=20, width= 50)
    listbox_tasks.pack(side = tkinter.LEFT)

    scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
    scrollbar_tasks.pack(side=tkinter.RIGHT, fill = tkinter.Y)

    listbox_tasks.config(yscrollcommand = scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    entry_task =tkinter.Entry(new_window, width=50 )
    entry_task.pack()

#Botões de adicionar, deletar, carregar e salvar 
    button_add_task = tkinter.Button(new_window, text="Add task", width=48, command=add_task)
    button_add_task.pack()

    button_delete_task = tkinter.Button(new_window, text="Excluir task", width=48, command=delete_task)
    button_delete_task.pack()

    button_load_tasks = tkinter.Button(new_window, text="Carregar tasks", width=48, command=load_tasks)
    button_load_tasks.pack()

    button_save_tasks = tkinter.Button(new_window, text="Save tasks", width=48, command=save_tasks)
    button_save_tasks.pack()

    new_window.mainloop()   