# Quantum Information Cosmology with Scalar Field (QIC-S)

**Ver 5.0 (Definitive Edition) - January 16, 2026**

## Overview
This repository contains the official implementation, datasets, and validation materials for the **Quantum Information Cosmology with Scalar Field (QIC-S)** theory.

QIC-S proposes a novel theoretical framework where the "missing mass" in galaxies is not a particle fluid (Dark Matter) but a manifestation of field energy associated with a scalar information field $D_{\rm eff}$, emerging from spacetime's information entropy. This theory successfully explains galaxy rotation curves without introducing any arbitrary free parameters.

## 📈 Key Result (Preview)
**NGC 2403: Newtonian Mass vs QIC-S Field Energy**
The theory demonstrates a **98.46% agreement** between the Newtonian mass distribution and the QIC-S conserved field energy, confirming the "Zero-Parameter" universality.

![NGC 2403 Result](./figures/Figure_Preview.png)

## 📄 Paper & Citation
The full paper (Ver 5.0) is available in this repository and on OSF.

* **PDF in Repo:** [Sasada_QIC-S_Paper_Ver5.0.pdf](./Sasada_QIC-S_Paper_Ver5.0.pdf)
* **OSF Preprint:** [https://osf.io/yadkr/overview](https://osf.io/yadkr/overview)
* **DOI:** [10.17605/OSF.IO/YADKR](https://doi.org/10.17605/OSF.IO/YADKR)

## 📂 Python Codes (Usage Guide)
This repository includes both the latest rigorous codes for Ver 5.0 and the original legacy codes.

### 1. Ver 5.0 Official Codes (Recommended)
Use these scripts to reproduce the results and figures presented in the Ver 5.0 paper.

* **`QIC_S_NGC2403_Landscape.py`**
    * **Purpose:** Visualizes the "Hamiltonian Landscape" for NGC 2403.
    * **Output:** Generates the 3D effective potential and rotation curve fit shown in the paper.
    * **Target:** Single galaxy analysis (Demo).

* **`QIC_S_MultiGalaxy_Analysis.py`**
    * **Purpose:** Statistical verification across 7 galaxies (Spirals, Dwarfs, LSB).
    * **Output:** Calculates $\chi^2_{\nu}$ and BIC values to validate the "Zero-Parameter" universality.
    * **Target:** Full statistical validation.

### 2. Legacy / Reference Codes
These are the original implementations, kept for historical reference and backward compatibility.

* **`qic_s_analysis.py`**
    * **Status:** Legacy (Popular)
    * **Description:** The original simple implementation. Excellent for understanding the basic concept of QIC-S.
    * **Note:** Contains Japanese comments.

* **`QICS_ZeroParam_Analysis.py`**
    * **Status:** Development / Beta
    * **Description:** Previous version of the multi-galaxy analysis tool. Useful for comparing development stages.

## 📊 Data & Figures
* **`data/`**: Contains the cleaned rotation curve data for 7 galaxies (NGC2403, NGC3198, NGC5055, NGC6503, IC2574, DDO154, UGC128).
* **`figures/`**: Contains high-resolution figures used in the paper.

## License
MIT License
