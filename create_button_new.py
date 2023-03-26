import tkinter as tk
import main
def quation():
    took = tk.Tk()
    took.geometry("200x200+500+500")


    tk.Button(took, text="Заново", font="Arial 20", command=main.reset()).grid(row=0, )



    took.grid_rowconfigure(0, minsize=50)
    took.grid_rowconfigure(1, minsize=50)
    took.grid_rowconfigure(2, minsize=50)
    took.grid_rowconfigure(3, minsize=50)
    took.grid_columnconfigure(0,minsize=50)
    took.grid_columnconfigure(1, minsize=50)
    took.grid_columnconfigure(2, minsize=50)
    took.grid_columnconfigure(3, minsize=50)



    took.mainloop()

