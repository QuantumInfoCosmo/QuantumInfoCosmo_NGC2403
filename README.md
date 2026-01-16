# Quantum Information Cosmology with Scalar Field (QIC-S)

[![OSF](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2FZ9NWY-blue.svg)](https://osf.io/yadkr/overview)
![Version](https://img.shields.io/badge/Version-5.0-green.svg)

**Version:** 5.0  
**Author:** Yoshiaki Sasada (Independent Researcher)

---

## Overview

This repository presents **Quantum Information Cosmology with Scalar Field (QIC-S)**, a theoretical framework that explains galaxy rotation curves without invoking dark matter particles. The "missing mass" is interpreted as field energy of an information-theoretic scalar field emerging from spacetime's entropy structure.

### Key Features

- **Parameter-Free**: No free parameters to fit - effective mass profiles are derived solely from observed baryonic distributions
- **Universal**: Successfully tested across 7 diverse galaxies spanning 2 orders of magnitude in mass
- **99.46% Agreement**: Mean statistical agreement between QIC-S predictions and dynamically required masses

---

## Results Summary

| Galaxy   | Type   | M_Newton | M_QIC | Agreement |
|----------|--------|----------|-------|-----------|
| DDO 154  | dIrr   | 2.46e9   | 2.46e9  | 100.21% |
| NGC 2403 | SABcd  | 6.92e10  | 6.81e10 | 98.46%  |
| NGC 3198 | SBc    | 1.65e11  | 1.66e11 | 100.49% |
| UGC 128  | LSB    | 1.67e11  | 1.75e11 | 104.28% |
| NGC 5055 | SAbc   | 2.02e11  | 1.98e11 | 98.25%  |
| NGC 6503 | SAcd   | 5.57e10  | 5.47e10 | 98.11%  |
| IC 2574  | Irr    | 7.72e9   | 7.44e9  | 96.43%  |

*Masses in solar mass units*

**Mean Agreement: 99.46% +/- 2.53%**

---

## Repository Contents

| File | Description |
|------|-------------|
| `qics_paper_v5.pdf` | Main paper with theoretical derivation and analysis |
| `qic_s_analysis.py` | Rotation curve analysis and Hamiltonian landscape visualization |
| `QICS_ZeroParam_Analysis.py` | Multi-galaxy zero-parameter analysis |
| `data/` | Rotation curve data from SPARC database |
| `figures/` | Generated plots and figures |

---

## How to Reproduce

```bash
# Single galaxy analysis with visualization
python qic_s_analysis.py

# Multi-galaxy zero-parameter analysis
python QICS_ZeroParam_Analysis.py
```

> [!TIP]
> Scripts include simulation mode and run successfully even without external data files.

---

## Theoretical Framework

QIC-S introduces a scalar information field D(x,t) whose gradient energy manifests as effective gravitational mass:

- **Field-Density Correspondence**: rho_eff = (grad D)^2
- **Energy Conservation**: M_eff(r) = integral of 4 pi r^2 (grad D)^2 dr
- **Local Response**: The field D is induced by baryonic matter distribution

The framework is inspired by holographic principles and entropic gravity, but provides concrete, parameter-free predictions.

---

## External Resources

- **OSF Project**: https://osf.io/yadkr/overview
- **DOI**: 10.17605/OSF.10.17605/OSF.IO/YADKR
- **SPARC Database**: http://astroweb.cwru.edu/SPARC/

---

## Citation

```bibtex
@misc{Sasada2026QICS,
  title   = {Quantum Information Cosmology with Scalar Field (QIC-S): 
             Parameter-Free Derivation of Galaxy Rotation Curves 
             from Information-Theoretic Field Energy},
  author  = {Sasada, Yoshiaki},
  year    = {2026},
  publisher = {OSF},
  doi     = {10.17605/OSF.IO/Z9NWY},
  url     = {https://doi.org/10.17605/OSF.IO/Z9NWY}
}
```

---

## Contact

For questions or discussions, please open a GitHub Issue.

**Yoshiaki Sasada**  
Independent Researcher, Quantum Information Cosmology
