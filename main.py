import tkinter as tk

class botonesMenu():
    def __init__(self, mainHeader,inputX,inputY,comandoBoton):

        self.mainHeader = mainHeader

        self.button11 = tk.Button(self.mainHeader,width="15",height="5",
                                  command=comandoBoton)
        self.button11.pack()

        self.button11.place(x=inputX,y=inputY)

class ventanaEstandar():
    def __init__(self, master):
        #Main header para todas las ventanas
        self.master = master
        self.mainHeader = tk.Frame(self.master,bg="#7bed9f",height="1100",width="135",
                                   highlightbackground="black",highlightthickness=1.5)


        boton012 = botonesMenu(mainHeader=self.mainHeader,inputX=10,inputY=0,comandoBoton="null")
        boton011 = botonesMenu(mainHeader=self.mainHeader, inputX=10, inputY=110, comandoBoton="null")
        boton013 = botonesMenu(mainHeader=self.mainHeader, inputX=10, inputY=200, comandoBoton="null")

        self.mainHeader.pack_propagate(False)
        self.mainHeader.pack(side="left")

def main():
    root = tk.Tk()
    root.geometry("1980x1080")
    root.title("Administracion de centros educativos")
    app = ventanaEstandar(root)

    root.mainloop()

def hola():
    print("Hola")


if __name__ == '__main__':
    main()
