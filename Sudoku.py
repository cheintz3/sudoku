import string
import math

import numpy as np

import Row
import Col
import Box
import Cell


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
        # for now assume input is 2D matrix of valid size 
        # puzzle should be square
        # generatepuzzle()

        self.clues = clues
        self.generate_cells()
        self.__validate_input()
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
        self.puzzle = self.clues
        self.n = self.puzzle.shape[0]
        
    def generate_cells(self):
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
        # int [1,n]
        row_idx = position[1]
        # int [0,n-1]
        col_idx = ord(position[0])-65
        n = self.n
        box = row_idx + int(math.sqrt(self.n))*col_idx
        return box