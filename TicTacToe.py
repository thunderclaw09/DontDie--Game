from tkinter import *
from tkinter import ttk
from Button import Square
from Button import Bomb
# from Button import GameHasEnded
import random

firstRow = 1
secondRow = firstRow + 1
thirdRow = firstRow + 2

class DontDie:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=40)
        self.frm.grid()

        level = 1  #There can only be 8 levels or you will get an unbeatable level.

        bombs = []

        Title = ttk.Label(self.frm, text="JUST DON'T DIE PLS")
        Title.grid(column=1, row=0)

        for i in range(level):
            while True:
                bomb = random.randint(0, 8)
                if bomb not in bombs:
                    bombs.append(bomb)
                    break

        print("Bombs:", bombs)


        grid = [
        Square(self.frm, 0, firstRow),
        Square(self.frm, 1, firstRow),
        Square(self.frm, 2, firstRow),
        Square(self.frm, 0, secondRow),
        Square(self.frm, 1, secondRow),
        Square(self.frm, 2, secondRow),
        Square(self.frm, 0, thirdRow),
        Square(self.frm, 1, thirdRow),
        Square(self.frm, 2, thirdRow),]



        def GameOver():
            for item in grid:
                item.isClicked = True




        for item in bombs:
            column = grid[item].column
            row = grid[item].row
            grid[item] = Bomb(self.frm, column, row, Title, GameOver)
            print("Bomb placed at square no.", item)


        for i in range(0, 9, 1):
            grid[i]


        mainloop()
        
        print("It should have worked.")


    
    

    

  

dont_die = DontDie()




############################################################### OLD CODE ###############################################################



''' Old version:
            # for item in bombs:
                #     if (item != bomb):
                #         bombs.append(bomb)
                #         break
                #     else:
                #         bomb = random.randint(0, 8)'''
        # instructions = ttk.Label(self.frm, text="Click 3 times and don't click the bomb.")
        # instructions.grid(column=1, row=1)