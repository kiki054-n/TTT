"""
TriTetra Theory — Nine-Point System
====================================
Core implementation of the nine-point octahedral stability model.

The nine points are:
  - 3 points on the real axis       (real_points)
  - 4 points on imaginary axes      (imag_points)
  - 2 central origin points         (origin_points)

Stability condition: vector sum of all nine points == 0
"""

import numpy as np
from dataclasses import dataclass, field
from typing import List


@dataclass
class NinePointSystem:
    """Represents a TriTetra nine-point system in 3D complex space."""

    real_points: np.ndarray = field(default_factory=lambda: np.zeros((3, 3)))
    imag_points: np.ndarray = field(default_factory=lambda: np.zeros((4, 3)))
    origin_points: np.ndarray = field(default_factory=lambda: np.zeros((2, 3)))

    def all_points(self) -> np.ndarray:
        """Return all 9 points as a (9, 3) array."""
        return np.vstack([self.real_points, self.imag_points, self.origin_points])

    def vector_sum(self) -> np.ndarray:
        """Compute the vector sum of all nine points."""
        return self.all_points().sum(axis=0)

    def is_stable(self, threshold: float = 1e-6) -> bool:
        """Check stability: vector sum must be near zero."""
        return np.linalg.norm(self.vector_sum()) < threshold

    def stress_magnitude(self) -> float:
        """Return the magnitude of the net displacement vector."""
        return float(np.linalg.norm(self.vector_sum()))

    def apply_perturbation(self, delta: np.ndarray) -> None:
        """Apply an external perturbation (stress) to all points."""
        noise = np.random.randn(*self.real_points.shape) * delta
        self.real_points += noise[:3]
        noise = np.random.randn(*self.imag_points.shape) * delta
        self.imag_points += noise[:4]

    @classmethod
    def ideal_octahedron(cls, scale: float = 1.0) -> "NinePointSystem":
        """
        Create a system initialized to an ideal nine-point octahedral geometry.
        Vector sum is zero by construction.
        """
        r = scale
        real_pts = np.array([[r, 0, 0], [-r, 0, 0], [0, 0, 0]])
        imag_pts = np.array([[0, r, 0], [0, -r, 0], [0, 0, r], [0, 0, -r]])
        origin_pts = np.array([[0, 0, 0], [0, 0, 0]])
        return cls(real_points=real_pts, imag_points=imag_pts, origin_points=origin_pts)


def stability_report(system: NinePointSystem) -> None:
    print("=== TriTetra Nine-Point Stability Report ===")
    print(f"  Vector sum    : {system.vector_sum()}")
    print(f"  Stress (|Σv|) : {system.stress_magnitude():.6f}")
    print(f"  Stable        : {system.is_stable()}")
    print("============================================")


if __name__ == "__main__":
    sys = NinePointSystem.ideal_octahedron(scale=1.0)
    stability_report(sys)

    print("\n[Applying perturbation δ=0.05]")
    sys.apply_perturbation(delta=0.05)
    stability_report(sys)
