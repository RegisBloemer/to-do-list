from asyncore import loop
import tkinter

def open_new_window(ctrl, list_id):
    new_window = tkinter.Tk()
    new_window.resizable(False, False)
    new_window.title("Tasks")

    task_ids = []

    def load_tasks_in_gui():
        tasks = ctrl.get_tasks_from_list(list_id)
        for id in tasks:
            listbox_tasks.insert(tkinter.END, tasks[id])
            task_ids.append(id)
            print("loop")
        print("2")

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

    load_tasks_in_gui()
    new_window.mainloop()   