import tkinter as tk
import mysql.connector


class botonesMenu():
    def __init__(self, mainHeader, inputX, inputY, comandoBoton,texto):
        self.mainHeader = mainHeader

        self.button11 = tk.Button(self.mainHeader, width="15", height="5",
                                  command=comandoBoton,bg="blue",text=texto)
        self.button11.pack(padx="10", pady="10")


class ventanaEstandar():

    def __init__(self, master):
        # Main header para todas las ventanas
        self.master = master

        self.mainWindow = tk.Frame(self.master, bg="#494E55", height="1080", width="1980")
        self.mainHeader = tk.Frame(self.mainWindow, bg="#8CBE8D", height="1100", width="135",
                                   highlightbackground="black", highlightthickness=1.5)

        self.databaseHeader = tk.Frame(self.mainWindow, width="250",height="1080")

        self.databaseHeader.pack_propagate(False)
        self.databaseHeader.pack(side="right")

        self.botonN = botonesMenu(mainHeader=self.mainHeader, inputX=10, inputY=200, comandoBoton=self.crearTablas,texto="ShowDatabases")

        self.mainWindow.pack_propagate(False)
        self.mainWindow.pack()

        self.mainHeader.pack_propagate(False)
        self.mainHeader.pack(side="left")

    def crearTablas(self):

        myCursor.execute("SHOW DATABASES")

        self.databaseText = tk.Label(self.databaseHeader,text="Database")
        self.databaseText.pack(pady=10,padx=10)
        self.databaseText.pack_propagate(False)

        for x in myCursor:
            print(x)
            self.databaseVariable = x
            boton = botonesMenu(mainHeader=self.databaseHeader, inputX=10, inputY=200, comandoBoton=self.crearDatos,texto=x)

    def crearDatos(self):

        self.variableQuery = "USE WORLD"
        myCursor.execute(self.variableQuery)

        myCursor.execute("SELECT * FROM country")

        for x in myCursor:
            self.boton = botonesMenu(mainHeader=self.mainWindow, inputX=10, inputY=200, comandoBoton=main, texto="Hola")

def helloFriend():
    print("Hello")


def main():
    root = tk.Tk()
    root.geometry("1600x900")
    root.title("Administracion de centros educativos")


    app = ventanaEstandar(root)
    #ventanaEstandar.crearTablas(app)

    root.mainloop()


if __name__ == '__main__':
    myDatabase = mysql.connector.connect(host="localhost",
                                         username="root",
                                         password="noseaquien")

    myCursor = myDatabase.cursor()

    main()
