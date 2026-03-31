from Monte_Carlo import random_step
from Monte_Carlo import diff_mod3


def verify_invariance(start, steps=50):
    state = start
    initial = diff_mod3(state)

    for _ in range(steps):
        nxt = random_step(state)
        if nxt is None:
            break

        if diff_mod3(nxt) != initial:
            return False

        state = nxt

    return True

if __name__ == "__main__":
    test_states = [
        (1, 1, 4),  # collapse O
        (2, 2, 2),  # collapse O
        (3, 1, 2),  # collapse X
        (0, 1, 5)   # collapse X
    ]

    for s in test_states:
        print(s, diff_mod3(s), verify_invariance(s))