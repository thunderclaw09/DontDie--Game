from tkinter import *
from tkinter import ttk


# PlayerTurn = "X"
GameHasEnded = False

UsedSquares = []


class Square:

    def __init__(self, app, col, r):
        self.option = "-"
        self.isClicked = False
        self.column = col
        self.row = r
        self.Button = ttk.Button(app, text=self.option, command=self.select)
        self.Button.grid(column=col, row=r)
        self.app = app
        self.id = id

    def Reload(self):
        self.Button.config(text=self.option)

    def select(self):
        if (self.isClicked == False):
            self.option = "💎"
            self.Reload()
            UsedSquares.append(self)
            print(UsedSquares)
                
        else:
            print("You can no longer select this square.")




class Bomb:

    def __init__(self, app, col, r, titleText, gameOverFunc):
        self.isClicked = False
        self.option = "-"
        self.column = col
        self.row = r
        self.Button = ttk.Button(app, text=self.option, command=self.select)
        self.Button.grid(column=col, row=r)
        self.app = app
        self.id = id
        self.titleText = titleText
        self.gameOverFunc = gameOverFunc

    def Reload(self):
        self.Button.config(text=self.option)
        self.titleText.config(text="YOU HAVE LOST.")


    def select(self):
        global GameHasEnded
        if (self.isClicked == False):
            self.option = "💀"
            self.Reload()
            GameHasEnded = True
            self.gameOverFunc()
                
                
        else:
            print("You can no longer select this square.")


