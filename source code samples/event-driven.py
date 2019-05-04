import sys
import tkinter

def main():
    root = tkinter.Tk()
    root.title("Remeinder!")
    root.resizable(width=False, height=False)
    tkinter.mainloop()

    mainFrame = tkinter.Frame(root,borderwidth=1, padx=5, pady=5)
    mainFrame.pack()
    
    note = tkinter.Text(mainFrame, bg="yellow", width=30, height=15)
    note.pack()    

if __name__ == "__main__":
    main()