'''##################################################### SKIP TO THE BOTTOM FOR ISSUES #####################################################'''


from tkinter import *
from tkinter import ttk
from Button import Square
from Button import Bomb
from Button import level ################### ONLY IMPORTS ONCE, AND DOESN'T UPDATE VALUE IF IT CHANGES IN OTHER SCRIPT. SPENT AN ANNOYING AMOUNT OF TIME DEBUGGING THIS.
# from Button import UsedSquares
# from Button import GameHasEnded
import random

firstRow = 1
secondRow = firstRow + 1
thirdRow = firstRow + 2

UsedSquares = []
bombs = []
class DontDie:
    def __init__(self):
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=40)
        self.frm.grid()

    
        Title = ttk.Label(self.frm, text="JUST DON'T DIE PLS")
        Title.grid(column=1, row=0)

        def AddToBombArray():
            from Button import level
            for i in range(level):
                while True:
                    bomb = random.randint(0, 8)
                    if bomb not in bombs:
                        bombs.append(bomb)
                        break
            print("Level: ", level)
            print("--------------------------Bombs:", bombs)
            

    

        def WinFunc():
            grid.clear()
            message = ttk.Label(self.frm, text="YOU WON!!!")
            grid.append(mesage)
            ReloadScreen()


        def LoadLevel():
            PrintLevel()
            print("Level should have loaded.")
            

        grid = [
        Square(self.frm, 0, firstRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 1, firstRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 2, firstRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 0, secondRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 1, secondRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 2, secondRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 0, thirdRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 1, thirdRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 2, thirdRow, WinFunc, LoadLevel, UsedSquares)]

        newGrid = [
        Square(self.frm, 0, firstRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 1, firstRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 2, firstRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 0, secondRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 1, secondRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 2, secondRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 0, thirdRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 1, thirdRow, WinFunc, LoadLevel, UsedSquares),
        Square(self.frm, 2, thirdRow, WinFunc, LoadLevel, UsedSquares)]




        def GameOver():
            for item in grid:
                item.isClicked = True




        def PlaceBomb():
            for item in bombs:
                column = grid[item].column
                row = grid[item].row
                grid[item] = Bomb(self.frm, column, row, Title, GameOver)
                print("Bomb placed at square no.", item)
                print("From PlaceBomb, grid:", grid)

        


        def PrintGrid():
            for i in range(0, 9, 1):
                grid[i]
            print("Printgrid, grid:", grid)
            

        def ReloadScreen():
            for item in grid:
                item.Button.config(text="-")

        def ClearBombs():
            # from Button import UsedSquares
            print("Clearbombs running.")
            UsedSquares.clear()
            print("Used squares cleared.")
            bombs.clear()
            print("Clearbombs, bombs:", bombs) #not running on the reload.
            print("Clearbombs, no. of stuff in grids:", len(grid))
            for i in range(0, 9, 1):
                # grid.remove(item)
                del grid[0]
                print("Item removed:", i)
            del grid[:]
            grid.clear()
            print("Grid was cleared, all was removed. Grid length:", len(grid))
            #grid.clear()
            print("Clearbombs, grid", grid)
            grid.extend(newGrid)
            print("Clearbombs, new grid", grid)

        
        def PrintLevel():
            print("==================================================================================")
            ClearBombs()
            AddToBombArray() #clearbombs does not seem to get run but the print function below does??? what's going on?
            print("bombs now:", bombs)
            PlaceBomb()
            ReloadScreen()
            PrintGrid()

        PrintLevel()

        mainloop()
        
        print("It should have worked.")


dont_die = DontDie()





################################################################## ISSUES: ##################################################################
# - Bombs from old levels still remain there, for some reason. Checked PlaceBomb function and Clearbombs function. Nothing, both come back that the grid was cleared but it wasn't.
#   AddToBombArray also said that the list had been redone. PrintGrid said that as well. BUT WHAT IS A BOMB DOING THERE THEN IF EVERYTHING SAYS THAT IT ISN'T???
#
#
#
#











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