import numpy as np
from functools import lru_cache

def zero_player_wins_as_first(n: int) -> bool:
    @lru_cache(None)
    def solve(state, turn):
        if -1 not in state:
            A = np.array(state).reshape(n, n)
            return int(round(np.linalg.det(A))) == 0  # det is float

        empties = [i for i, v in enumerate(state) if v == -1]

        if turn == 0: 
            for k in empties:
                if solve(state[:k] + (0,) + state[k+1:], 1):
                    return True
            return False
        else:          
            for k in empties:
                if not solve(state[:k] + (1,) + state[k+1:], 0):
                    return False
            return True

    return solve(tuple([-1] * (n*n)), 0)

for n in range(1, 5):
    print(n, zero_player_wins_as_first(n))
