'''
contains Sudoku class definition. Instances of this class are
representations of Sudoku puzzles. An instance is generated
from an input string containing a perfect square number of single
digit integers
'''
import string
import math

import numpy as np

from cell import Cell
from units import Row, Col, Box


class Sudoku:
    '''
    Useful fields:
    - Rows (.rows plus .row1, .row2, etc) 
    - Cols (.cols plus .cola, .colb, etc)
    - Boxes (.boxes plus .box1, .box2, etc)
    - Cells (dictionary or list? Key is already field of Cell class)
    - Shape/n - puzzle size (assume square or allow for different puzzle sizes)
    '''
    def __init__(self, clues):
        # for now assume input is string of single digit integers of valid size
        # puzzle should be square

        self.__validate_input()
        self.clues = self.get_clue_array(clues)
        self.n = self.clues.shape[0]
        self.generate_cells()
        self.generate_rows()
        self.generate_cols()
        self.generate_boxes()

        # displaypuzzle()

    def __validate_input(self):
        # checks if input comprises a valid puzzle
        # does NOT check for solvability or uniqueness of solution
        #    should it?

        # input is 2D numpy array, 2D array, or string/float of single-digit integers?
        # input square?
        # cell entries are single digit integers?
        # input doesn't contain extra/invalid characters or delimiters?
        # self.puzzle = self.clues
        # self.n = self.puzzle.shape[0]
        pass

    def get_clue_array(self, clues):
        """
        converts clue string to array representing puzzle
        inputs:
            clues - string of single digit integers. Length should be perfect square.
        """
        n = int(math.sqrt(len(clues)))
        clue_arr = np.zeros((n,n))

        for r in range(n):
            this_row_slice = slice(r*n, (r+1)*n)
            clue_arr[r, :n] = np.array(list(clues[this_row_slice]))
        return clue_arr

    def generate_cells(self):
        ''' 
        generates cells field of Sudoku object
        cells is a dictionary of Cell objects with positions as keys
        '''
        cells = {}
        for r in range(self.n):
            row_label = r+1
            for c in range(self.n):
                col_label = string.ascii_uppercase[c]
                cell_label = col_label + str(row_label)
                position = (cell_label[1], cell_label[0], self.get_box(cell_label))
                cells[cell_label] = Cell(position, self.clues[r,c])
        self.cells = cells

    def generate_rows(self):
        '''
        generates rows field of Sudoku object
        rows is a dictionary of Row objects with labels as keys
        '''
        rows = {}
        for r in range(self.n):
            cells = []
            row_label = r+1
            for c in range(self.n):
                col_label = string.ascii_uppercase[c]
                cell_label = col_label + str(row_label)
                cells.append(self.cells[cell_label])
            rows[r+1] = Row(row_label, cells)
        self.rows = rows

    def generate_cols(self):
        '''
        generates cols field of Sudoku object
        cols is a dictionary of Col objects with labels as keys
        '''
        cols = {}
        for c in range(self.n):
            cells = []
            col_label = string.ascii_uppercase[c]
            for r in range(self.n):
                row_label = r+1
                cell_label = col_label + str(row_label)
                cells.append(self.cells[cell_label])

            cols[r+1] = Col(col_label, cells)
        self.cols = cols

    def generate_boxes(self):
        '''
        generates boxes field of Sudoku object
        boxes is a dictionary of Box objects with box numbers as keys
        '''
        boxes = {}
        for b in range(self.n):
            cells = {}
            first_row_idx = b // int(math.sqrt(self.n))
            last_row_idx = first_row_idx + int(math.sqrt(self.n)) - 1
            row_labels = np.arange(first_row_idx, last_row_idx + 1) + 1

            first_col_idx = b % int(math.sqrt(self.n))
            last_col_idx = first_col_idx + int(math.sqrt(self.n)) - 1
            col_labels = string.ascii_uppercase[first_col_idx:last_col_idx+1]

            for r in row_labels:
                for c in col_labels:
                    cell_label = c+str(r)
                    cells[cell_label] = self.cells[cell_label]

            box_num = b+1
            boxes[box_num] = Box(box_num, cells)
        self.boxes = boxes

    def get_box(self, position):
        '''
        returns number of box containing cell in provided position
        '''
        # int [1,n]
        row_idx = int(position[1])
        # int [0,n-1]
        col_idx = int(ord(position[0])-65)
        n = self.n
        box = row_idx + int(math.sqrt(n))*col_idx

        return box
