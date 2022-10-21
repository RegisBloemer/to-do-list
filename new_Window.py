import tkinter
def open_new_window():
    new_window = tkinter.Tk()
    new_window.resizable(False, False)
    new_window.title("Tasks")

    def add_task():
        task = entry_task.get()
        if task != "":
            listbox_tasks.insert(tkinter.END, task)
            entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showerror(
                title="Aviso!", message="Voce deve digitar o nome da task!")

#Create de GUI
    listbox_tasks = tkinter.Listbox(new_window, height=3, width= 50)
    listbox_tasks.pack()

    entry_task =tkinter.Entry(new_window, width=50 )
    entry_task.pack()

    button_add_task = tkinter.Button(new_window, text="Add task", width=48, command=add_task)
    button_add_task.pack()

    new_window.mainloop()   