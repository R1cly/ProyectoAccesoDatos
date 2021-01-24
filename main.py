import tkinter as tk
import mysql.connector

"""
class loginUser():
    def __init__(self, master):

        self.master = master
        self.mainLoginFrame = tk.Frame(self.master, bg="silver",width="500",height="700")

        self.mainLoginFrame.pack()
        self.mainLoginFrame.pack_propagate(False)
"""


# Creacion de botones estandar
class botonesMenu():

    def __init__(self, mainHeader, inputX, inputY, comandoBoton, texto):
        self.mainHeader = mainHeader

        self.botonMenu = tk.Button(self.mainHeader, width="15", height="5",
                                   command=comandoBoton, bg="silver", text=texto)
        self.botonMenu.pack(padx="10", pady="10")


class ventanaEstandar():

    def __init__(self, master):
        # Main header para todas las ventanas
        self.master = master

        self.mainWindow = tk.Frame(self.master, bg="#494E55", height="1080", width="1980")
        self.mainHeader = tk.Frame(self.mainWindow, bg="#8CBE8D", height="1100", width="135",
                                   highlightbackground="black", highlightthickness=1.5)

        self.botonN = botonesMenu(mainHeader=self.mainHeader, inputX=10, inputY=200, comandoBoton=self.crearTablas,
                                  texto="ShowDatabases")

        self.mainWindow.pack_propagate(False)
        self.mainWindow.pack()

        self.mainHeader.pack_propagate(False)
        self.mainHeader.pack(side="left")

    def crearTablas(self):

        self.databaseHeader = tk.Frame(self.mainWindow, width="250", height="1080")
        self.databaseHeader.pack_propagate(False)
        self.databaseHeader.pack(side="right")

        myCursor.execute("SHOW DATABASES")

        self.databaseText = tk.Label(self.databaseHeader, text="Database")
        self.databaseText.pack(pady=10, padx=10)
        self.databaseText.pack_propagate(False)

        for x in myCursor:
            print(x)
            self.databaseVariable = x
            boton = botonesMenu(mainHeader=self.databaseHeader, inputX=10, inputY=200, comandoBoton=self.crearDatos,
                                texto=x)

    def crearDatos(self):

        variableQuery = "USE WORLD"
        myCursor.execute(variableQuery)

        myCursor.execute("SELECT name FROM country")

        for x in myCursor:
            boton = botonesMenu(mainHeader=self.mainWindow, inputX=10, inputY=200, comandoBoton=main, texto=x)


def main():
    root = tk.Tk()
    root.geometry("1600x900")
    root.title("Administracion de centros educativos")

    #  = loginUser(root) Not in use

    app = ventanaEstandar(root)

    root.mainloop()


if __name__ == '__main__':
    myDatabase = mysql.connector.connect(host="localhost",
                                         username="root",
                                         password="noseaquien")

    myCursor = myDatabase.cursor()

    main()
