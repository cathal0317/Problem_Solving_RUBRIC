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

import networkx as nx
import matplotlib.pyplot as plt

# Transition map
def T(x, y):
    return (y, (x + y) % 10)

# Build directed graph
G = nx.DiGraph()
for x in range(10):
    for y in range(10):
        G.add_edge((x, y), T(x, y))

# Find all cycles (each cycle = one bracelet)
cycles = list(nx.simple_cycles(G))
print(f"Number of distinct bracelets: {len(cycles)}")

# Choose one representative cycle to visualise
cycle = max(cycles, key=len)   # Longest cycle 
H = G.subgraph(cycle)

# Circular layout looks best for cycles
pos = nx.circular_layout(H)

# Plot
plt.figure(figsize=(5, 5))
nx.draw(
    H,
    pos,
    with_labels=True,
    node_size=1400,
    node_color="#cfe8ff",
    edge_color="black",
    font_size=10,
    arrowsize=20,
    arrowstyle="-|>"
)

plt.title(f"One number bracelet (cycle length = {len(cycle)})")
plt.axis("off")

# Save for LaTeX
plt.savefig("bracelet_cycle.png", dpi=300, bbox_inches="tight")
plt.show()