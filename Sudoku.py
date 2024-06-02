class Sudoku:
    '''
    Useful fields:
    - Rows (.rows plus .row1, .row2, etc) 
    - Cols (.cols plus .cola, .colb, etc)
    - Boxes (.boxes plus .box1, .box2, etc)
    - Shape/n - puzzle size (assume square or allow for different puzzle sizes)
    '''
    def __init__(self, sudoku_data):
        # for now assume input is 2D matrix of valid size 
        # puzzle should be square
        # generatepuzzle()

        validate_input()
        self.n = sudoku_data.shape[0]
        generate_cells()
        generate_rows()
        generate_cols()
        generate_boxes()

        # displaypuzzle()

    def validate_input(self):
        # checks if input comprises a valid puzzle
        # does NOT check for solvability or uniqueness of solution
        #    should it?

        # input is 2D numpy array, 2D array, or string/float of single-digit integers? 
        # input square?
        # cell entries are single digit integers?
        # input doesn't contain extra/invalid characters or delimiters?
        pass

    def generate_cells(self):
        for r in range(self.shape[0]):
            for c in range(self.shape[1]):
