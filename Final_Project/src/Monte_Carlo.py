import random

def available_moves(state):
    a, b, c = state
    moves = []

    if a > 0 and b > 0:
        moves.append((a * b, (a - 1, b - 1, c + 2)))
    if b > 0 and c > 0:
        moves.append((b * c, (a + 2, b - 1, c - 1)))
    if c > 0 and a > 0:
        moves.append((c * a, (a - 1, b + 2, c - 1)))

    return moves


# def diff_mod3(state):
#     a, b, c = state
#     return ((a - b) % 3, (b - c) % 3)

def is_single_species(state):
    return sum(x > 0 for x in state) == 1

def random_step(state):
    moves = available_moves(state)
    if not moves:
        return None

    weights = [w for w, _ in moves]
    _, new_state = random.choices(moves, weights=weights, k=1)[0]
    return new_state

def simulate(start, max_steps=100):
    state = start
    seen = {state}

    for _ in range(max_steps):
        if is_single_species(state):
            return "collapsed"

        nxt = random_step(state)
        if nxt is None:
            return "stuck"

        if nxt in seen:
            return "repeat"

        seen.add(nxt)
        state = nxt

    return "max_steps"

def all_states(N):
    out = []
    for a in range(N + 1):
        for b in range(N + 1 - a):
            c = N - a - b
            out.append((a, b, c))
    return out

def experiment_N(N, trials=200, max_steps=100):
    results = {}

    for state in all_states(N):
        if is_single_species(state):
            continue

        counts = {"collapsed": 0, "repeat": 0, "stuck": 0, "max_steps": 0}

        for _ in range(trials):
            outcome = simulate(state, max_steps=max_steps)
            counts[outcome] += 1

        results[state] = counts

    return results

def print_summary(results):
    for state in sorted(results):
        print(state, "counts =", results[state])

if __name__ == "__main__":
    N = 6
    results = experiment_N(N, trials=500, max_steps=100)
    print_summary(results)