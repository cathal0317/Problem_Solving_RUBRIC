import numpy as np
from functools import lru_cache

def zero_player_wins(n: int, zero_starts: bool) -> bool:
    @lru_cache(None)
    def solve(state, turn):  
        if -1 not in state:
            A = np.array(state).reshape(n, n)
            return int(round(np.linalg.det(A))) == 0

        empties = [i for i, v in enumerate(state) if v == -1]

        if turn == 0:  # 0-player
            return any(solve(state[:k] + (0,) + state[k+1:], 1) for k in empties)
        else:          # 1-player
            return all(solve(state[:k] + (1,) + state[k+1:], 0) for k in empties)

    start_turn = 0 if zero_starts else 1
    return solve(tuple([-1] * (n*n)), start_turn)

for n in range(1, 5):
    print("n=", n,
          "zero-first:", zero_player_wins(n, True),
          "zero-second:", zero_player_wins(n, False))
