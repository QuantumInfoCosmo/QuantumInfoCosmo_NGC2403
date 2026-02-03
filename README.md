# QIC-S Theory Ver 9.0

## Two-Tier Steady-State Cosmology & Universal Scaling Law

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Paper](https://img.shields.io/badge/Paper-Ver%209.0-success)](./Sasada_QIC-S_Ver9.0.pdf)
[![OSF](https://img.shields.io/badge/OSF-Preregistered-brightgreen)](https://osf.io/)
[![SPARC](https://img.shields.io/badge/Data-SPARC%20N%3D170-orange)](http://astroweb.cwru.edu/SPARC/)

**A unified theoretical framework explaining galactic rotation curves and cosmic structures through information thermodynamics — without particle dark matter.**

---

## 🔬 Abstract

QIC-S (Quantum Information Cosmology) reconceptualizes the universe as a **Two-Tier System**:

| Tier | Scale | Dynamics |
|------|-------|----------|
| **Tier 1** | Galactic | Regenerative cycles (Birth → Growth → Death → Rebirth) |
| **Tier 2** | Cosmic | Steady-state equilibrium via Cosmic Web |

This work establishes two definitive observational validations spanning **four orders of magnitude**.

---

## 🌌 Key Discoveries

### Discovery 1: Universal Scaling Law

A single power law connects galactic dynamics to cosmic large-scale structures:

```
D_eff ∝ R^1.38    (R² = 0.920)
```

![Universal Scaling Law](Fig3_Scaling_Law.png)

**Figure 3**: The effective transport coefficient scales continuously from individual galaxies (~1 kpc) through cosmic filaments (15 Mpc). Gold stars indicate filament data from Tudorache et al. (2025).

### Discovery 2: Statistical Verification (N=170)

Comprehensive SPARC database analysis confirms thermodynamic predictions:

| Phase | Criterion | Count | Percentage |
|-------|-----------|-------|------------|
| **Order** | M < 0.5 | 133 | 78.2% |
| **Chaos** | M ≥ 0.5 | 37 | 21.8% |

![Phase Distribution](Fig2_Phase_Histogram.png)

**Figure 2**: The sharp peak near M ≈ 0 demonstrates that mature galaxies have established stable interface energy connections with Tier 2.

---

## 📐 Theoretical Foundation

### Phase Metric

The Hamiltonian Landscape state is quantified by:

```
M = Var(log(|∇H| + ε))

where ∇H ≈ v²/r (information flux gradient)
```

### Fundamental Constant

Derived from first principles:

```
a₀ = cH₀ / 2π ≈ 1.2 × 10⁻¹⁰ m/s²
```

This zero-parameter foundation connects to the MOND acceleration scale while providing deeper theoretical motivation.

---

## 📂 Repository Structure

```
QuantumInfoCosmo_NGC2403/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── Sasada_QIC-S_Ver9.0.pdf     # Full paper
│
├── data/                       # Input data
│   └── (SPARC .dat files)      # Download from SPARC website
│
├── images/                     # Generated figures
│   ├── Fig1_Individual_Verification.png
│   ├── Fig2_Phase_Histogram.png
│   └── Fig3_Scaling_Law.png
│
├── results/                    # Analysis outputs
│   └── QIC_S_Result_N170.csv   # Complete analysis results
│
├── qics_analyzer.py            # Core calculation engine
├── phase_analysis.py           # Generate Fig 2 (histogram)
└── plot_scaling_law.py         # Generate Fig 3 (scaling law)
```

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install numpy pandas matplotlib scipy
```

### Data Preparation

Download SPARC rotation curve data from [astroweb.cwru.edu/SPARC](http://astroweb.cwru.edu/SPARC/) and place `.dat` files in `data/`.

### Reproduce Results

```bash
# Generate statistical verification (Fig 2)
python phase_analysis.py

# Generate universal scaling law (Fig 3)
python plot_scaling_law.py
```

---

## ✅ Testable Predictions

| # | Prediction | Status |
|---|------------|--------|
| 1 | LRD-Quasar transition objects discoverable by JWST | Pending |
| 2 | Interface density gradients steeper than NFW | Pending |
| 3 | Filament rotation follows universal scaling | ✓ Partial |
| 4 | 78.2% of galaxies in Order Phase (M < 0.5) | ✓ Verified |
| 5 | D_eff ∝ R^1.38 from kpc to Mpc | ✓ Discovered |

---

## 📊 Data Sources

| Source | Description | Reference |
|--------|-------------|-----------|
| **SPARC** | 175 galaxies with photometry + rotation curves | [Lelli et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016AJ....152..157L) |
| **Filament** | 15 Mpc rotating structure | [Tudorache et al. (2025)](https://ui.adsabs.harvard.edu/abs/2025MNRAS.544.4306T) |

---

## 📝 Citation

```bibtex
@article{Sasada2026QICS,
  title   = {Two-Tier Steady-State Cosmology and the Discovery of a 
             Universal Scaling Law: {QIC-S} Theory Ver 9.0},
  author  = {Sasada, Yoshiaki},
  year    = {2026},
  month   = {February},
  note    = {Independent Researcher},
  url     = {https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403}
}
```

---

## 🔗 Related Work

- **OSF Project**: [osf.io/9a3cd](https://doi.org/10.17605/OSF.IO/9A3CD)
- **Theoretical Background**: ER=EPR ([Maldacena & Susskind 2013](https://arxiv.org/abs/1306.0533))
- **Conformal Interfaces**: [Komatsu et al. (2025)](https://arxiv.org/abs/2512.11045)

---

## 🙏 Acknowledgments

- **SPARC Team**: F. Lelli, S. S. McGaugh, J. M. Schombert
- **Filament Data**: M. N. Tudorache et al.
- **AI Assistance**: Claude (theoretical articulation), Gemini (numerical analysis)

All physical interpretations and theoretical frameworks are the sole responsibility of the author.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  <i>© 2026 Yoshiaki Sasada — Independent Researcher</i>
</p>
