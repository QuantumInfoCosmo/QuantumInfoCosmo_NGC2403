# QIC-S Theory: Quantum Information Cosmology

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/Version-8.1-blue.svg)](https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403)

## Overview

**QIC-S (Quantum Information Cosmology - Sasada)** is a theoretical framework that explains galactic rotation curves without invoking Dark Matter particles. The theory treats spacetime as an information processing medium and proposes a **Two-Tier System**:

- **Tier 1 (Local)**: Galaxies as information processing units with local entropy production
- **Tier 2 (Global)**: Universal steady-state maintained by Interface Energy supply

### Key Features

- **Zero-Parameter Prediction**: Uses only the theoretical acceleration scale a₀ = cH₀/2π ≈ 1.23×10⁻¹⁰ m/s²
- **Hamiltonian Landscape Analysis**: Visualizes the effective potential structure of galaxies
- **Phase Classification**: Distinguishes mature (Order) vs. germinating (Chaos) galaxies

---

## Latest Results (Ver. 8.1)

### Phase Metric Analysis

| Galaxy | Type | Phase | Metric (M) | Interpretation |
|--------|------|-------|------------|----------------|
| NGC 6503 | Standard Spiral | 5 | 0.17 | Stable Order |
| UGC 128 | LSB Galaxy | 5 | 0.26 | Stable Order |
| NGC 2403 | SABcd Spiral | 5 | 0.30 | Stable Order |
| ID 830 | Transitional | 4 | 1.91 | Chaotic (Entropic Release) |

**Threshold**: M = 0.5 (Order/Chaos boundary)

### Key Figures

![Universality](figures/QICS_Universality_NGC6503_UGC00128.png)
*Figure 1: Universality of QIC-S across galaxy morphologies*

![Phase Transition](figures/QICS_Scientific_Result.png)
*Figure 2: Phase transition from Order to Chaos*

---

## Repository Structure

```
QuantumInfoCosmo_NGC2403/
├── README.md
├── LICENSE
├── papers/
│   ├── QIC-S_Ver8_1_Sasada_2026.pdf
│   ├── QIC-S_Paper_v3911.pdf
│   └── ...
├── code/
│   ├── qics_analyzer.py          # Main analysis script (Ver. 2.1)
│   ├── QICS_ZeroParam_Analysis.py
│   └── requirements.txt
├── data/
│   ├── NGC2403_rotmod.dat
│   ├── NGC6503_rotmod.dat
│   ├── UGC00128_rotmod.dat
│   ├── ID830_rotmod.dat
│   └── ...
└── figures/
    ├── QICS_Universality_NGC6503_UGC00128.png
    └── QICS_Scientific_Result.png
```

---

## Quick Start

### Requirements

```bash
pip install numpy matplotlib
```

### Basic Usage

```bash
# Single galaxy analysis
python qics_analyzer.py --file1 data/NGC2403_rotmod.dat

# Comparison analysis
python qics_analyzer.py --file1 data/NGC6503_rotmod.dat --file2 data/UGC00128_rotmod.dat
```

### Output

The script generates:
1. **Rotation curve plot**: Observed vs. QIC-S prediction
2. **Hamiltonian Landscape**: Polar visualization of H_eff gradient
3. **Phase Metric**: Quantitative classification (Order/Chaos)

---

## Theory Summary

### Fundamental Equation

The characteristic acceleration scale is derived from cosmological parameters:

```
a₀ = cH₀ / 2π ≈ 1.23 × 10⁻¹⁰ m/s²
```

### Phase Metric Definition

```python
M = Var(log(|∇H_eff| + ε))
```

- **M < 0.5**: Phase 5 (Mature, Ordered)
- **M > 0.5**: Phase 4 (Germinating, Chaotic)

### QIC-S Interpolation Function (RAR form)

```python
g_tot = g_bar / (1 - exp(-sqrt(g_bar / a₀)))
```

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 8.1 | 2026-01-26 | Scientific update: removed randomized visualization |
| 8.0.5 | 2026-01-25 | Two-Tier System formulation |
| 7.0 | 2026-01 | Conformal Interface theory integration |
| 5.1 | 2026-01-16 | 7-galaxy validation (99.46% agreement) |
| 3.9.11 | 2025-12-30 | CSH derivation of a₀ |

---

## Citation

If you use QIC-S in your research, please cite:

```bibtex
@article{Sasada2026QICS,
  author  = {Sasada, Yoshiaki},
  title   = {Quantum Information Cosmology (QIC-S): A Two-Tier Steady-State Universe},
  year    = {2026},
  version = {8.1},
  url     = {https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403}
}
```

---

## Data Sources

- **SPARC Database**: [Lelli, McGaugh & Schombert (2016)](http://astroweb.cwru.edu/SPARC/)
- **ID 830**: Obuchi et al. (2026), ApJ, 997, 156

---

## Acknowledgments

This research was assisted by AI systems (Claude for theoretical articulation and Gemini for numerical analysis). All physical interpretations and theoretical frameworks are the sole responsibility of the author.

---

## License

MIT License - See [LICENSE](LICENSE) for details.

---

## Contact

- **Author**: Yoshiaki Sasada
- **GitHub**: [@QuantumInfoCosmo](https://github.com/QuantumInfoCosmo)
- **OSF**: [https://osf.io/xxxxx](https://osf.io/)
