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
                cells[cell_label] = self.clues[r,c]
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
            rows[r+1] = Row(cells)
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
            cols[r+1] = Row(cells)
        self.cols = cols
    
    def generate_boxes(self):
        boxes = {}
        for b in range(self.n):
            first_row_idx = b // int(math.sqrt(self.n))
            last_row_idx = first_row_idx + int(math.sqrt(self.n)) - 1
            first_col_idx = b % int(math.sqrt(self.n))
            last_col_idx = first_col_idx + int(math.sqrt(self.n)) - 1
            this_box = self.puzzle[first_row_idx:last_row_idx+1,
                                    first_col_idx:last_col_idx+1]
            boxes[b+1] = Box(this_box)
        self.boxes = boxes