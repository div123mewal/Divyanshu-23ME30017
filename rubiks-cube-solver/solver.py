from collections import deque
import copy

def solve_cube(initial_cube):
    """Uses Breadth-First Search to find the shortest path to solve the cube."""
    if initial_cube.is_solved():
        return []

    # Queue stores tuples of (cube_object, path_taken)
    queue = deque([(initial_cube, [])])
    
    # Visited set keeps track of explored matrix state signatures
    visited = {initial_cube.get_state_tuple()}
    
    allowed_moves = ['U', 'R', 'F']

    while queue:
        current_cube, path = queue.popleft()

        for move in allowed_moves:
            # Create a deep copy to simulate the move safely
            next_cube = copy.deepcopy(current_cube)
            next_cube.apply_move(move)
            state_signature = next_cube.get_state_tuple()

            if next_cube.is_solved():
                return path + [move]

            if state_signature not in visited:
                visited.add(state_signature)
                queue.append((next_cube, path + [move]))
                
    return None  # Return None if no solution is found within limits