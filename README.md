# Quantum Information Cosmology (QIC-S) - NGC 2403 Analysis

[![OSF](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2FZ9NWY-blue.svg)](https://osf.io/z9nwy/)
![Version](https://img.shields.io/badge/Version-3.9.11-green.svg)

**Version:** 3.9.11 (Definitive Edition)  
**Author:** Yoshiaki Sasada (Independent Researcher)

---

## 🚀 How to Reproduce Results (Ver.3.9.11)

To generate the definitive 4-panel plots (Rotation Curve, Residuals, Model Comparison, RAR) and verify the zero-parameter analysis, please run the following script:

```bash
python QIC_S_NGC2403_Analysis_v3911.py
```

> [!TIP]
> This script includes a simulation mode, so it runs successfully even without the external data file.

---

## Overview

This repository presents the theoretical framework and observational validation results for solving the galactic rotation curve problem based on **Quantum Information Cosmology (QIC-S)**.

In Ver.3.9.11, the consistency between theory and observation has been fully established. Analysis using NGC 2403 data demonstrates that QIC-S theory reproduces observational facts with high precision using only first principles of physical laws, without utilizing any free parameters (**Zero Parameters**).

---

## Key Achievements (Ver.3.9.11)

### 1. Theoretical Framework

This version marks the completion of the core QIC-S theory. The flattening of galactic rotation curves is explained not by unknown substances like Dark Matter, but by the following two physical mechanisms:

- **Critical New Massive Gravity (CNMG) on 3D Cauchy Slices:** A geometric approach based on the microscopic structure of spacetime.
- **Logarithmic Potential Correction:** A quantum informational correction term in long-range interactions.

### 2. Observational Validation

The validation results using the rotation curve data of NGC 2403 are as follows:

- **Zero Parameters:** The acceleration scale $a_0$ in the theory is not a fitting parameter but is uniquely determined from cosmological constants as $a_0 = 2\pi c H_0$.
- **High Precision:**
  - RMS: 4.8 km/s
  - $\chi^2_{\text{red}}$: 12.7
  - The theory naturally explains the data without arbitrary adjustments, performing comparably to or better than traditional Dark Matter models or MOND.

> [!NOTE]
> **On Statistical Interpretation:** While the RMS fit is excellent (4.8 km/s), the reduced χ² value ($\chi^2_{\text{red}}=12.7$) suggests the presence of systematic uncertainties (e.g., inclination angle, distance, non-circular motions) that are not fully accounted for in the current standard error budget. A comprehensive covariance analysis incorporating these systematic floors is planned for future updates.

### 3. Figure

**Figure 1: NGC 2403 Rotation Curve (QIC-S Ver.3.9.11)**  
*(Comparison between Theoretical Prediction (cyan line) and Observational Data (points with error bars))*

---

## Repository Contents

The main outputs are listed below. The paper and supplementary data are permanently stored and published on OSF.

| File | Description |
|------|-------------|
| `QIC_S_Paper_v3911.pdf` | The definitive paper summarizing the detailed theoretical derivation, mathematical backbone, and analysis results. |
| `NGC2403_QICS_v3911.png` | The graph of the rotation curve fitting result based on this theory. |
| `QIC_S_NGC2403_Analysis_v3911.py` | The definitive analysis code (Python). |

---

## External Resources

- **OSF Project Page:** <https://osf.io/z9nwy/>
- **Project DOI:** `10.17605/OSF.IO/Z9NWY`

---

## Future Roadmap (Post-Ver.4.0)

With the foundation established in Ver.3.9.11, future work will focus on rigorous mathematical formalization and expanding the scope of application:

1. **Theoremization of Assumptions:** Elevating current physical assumptions to mathematical theorems.
2. **Uniqueness of Ξ<sup>μν</sup>:** Proving the uniqueness and minimality of the emergent tensor (theory's core).
3. **Solar System Constraints:** Quantifying effects at smaller scales (e.g., Totani's direction).
4. **Model Comparison:** Statistical demonstration of superiority using BIC (Bayesian Information Criterion) against ΛCDM and MOND.

---

## Contact

For questions or discussions, please contact via [GitHub Issues](../../issues).

**Yoshiaki Sasada**  
Independent Researcher, Quantum Information Cosmology

---

## Citation

If you use this theory or code in your research, please cite the project via the OSF DOI:

```bibtex
@misc{Sasada2025QICS,
  title   = {Emergent Galactic Dynamics from Critical Cauchy Slice Holography (QIC-S Ver.3.9.11)},
  author  = {Sasada, Yoshiaki},
  year    = {2025},
  publisher = {OSF},
  doi     = {10.17605/OSF.IO/Z9NWY},
  url     = {https://doi.org/10.17605/OSF.IO/Z9NWY}
}
```
