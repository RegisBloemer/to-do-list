import tkinter
import tkinter.messagebox
from new_Window import open_new_window

window = tkinter.Tk()
window.geometry("500x500")
window.resizable(False, False)
window.title("To-Do-List")

# Criar label frame
label_frame = tkinter.LabelFrame(window)
label_frame2 = tkinter.LabelFrame(window)
#Criar canvas
main_canvas = tkinter.Canvas(label_frame)
main_canvas.pack(side=tkinter.LEFT, fill='both', expand="yes")

#Criar scroollbar_lists
scroolbar_lists = tkinter.Scrollbar(label_frame, orient="vertical", command=main_canvas.yview)
scroolbar_lists.pack(side=tkinter.RIGHT, fill="y")
main_canvas.configure(yscrollcommand=scroolbar_lists.set)

main_canvas.bind('<Configure>', lambda e: main_canvas.configure(scrollregion = main_canvas.bbox('all')))

#Criar Frame
main_frame = tkinter.Frame(main_canvas)
main_canvas.create_window((0,0), window= main_frame, anchor="nw")

#Exibir label_frame
label_frame.pack(fill="both", expand="yes", padx=10, pady=10)
label_frame2.pack(fill="both", padx=10, pady=10)


#Adiciona o nome da lista
def add_list_name():
    if entry_list.get() != "":
        tkinter.Button(main_frame, text=f"{entry_list.get()}", width=73, padx=3, command=open_new_window).pack()
    else:
        tkinter.messagebox.showerror(
            title="Aviso!", message="Voce deve digitar o nome da lista!")


#Cria botão de adicionar tarefas
button = tkinter.Button(label_frame2, text="ADD LIST",command=add_list_name, width=98)
button.pack(fill=tkinter.Y, side=tkinter.BOTTOM)

# Input de texto 
entry_list = tkinter.Entry(label_frame2, width=100)
entry_list.pack(fill=tkinter.Y, side=tkinter.BOTTOM)


window.mainloop()