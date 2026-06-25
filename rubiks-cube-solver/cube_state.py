import numpy as np

class RubiksCube:
    def __init__(self):
        # Representing 6 faces as 3x3 matrices
        # W=White, Y=Yellow, G=Green, B=Blue, O=Orange, R=Red
        self.faces = {
            'U': np.full((3, 3), 'W'),  # Up
            'D': np.full((3, 3), 'Y'),  # Down
            'F': np.full((3, 3), 'G'),  # Front
            'B': np.full((3, 3), 'B'),  # Back
            'L': np.full((3, 3), 'O'),  # Left
            'R': np.full((3, 3), 'R')   # Right
        }

    def get_state_tuple(self):
        """Converts the current state into a hashable tuple for search algorithms."""
        return tuple(tuple(face.flatten()) for face in self.faces.values())

    def is_solved(self):
        """Returns True if every face contains only one uniform color."""
        for face in self.faces.values():
            if len(np.unique(face)) > 1:
                return False
        return True

    def rotate_face_clockwise(self, face):
        """Rotates a single 3x3 face matrix 90 degrees clockwise."""
        self.faces[face] = np.rot90(self.faces[face], -1)

    def move_U(self):
        """Applies a clockwise turn to the Up face."""
        self.rotate_face_clockwise('U')
        # Temporarily store adjacent row to cycle them clockwise
        temp = self.faces['F'][0, :].copy()
        self.faces['F'][0, :] = self.faces['R'][0, :]
        self.faces['R'][0, :] = self.faces['B'][0, :]
        self.faces['B'][0, :] = self.faces['L'][0, :]
        self.faces['L'][0, :] = temp

    def move_R(self):
        """Applies a clockwise turn to the Right face."""
        self.rotate_face_clockwise('R')
        temp = self.faces['U'][:, 2].copy()
        self.faces['U'][:, 2] = self.faces['F'][:, 2]
        self.faces['F'][:, 2] = self.faces['D'][:, 2]
        self.faces['D'][:, 2] = np.flip(self.faces['B'][:, 0])
        self.faces['B'][:, 0] = np.flip(temp)

    def move_F(self):
        """Applies a clockwise turn to the Front face."""
        self.rotate_face_clockwise('F')
        temp = self.faces['U'][2, :].copy()
        self.faces['U'][2, :] = np.flip(self.faces['L'][:, 2])
        self.faces['L'][:, 2] = self.faces['D'][0, :]
        self.faces['D'][0, :] = np.flip(self.faces['R'][:, 0])
        self.faces['R'][:, 0] = temp

    def apply_move(self, move):
        """Mapping system execution string to functional face moves."""
        if move == 'U': self.move_U()
        elif move == 'R': self.move_R()
        elif move == 'F': self.move_F()