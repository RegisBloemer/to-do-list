import tkinter
import tkinter.messagebox
from new_Window import open_new_window
import control

ctrl = control.Control()
ctrl.load_all()
list_ids = []

window = tkinter.Tk()
window.resizable(False, False)
window.title("To-Do-List")


def load_lists_in_gui():
    lists = ctrl.get_lists()
    for id in lists:
        listbox_lists.insert(tkinter.END, lists[id])
        list_ids.append(id)

#Funções para adicionar, deletar, carregar e salvar 
def add_list():
    name = entry_list.get()
    if name != "":
        listbox_lists.insert(tkinter.END, name)
        entry_list.delete(0, tkinter.END)
        new_id = ctrl.add_list(name)
        list_ids.append(new_id)
    else:
        tkinter.messagebox.showwarning(
            title="Aviso!", message="Voce deve digitar o nome da list!")

def delete_list():
    try:
        list_index = listbox_lists.curselection()[0]
        listbox_lists.delete(list_index)
        ctrl.remove_list(list_ids[list_index])
        del list_ids[list_index]
    except:
        tkinter.messagebox.showwarning(
            title="Aviso!", message="Voce deve selecionar a list!")

def open_list():
    try:
        selection_list = listbox_lists.curselection()[0]
        open_new_window(ctrl, list_ids[selection_list])
    except:
        tkinter.messagebox.showwarning(
            title="Falha na leitura!", message="Voce deve selecionar uma lista para abrir")

#Create de GUI
frame_lists = tkinter.Frame(window)
frame_lists.pack()

listbox_lists = tkinter.Listbox(frame_lists, height=20, width= 50)
listbox_lists.pack(side = tkinter.LEFT)

scrollbar_lists = tkinter.Scrollbar(frame_lists)
scrollbar_lists.pack(side=tkinter.RIGHT, fill = tkinter.Y)

listbox_lists.config(yscrollcommand = scrollbar_lists.set)
scrollbar_lists.config(command=listbox_lists.yview)

entry_list =tkinter.Entry(window, width=50 )
entry_list.pack()

#Botões de adicionar, deletar, carregar e salvar 
button_add_list = tkinter.Button(window, text="Add lista", width=48, command=add_list)
button_add_list.pack()

button_delete_list = tkinter.Button(window, text="Excluir lista", width=48, command=delete_list)
button_delete_list.pack()

button_open_lists = tkinter.Button(window, text="Abrir lista", width=48, command=open_list)
button_open_lists.pack()

load_lists_in_gui()
window.mainloop()   