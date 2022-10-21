import tkinter
def open_new_window():
    new_window = tkinter.Tk()
    new_window.geometry("500x500")
    new_window.resizable(False, False)
    new_window.title("To-Do-List")

    new_window.mainloop()