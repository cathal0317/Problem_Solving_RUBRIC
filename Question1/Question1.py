# Problem: Bracelets
# Start with any two natural numbers less than 10. For example, 1 and 5. Make a ‘number
# bracelet’ like this: 1 → 5 → 6 → 1 → 7 → 8 → 5 → · · · . Continue this chain – what
# happens? How many different bracelets are there


## ******************************************************************************************************************************************* ##
## ******************************************************************************************************************************************* ##

# Brute force method to see the pattern
def Sequence(a,b):
    pos = []
    pos.append((a,b))
    while True:
        new = (pos[-1][0] + pos[-1][1])%10
        pos.append((pos[-1][1],new)) 
        if pos[-1][0] == a and pos[-1][1] == b:
            break
    return pos, len(pos)-1

print(Sequence(1,5))

## ******************************************************************************************************************************************* ##
## ******************************************************************************************************************************************* ##

def T(x, y):
    return (y, (x + y) % 10)

def enumerate_cycles():
    visited = set()
    cycles = []

    for x in range(10):
        for y in range(10):
            start = (x, y)
            # Prevent equivalent bracelet a
            if start in visited:
                continue

            # Evolve until we see a repeated position
            order = {}         
            path = []
            cur = start

            while cur not in order:
                order[cur] = len(path)
                path.append(cur)
                cur = T(*cur)

            # Extract the cycle part
            cycle_start_idx = order[cur]
            cycle = path[cycle_start_idx:] 

            # Mark all positions encountered as visited 
            for s in path:
                visited.add(s)

            cycles.append(cycle)

    return cycles

if __name__ == "__main__":
    cycles = enumerate_cycles()

    print("Number of disjoint cycles:", len(cycles))
    lengths = sorted(len(c) for c in cycles)
    print("Cycle lengths:", lengths)
    print("Sum of cycle lengths:", sum(lengths))

