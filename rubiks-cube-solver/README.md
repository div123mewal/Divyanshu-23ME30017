# 3x3 Rubik's Cube Simulation & Graph-Search Solver

A modular object-oriented Python implementation modeling the physical mechanics, matrix states, and algorithmic solutions of a 3x3 Rubik's Cube. 

## 🛠️ System Architecture & Components
* **`cube_state.py`**: State representation layer tracking face matrices and adjacent piece mapping via NumPy vector slices.
* **`solver.py`**: Algorithmic engine utilizing a state-space Breadth-First Search (BFS) to identify shortest path solutions.
* **`utils.py`**: Functional components handling structural terminal visualizations and stochastic scramble generation.
* **`main.py`**: Pipeline orchestration layer linking environment logic with the search backend.

## 🚀 Execution Instructions
Ensure you have the required dependencies installed:
```bash
pip install -r requirements.txt