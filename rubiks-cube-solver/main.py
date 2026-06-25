from cube_state import RubiksCube
from utils import scramble_cube, print_cube_layout
from solver import solve_cube

def main():
    print("Initializing a clean, solved Rubik's Cube...")
    cube = RubiksCube()
    print_cube_layout(cube)

    # Scramble length is kept short for demonstration since BFS grows exponentially
    scramble_depth = 3
    print(f"Scrambling the cube randomly with {scramble_depth} moves...")
    moves_applied = scramble_cube(cube, num_moves=scramble_depth)
    print(f"Applied Scramble Sequence: {moves_applied}")
    print_cube_layout(cube)

    print("Invoking the BFS Graph Search Solver Architecture...")
    solution_path = solve_cube(cube)

    if solution_path is not None:
        print(f"Success! Solution discovered in {len(solution_path)} steps.")
        print(f"Required Execution Moves: {solution_path}")
    else:
        print("Solver was unable to find a clear path to resolution.")

if __name__ == "__main__":
    main()