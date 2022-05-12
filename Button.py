from tkinter import *
from tkinter import ttk


# PlayerTurn = "X"
GameHasEnded = False

level = 1  #There can only be 8 levels or you will get an unbeatable level.




class Square:

    def __init__(self, app, col, r, winFunc, changeLevel, usedSquaresArray):
        self.option = "-"
        self.isClicked = False
        self.column = col
        self.row = r
        self.Button = ttk.Button(app, text=self.option, command=self.select)
        self.Button.grid(column=col, row=r)
        self.app = app
        self.id = id
        self.winFunc = winFunc
        self.changeLevel = changeLevel
        self.UsedSquares = usedSquaresArray

    def Reload(self):
        self.Button.config(text=self.option)

    def select(self):
        if (self.isClicked == False):
            self.option = "💎"
            self.Reload()
            self.UsedSquares.append(self)   ######################### HOW DO YOU APPEND YOURSELF TO A LIST??? SCRATCH THAT-- THIS WORKS. 
            #print(UsedSquares)

            if len(self.UsedSquares) == 8:
                global level
                if level < 8:
                    level = level + 1
                    print("from button, level:",level)
                    print("from Button: new level has loaded!")
                    self.changeLevel()
                else:
                    print("YOU WON!!!")
                    self.winFunc()

                
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


