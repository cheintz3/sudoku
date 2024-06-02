import numpy as np

import sudoku

class Unit:
    def __init__(self, label, cells):
        self.label = label
        self.cells = cells

class Row(Unit):
    '''
    Useful fields:
    - Label
    - Cells (add another field with just ordered array of values?)
    '''
    

class Col(Unit):
    '''
    Useful fields:
    - Label
    - Cells (add another field with just ordered array of values?)
    '''

class Box(Unit):
    '''
    Useful fields:
    - Label
    - Cells (add another field with just ordered array of values?)
    '''