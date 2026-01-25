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
from matplotlib.patches import FancyArrowPatch

def T(x, y):
    return (y, (x + y) % 10)

G = nx.DiGraph()
for x in range(10):
    for y in range(10):
        G.add_edge((x, y), T(x, y))

cycles = list(nx.simple_cycles(G))
print(f"Number of distinct bracelets (cycles): {len(cycles)}")

# 너무 짧지도, 너무 길지도 않은 사이클 하나만 골라서 그림
cycles_sorted = sorted(cycles, key=len)
candidates = [c for c in cycles_sorted if 10 <= len(c) <= 20]
cycle = candidates[-1] if candidates else cycles_sorted[len(cycles_sorted) // 2]

H = G.subgraph(cycle).copy()
pos = nx.circular_layout(H, scale=2.0)

fig, ax = plt.subplots(figsize=(7, 7))

nx.draw_networkx_nodes(
    H, pos,
    node_size=1200,
    linewidths=1.3,
    edgecolors="black",
    node_color="#D9ECFF",
    ax=ax,
)

labels = {n: f"({n[0]},{n[1]})" for n in H.nodes()}
nx.draw_networkx_labels(
    H, pos,
    labels=labels,
    font_size=9,
    font_weight="bold",
    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="black", lw=0.6),
    ax=ax,
)

for u, v in H.edges():
    if u == v:
        x, y = pos[u]
        loop = FancyArrowPatch(
            (x, y), (x, y),
            connectionstyle="arc3,rad=0.6",
            arrowstyle="-|>",
            mutation_scale=16,
            lw=1.3,
            color="black",
        )
        ax.add_patch(loop)
    else:
        ax.annotate(
            "",
            xy=pos[v], xycoords="data",
            xytext=pos[u], textcoords="data",
            arrowprops=dict(
                arrowstyle="-|>",
                lw=1.3,
                color="black",
                shrinkA=18, shrinkB=18,
                connectionstyle="arc3,rad=0.15",
            ),
        )

m = len(cycle)
ax.set_title(
    f"Transition graph cycle (bracelet) of length {m}\n"
    r"$T(x,y) = (y,\ (x+y)\ \mathrm{mod}\ 10)$",
    fontsize=13,
    pad=16,
)

ax.set_axis_off()
ax.set_aspect("equal")

plt.savefig("bracelet_cycle_presentable.png", dpi=300, bbox_inches="tight")
plt.show()