"""
Script for generating GUI using streamlit
"""
import numpy as np
import pandas as pd
import streamlit as st

from sudoku import Sudoku

def main():
    """
    Main function.
    Builds GUI using the streamlit package.
    Once a user fills in inputs fields with the GUI,
    other particlepals functions are then called from here.
    Inputs:
        None
    Returns:
        None
    """
    # st.set_page_config(layout="wide")
    puzzle_data = st.sidebar.text_input("Enter Puzzle:")

    puzzle = Sudoku(puzzle_data)
    if puzzle:
        board = st.dataframe(puzzle.clues)

if __name__ == '__main__':
    main()
