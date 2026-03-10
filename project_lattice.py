"""
TriTetra Theory — ProjectLattice Visualizer
=============================================
3D visualization of the nine-point octahedral system using matplotlib.
Shows stable (blue) and stressed (red) states side by side.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from nine_point_system import NinePointSystem


POINT_LABELS = [
    "R1", "R2", "R3",        # real axis
    "I1", "I2", "I3", "I4",  # imaginary axes
    "O1", "O2",               # origins
]

COLORS = {
    "real":   "#2196F3",
    "imag":   "#FF9800",
    "origin": "#9C27B0",
}


def plot_system(ax, system: NinePointSystem, title: str) -> None:
    pts = system.all_points()
    colors = (
        [COLORS["real"]] * 3
        + [COLORS["imag"]] * 4
        + [COLORS["origin"]] * 2
    )
    ax.scatter(pts[:, 0], pts[:, 1], pts[:, 2], c=colors, s=80, depthshade=True)
    for i, (p, label) in enumerate(zip(pts, POINT_LABELS)):
        ax.text(p[0], p[1], p[2], f"  {label}", fontsize=7)
    # Draw edges between all pairs
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            ax.plot(
                [pts[i, 0], pts[j, 0]],
                [pts[i, 1], pts[j, 1]],
                [pts[i, 2], pts[j, 2]],
                "gray", alpha=0.2, linewidth=0.5,
            )
    stress = system.stress_magnitude()
    ax.set_title(f"{title}\nStress |Σv| = {stress:.4f}", fontsize=10)
    ax.set_xlabel("Real"); ax.set_ylabel("Imag"); ax.set_zlabel("Sub-Imag")


def visualize(delta: float = 0.3) -> None:
    fig = plt.figure(figsize=(12, 5))
    fig.suptitle("ProjectLattice — TriTetra Nine-Point System", fontsize=13)

    # Stable state
    ax1 = fig.add_subplot(121, projection="3d")
    stable = NinePointSystem.ideal_octahedron()
    plot_system(ax1, stable, "Stable State (δ = 0)")

    # Stressed state
    ax2 = fig.add_subplot(122, projection="3d")
    stressed = NinePointSystem.ideal_octahedron()
    stressed.apply_perturbation(delta=delta)
    plot_system(ax2, stressed, f"Stressed State (δ = {delta})")

    plt.tight_layout()
    plt.savefig("../figures/project_lattice.png", dpi=150)
    print("Saved → figures/project_lattice.png")
    plt.show()


if __name__ == "__main__":
    visualize(delta=0.3)
