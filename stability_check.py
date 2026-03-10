"""
TriTetra Theory — Stability Checker
=====================================
Evaluates whether a nine-point system remains stable under incremental stress,
and identifies the critical threshold at which the system breaks down.
"""

import numpy as np
from nine_point_system import NinePointSystem, stability_report


def find_critical_threshold(
    system: NinePointSystem,
    delta_step: float = 0.01,
    max_delta: float = 5.0,
) -> float:
    """
    Incrementally increase perturbation until stability is lost.
    Returns the critical delta at which the system first becomes unstable.
    """
    delta = 0.0
    while delta <= max_delta:
        test_sys = NinePointSystem(
            real_points=system.real_points.copy(),
            imag_points=system.imag_points.copy(),
            origin_points=system.origin_points.copy(),
        )
        test_sys.apply_perturbation(delta=delta)
        if not test_sys.is_stable(threshold=0.5):
            return delta
        delta += delta_step
    return float("inf")


if __name__ == "__main__":
    sys = NinePointSystem.ideal_octahedron(scale=1.0)
    print("Searching for critical breakdown threshold...")
    critical = find_critical_threshold(sys)
    print(f"  Critical threshold δ* ≈ {critical:.3f}")
