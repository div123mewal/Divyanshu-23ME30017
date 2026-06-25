import random
import copy

def scramble_cube(cube, num_moves=3):
    """Scrambles the cube using random moves and returns the sequence sequence."""
    possible_moves = ['U', 'R', 'F']
    scramble_sequence = [random.choice(possible_moves) for _ in range(num_moves)]
    
    for move in scramble_sequence:
        cube.apply_move(move)
        
    return scramble_sequence

def print_cube_layout(cube):
    """Prints a clear, descriptive textual layout of the active cube faces."""
    print("\n--- Current Cube Layout ---")
    for face_name, grid in cube.faces.items():
        print(f"Face {face_name}:")
        for row in grid:
            print("  " + " ".join(row))
    print("---------------------------\n")