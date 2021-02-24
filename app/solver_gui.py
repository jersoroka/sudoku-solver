'''GUI for solver'''

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
import solver


class App:
    '''
    A class used to represent the GUI sudoku board

    ...

    Attributes
    ----------
    grid_frame: Frame
        a frame holding the sudoku grid
    button_frame: Frame
        a frame holding the solve and clear buttons
    entryText : List[StringVar]
        a list containing all of the text variables for each entry field in
        the sudoku grid
    cells : List[List[Entry]]
        a list of all the entry fields in the sudoku grid


    Methods
    -------
    make_board()
        Produces a 9x9 sudoku board
    make_entry(x, y)
        Makes an Entry and places it at x and y
    make_buttons()
        Creates the solve and clear buttons on the board
    solve_board()
        If the inputs to the board are valid, solves the board
    clear_board()
        Removes all the inputs on the board
    popup(message)
        Produces a popup stating that the board has at least one invalid entry
    '''

    def __init__(self, parent: Entry):
        '''
        Parameters
        ----------
        parent : Tk
        '''
        self.grid_frame = Frame(parent, bd=5, relief=RIDGE)
        self.button_frame = Frame(parent)
        self.grid_frame.pack(side=LEFT)
        self.button_frame.pack(side=RIGHT)
        self.entryText = [[StringVar() for y in range(9)] for x in range(9)]
        self.cells = self.make_board()
        self.make_buttons()

    def make_board(self):
        '''Produces a 9x9 sudoku board GUI

        Returns:
            a list of all the entry fields in the sudoku grid
        '''
        entry_fields = []
        for x in range(9):
            entry_row = []
            for y in range(9):
                entry_row.append(self.make_entry(x, y))
            entry_fields.append(entry_row)
        return entry_fields

    def make_entry(self, x: int, y: int):
        '''Makes an Entry and places it at row x and position y

        Args:
            x : row index
            y : position index
        Returns:
            an Entry placed at row x and position y
        '''
        entryBox = ttk.Entry(self.grid_frame, width=2, font="Helvetica 30",
                             textvariable=self.entryText[x][y])
        entryBox.grid(row=x, column=y)
        return entryBox

    def make_buttons(self):
        '''Makes the solve and clear buttons
        '''

        self.solve_button = ttk.Button(self.button_frame, text="Solve",
                                       command=self.solve_board)
        self.solve_button.grid(row=0)
        self.clear_button = ttk.Button(self.button_frame,
                                       text="Clear",
                                       command=self.clear_board)
        self.clear_button.grid(row=1)

    def solve_board(self):
        '''Solves the board
        '''
        valid_entries = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        values = []
        for row in self.cells:
            row_values = []
            for cell in row:
                if cell.get() not in valid_entries:
                    self.popup("Invalid entries! Please only use integers from 1-9")
                    break
                elif cell.get() == "":
                    row_values.append(0)
                else:
                    row_values.append(int(cell.get()))
            values.append(row_values)

        if len(values) > 0:
            solution = solver.solver(values)

        if isinstance(solution, bool):
            self.popup("This board is not solvable.")
        else:
            for row in range(len(self.cells)):
                for cell in range(len(self.cells[row])):
                    self.entryText[row-1][cell-1].set(solution[row-1][cell-1])

    def clear_board(self):
        '''Clears the inputs on the board
        '''
        for row in self.cells:
            for cell in row:
                cell.delete(0, 'end')

    def popup(self, message: str):
        '''Produces a pop-up displaying given message
        '''
        popup = Tk()

        def close_popup():
            popup.destroy()

        popup.wm_title("Error")
        label = ttk.Label(popup, text=message)
        label.pack()
        confirm_button = ttk.Button(popup, text="okay", command=close_popup)
        confirm_button.pack()
        popup.mainloop()


def main():
    root = Tk()
    root.title("Sudoku Solver")
    root.geometry("600x500")

    style = ThemedStyle(root)
    style.set_theme("arc")

    board = App(root)

    root.mainloop()


if __name__ == "__main__":
    main()
