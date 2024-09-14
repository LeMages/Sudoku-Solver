# Sudoku Solver 🧩
Welcome to **Sudoku Solver**, a Python-based project to solve Sudoku puzzles using a backtracking algorithm. Whether you're stuck on a Sudoku puzzle or just want to have fun with coding, this project has got you covered!

# Features 🌟
- **Solve any valid 9x9 Sudoku puzzle** with missing values (represented as 0s).
- Uses a **backtracking algorithm** for efficient and recursive solving.
- **Customizable puzzles**: Just modify the input grid to solve any Sudoku problem.
- Simple, easy-to-read code for anyone interested in learning **algorithm design** and **Python**.

# Installation 💻
Clone the repository:
git clone https://github.com/Kanason/sudoku-solver.git
cd sudoku-solver

Run the solver:
python sudoku_solver.py

# Usage 🚀
You can modify the grid directly in the code or supply it through a different input method. Here's a basic example grid:
grille = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0]
]
The goal is to fill the grid following the Sudoku rules, ensuring that each number from 1 to 9 appears only once in each row, column, and 3x3 sub-grid.

# How It Works 🛠️
The backtracking algorithm recursively tries each possible number in each empty cell (0s) and checks for Sudoku rule violations. If a violation occurs, the algorithm backtracks to the previous step and tries a different number. This process continues until the puzzle is solved or determined unsolvable.

# Example Output 📈
Given the grid above, the solution would look like this:
[
    [4, 2, 3, 6, 7, 8, 9, 5, 1],
    [5, 8, 1, 2, 3, 9, 7, 4, 6],
    [7, 9, 6, 1, 4, 5, 3, 2, 8],
    [3, 7, 2, 4, 1, 6, 5, 8, 9],
    [6, 1, 5, 9, 8, 7, 2, 3, 4],
    [9, 4, 8, 5, 2, 3, 6, 1, 7],
    [8, 5, 4, 7, 2, 1, 9, 6, 3],
    [2, 3, 9, 8, 6, 4, 1, 7, 5],
    [1, 6, 7, 3, 9, 5, 4, 9, 2]
]

# Contributing 🧑‍💻
Feel free to fork the repo, make improvements, or experiment with different algorithms! If you find bugs or have suggestions, please open an issue or submit a pull request.

# About the Author 👨‍💻
I'm **Kanason**, a digital engineering student based in Paris with a passion for **backend development**. I love coding in **Rust**, **Python**, **HTML**, **CSS**, **JavaScript**, **C**, and **Java**. 
