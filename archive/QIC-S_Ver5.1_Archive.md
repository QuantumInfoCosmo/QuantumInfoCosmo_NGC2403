# Quantum Information Cosmology with Scalar Field (QIC-S)
**Parameter-Free Derivation of Galaxy Rotation Curves**

[![GitHub](https://img.shields.io/badge/GitHub-Repo-black.svg?logo=github)](https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403)
[![OSF](https://img.shields.io/badge/OSF-10.17605%2FOSF.IO%2FYADKR-blue.svg)](https://osf.io/yadkr/)
![Version](https://img.shields.io/badge/Version-5.1-green.svg)

* **Version:** 5.1
* **Author:** Yoshiaki Sasada (Independent Researcher)
* **Status:** Complete / Archived

---

## 🌌 Overview

**Does the universe really need Dark Matter?**

This project presents **Quantum Information Cosmology with Scalar Field (QIC-S)**, a novel theoretical framework that resolves the galactic "missing mass" problem without postulating non-baryonic dark matter.

By treating gravity as an emergent phenomenon driven by the conservation of **Information Field Energy**, QIC-S naturally reproduces the flat rotation curves of galaxies.

### 🏆 Key Achievements

1.  **Parameter-Free**: Unlike $\Lambda$CDM (NFW profiles) or MOND ($a_0$), QIC-S requires **no tuning parameters**. The halo mass is mathematically derived solely from the visible baryonic distribution.

2.  **Universal Validity**: Tested against 7 diverse galaxies from the **SPARC database**, covering 2 orders of magnitude in mass ($10^{9.4} - 10^{11.3} M_\odot$).

3.  **Statistical Proof**: Achieved **99.46% ± 2.53%** agreement with dynamically required halo masses.

---

## 📐 Theoretical Framework

QIC-S posits that the "missing mass" is a manifestation of field energy associated with a scalar information field, $D(x,t)$, which emerges from the information entropy of spacetime.

### Core Equations

* **Field-Density Correspondence:**
    $\rho_{\rm eff} = (\nabla D)^2$

* **Energy Conservation:**
    $M_{\rm eff}(r) = \int 4\pi r^2 (\nabla D)^2 dr$

* **Local Response:**
    The field $D$ is induced locally by the baryonic matter distribution.

---

## 📂 Repository Contents

### Paper
* **`Sasada_QIC-S_Paper_Ver5.1.pdf`** : The full scientific paper (Main Text).

### Analysis Code
* **`QICS_ZeroParam_Analysis.py`** : True zero-parameter analysis (Definitive Edition, Ver 4.0).
* **`QIC_S_MultiGalaxy_Analysis.py`** : Multi-galaxy analysis code (8 galaxies).
* **`QIC_S_NGC2403_Landscape.py`** : Hamiltonian landscape visualization for NGC 2403.

### Data
* **`data/`** : Rotation curve data from SPARC database.
* **`figures/`** : Analysis plots and figures.

---

## 📝 Citation

If you use this theory or code in your research, please cite as:

```bibtex
@misc{Sasada2026QICS_v51,
  title   = {Quantum Information Cosmology with Scalar Field (QIC-S): Parameter-Free Derivation},
  author  = {Sasada, Yoshiaki},
  year    = {2026},
  version = {5.1},
  url     = {[https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403](https://github.com/QuantumInfoCosmo/QuantumInfoCosmo_NGC2403)}
}
