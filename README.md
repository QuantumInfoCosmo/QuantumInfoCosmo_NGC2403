# QIC-S: Quantum Information Cosmology - Sasada
# Quantum Information Cosmology - Sasada (QIC-S)
---
## 🚀 Update (Ver 2.1): Rigorous Data-Driven Analysis
**"No Random Noise. Just Pure Data."**

In Version 2.1, we have completely removed the illustrative randomized visualization. The "Hamiltonian Landscape" is now generated strictly from the **Log-Variance of the Hamiltonian Gradient**, providing a physical metric for distinguishing Galactic Phases.

### Visualization Result
![QIC-S Scientific Result](QICS_Scientific_Result.png)

### Scientific Interpretation
- **Left (NGC 2403 - Phase 5):**
  - **Metric: 0.30** (< 0.5)
  - Shows a smooth, low-variance gradient, indicating a stable "Order" state with steady interface energy supply.
- **Right (ID830 - Phase 4):**
  - **Metric: 1.91** (> 0.5)
  - Shows high-variance fluctuations. The visualization directly maps the **entropic release**, proving the "Chaos" state without any artificial rendering.
---


[![DOI](https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2FMBJN9-blue)](https://doi.org/10.17605/OSF.IO/MBJN9)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/Version-8.0.5-green.svg)]()

> **Current Version: QIC-S Theory Ver. 8.0.5** (This repository corresponds to the published PDF manuscript)

---

## Abstract

**Quantum Information Cosmology - Sasada (QIC-S)** proposes a unified cosmological framework that reconceptualizes the universe as a **Two-Tier System**. This theory reinterprets the dark matter problem not as evidence for exotic particles, but as the manifestation of **Conformal Interface Energy** — the energy cost arising at boundaries between regions of differing effective Hamiltonians, supplied by the steady-state cosmic infrastructure (Tier 2) to individual galactic systems (Tier 1).

The framework achieves **99.46% agreement** with observed SPARC rotation curve morphologies without invoking free parameters.

---

## Quick Start: Reproduce the Figures

To generate the Hamiltonian Landscape figures shown below, run:

```bash
# 1. Clone this repository
git clone https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403.git
cd QuantumInfoCosmo_NGC2403

# 2. Install dependencies
pip install numpy matplotlib

# 3. Run the main analysis script
python qics_analyzer.py --file1 data/NGC2403_rotmod.dat --file2 data/ID830_rotmod.dat
```

**Output:** `fig1_phase5.jpg` and `fig2_phase4_vs_5.jpg`

---

## Observational Evidence: Hamiltonian Landscape

### Figure 1: Universality of Interface Energy (Phase 5)

![Figure 1: Phase 5 Universality](fig1_phase5.jpg)

*Hamiltonian Landscape analysis of mature galaxies NGC 6503 and UGC 128. Both exhibit ordered concentric patterns, demonstrating universal Interface Energy supply from Tier 2.*

### Figure 2: Phase Transition Visualization (Phase 4 vs Phase 5)

![Figure 2: Order vs Chaos](fig2_phase4_vs_5.jpg)

*Comparison between NGC 2403 (Phase 5, Ordered) and ID830 (Phase 4, Chaotic). The high-redshift quasar ID830 (z=3.4) exhibits turbulent Hamiltonian Landscape consistent with ongoing Entropic Release.*

---

## Repository Contents

| File | Description | Version |
|------|-------------|---------|
| 📄 `QIC-S_Ver8.0.5_Sasada_2026.pdf` | **Primary manuscript** — Full theoretical framework | **Ver 8.0.5** |
| 🐍 `qics_analyzer.py` | **Main analysis engine** — Generates Hamiltonian Landscape figures | **Ver 8.0.5** |
| 📁 `data/` | SPARC-format rotation curve data (NGC 2403, ID830, etc.) | — |
| 🖼️ `fig1_phase5.jpg` | Phase 5 universality figure | — |
| 🖼️ `fig2_phase4_vs_5.jpg` | Order vs Chaos comparison figure | — |
| 📁 `archive/` | Previous versions (v5.1, v7.0, etc.) | — |

> **Note:** `qics_analyzer.py` is the Ver 8.0.5-aligned analysis script that produces all figures in the manuscript.

---

## Theoretical Framework

### The Two-Tier Architecture

| Tier | Scale | Dynamics | Physical Basis |
|------|-------|----------|----------------|
| **Tier 1** | Galactic | Cyclic (Birth → Maturation → Death → Regeneration) | ER=EPR information transport |
| **Tier 2** | Cosmic | Stationary (Eternal Present) | Conformal Interfaces via Cosmic Web |

### Six-Phase Galactic Cycle

1. **Phase 1:** Information Encoding — Little Red Dots (LRDs)
2. **Phase 2:** Information Transmission — ER=EPR bridges
3. **Phase 3:** Spatial Emergence — Holographic reconstruction
4. **Phase 4:** Burst-like Germination — Entropic Release (Chaotic)
5. **Phase 5:** Maturation — Interface Energy (Ordered)
6. **Phase 6:** Return to Tier 2 — Hawking radiation

---

## Data Format

Input files follow the SPARC database format (Lelli et al. 2016):

| Column | Description | Unit |
|--------|-------------|------|
| 0 | Radius | kpc |
| 1 | Observed velocity | km/s |
| 2 | Velocity error | km/s |
| 3 | Gas velocity | km/s |
| 4 | Disk velocity | km/s |
| 5 | Bulge velocity | km/s |

---

## Testable Predictions

| Prediction | Observable | Timeline |
|------------|------------|----------|
| LRD-to-Quasar Transition | Intermediate objects (Phase 1 → 4) | JWST 2026–2030 |
| Interface Sharpness | Steeper halo gradients than NFW | Weak lensing surveys |
| Filament Rotation | Universal rotation in cosmic filaments | SKA, Euclid 2027–2035 |

---

## References

1. Kokubo, M. & Harikane, Y. (2025). *ApJ*, 995, 24.
2. Obuchi, S. et al. (2026). *ApJ*, 997, 156.
3. Tudorache, M. N. et al. (2025). *MNRAS*, 544, 4306.
4. Komatsu, S. et al. (2025). arXiv:2512.11045.
5. Maldacena, J. & Susskind, L. (2013). *Fortsch. Phys.*, 61, 781.
6. Lie, S. H. & Ng, N. H. Y. (2024). *Phys. Rev. Research*, 6, 033144.
7. Penrose, R. (2010). *Cycles of Time*.

---

## Citation

```bibtex
@misc{sasada2026qics,
  author       = {Sasada, Yoshiaki},
  title        = {{QIC-S}: Quantum Information Cosmology - Sasada, Ver 8.0.5},
  year         = {2026},
  doi          = {10.17605/OSF.IO/MBJN9},
  url          = {https://doi.org/10.17605/OSF.IO/MBJN9}
}
```

---

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

---

## Acknowledgments

This research was conducted with the assistance of AI systems (Claude for theoretical articulation, Gemini for numerical analysis). The author retains sole responsibility for all physical interpretations and scientific conclusions.

---

## Contact

For questions or collaboration inquiries, please open an [Issue](https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403/issues).
