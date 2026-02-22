from collections import Counter
import random

def simulate(n=200):
    S = list(range(1, n+1))
    while len(S) > 1:
        i, j = random.sample(range(len(S)), 2)
        a, b = S[i], S[j]
        if a < b:
            a, b = b, a
        for idx in sorted([i, j], reverse=True):
            S.pop(idx)
        S.append(a - b)
    return S[0]

def distribution(n=200, trials=1000, seed=42):
    random.seed(seed)
    results = [simulate(n) for _ in range(trials)]
    e_parity = (n * (n + 1) // 2) % 2
    assert all(v % 2 == e_parity for v in results)
    return Counter(results)


dist = distribution(n=200, trials=5000, seed=42)
print(sorted(dist.keys()))
