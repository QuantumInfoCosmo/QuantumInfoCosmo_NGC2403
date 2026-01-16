# Quantum Information Cosmology with Scalar Field (QIC-S)

[![OSF](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2FZ9NWY-blue.svg)](https://osf.io/z9nwy/)
![Version](https://img.shields.io/badge/Version-5.0-green.svg)

**Version:** 5.0  
**Author:** Yoshiaki Sasada (Independent Researcher)

---

## Overview

This repository presents **Quantum Information Cosmology with Scalar Field (QIC-S)**, a theoretical framework that explains galaxy rotation curves without invoking dark matter particles. The "missing mass" is interpreted as field energy of an information-theoretic scalar field emerging from spacetime's entropy structure.

### Key Features

- **Parameter-Free**: No free parameters to fit — effective mass profiles are derived solely from observed baryonic distributions
- **Universal**: Successfully tested across 7 diverse galaxies spanning 2 orders of magnitude in mass (10^9.4 – 10^11.3 solar masses)
- **99.46% Agreement**: Mean statistical agreement between QIC-S predictions and dynamically required masses

---

## Results Summary

| Galaxy   | Type   | M_Newton (M☉) | M_QIC (M☉) | Agreement |
|----------|--------|---------------|------------|-----------|
| DDO 154  | dIrr   | 2.46×10⁹     | 2.46×10⁹  | 100.21%   |
| NGC 2403 | SABcd  | 6.92×10¹⁰    | 6.81×10¹⁰ | 98.46%    |
| NGC 3198 | SBc    | 1.65×10¹¹    | 1.66×10¹¹ | 100.49%   |
| UGC 128  | LSB    | 1.67×10¹¹    | 1.75×10¹¹ | 104.28%   |
| NGC 5055 | SAbc   | 2.02×10¹¹    | 1.98×10¹¹ | 98.25%    |
| NGC 6503 | SAcd   | 5.57×10¹⁰    | 5.47×10¹⁰ | 98.11%    |
| IC 2574  | Irr    | 7.72×10⁹     | 7.44×10⁹  | 96.43%    |

**Mean Agreement: 99.46% ± 2.53%**

---

## Repository Contents

| File | Description |
|------|-------------|
| `qics_paper_v5.pdf` | Main paper with theoretical derivation and analysis |
| `QIC_S_NGC2403_Analysis_v3911.py` | Python analysis code (NGC 2403) |
| `data/` | Rotation curve data from SPARC database |
| `figures/` | Generated plots and figures |

---

## How to Reproduce

```bash
python QIC_S_NGC2403_Analysis_v3911.py
```

> [!TIP]
> The script includes a simulation mode and runs successfully even without external data files.

---

## Theoretical Framework

QIC-S introduces a scalar information field D(x,t) whose gradient energy manifests as effective gravitational mass:

- **Field-Density Correspondence**: ρ_eff = (∇D)²
- **Energy Conservation**: M_eff(r) = ∫ 4πr² (∇D)² dr
- **Local Response**: The field D is induced by baryonic matter distribution

The framework is inspired by holographic principles and entropic gravity, but provides concrete, parameter-free predictions.

---

## External Resources

- **OSF Project**: [https://osf.io/z9nwy/](https://osf.io/z9nwy/)
- **DOI**: 10.17605/OSF.IO/Z9NWY
- **SPARC Database**: [http://astroweb.cwru.edu/SPARC/](http://astroweb.cwru.edu/SPARC/)

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
