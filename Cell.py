import numpy as np

class Cell:
    '''
    Useful fields:
    - Row (label)
    - Col (label)
    - Box (label)
    - Value (0 if unkown)
    - Position (row label, col label, box number)
    - Candidates (available after get_candidates())
    '''
    def __init__(self, position, value):
        self.value = value
        self.position = position
        self.row = position[1]
        self.col = position[0]
        self.box = position[2]