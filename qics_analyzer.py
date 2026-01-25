# -*- coding: utf-8 -*-
"""
================================================================================
QIC-S Theory: Hamiltonian Landscape Analyzer
Version: 2.0 (GitHub Public Release)
Author: Yoshiaki Sasada
License: MIT

Description:
    This script analyzes galaxy rotation curves using the QIC-S (Quantum 
    Information Cosmology - Sasada) theoretical framework. It visualizes 
    the "Hamiltonian Landscape" to distinguish between:
    - Phase 5 (Mature galaxies): Ordered, stable interface energy
    - Phase 4 (Germinating galaxies): Chaotic, entropic release

Usage:
    python qics_analyzer.py --file1 data/NGC2403_rotmod.dat --file2 data/ID830_rotmod.dat
    python qics_analyzer.py --file1 data/NGC6503_rotmod.dat  # Single galaxy mode

Data Format (SPARC standard):
    Column 0: Radius [kpc]
    Column 1: Observed velocity [km/s]
    Column 2: Error (optional)
    Column 3: Gas velocity [km/s]
    Column 4: Disk velocity [km/s]
    Column 5: Bulge velocity [km/s] (optional)

References:
    [1] Sasada, Y. (2026). QIC-S Theory Ver 8.0.5
    [2] Lelli, F. et al. (2016). SPARC Database. AJ, 152, 157.
================================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import argparse
import os
import sys

# ==========================================
# 1. PHYSICS CONSTANTS (QIC-S Theory)
# ==========================================
A0 = 1.23e-10       # Characteristic acceleration scale [m/s^2] (≈ cH₀/2π)
ML_DISK = 0.5       # Mass-to-light ratio for stellar disk [M☉/L☉]
ML_GAS = 1.0        # Mass-to-light ratio for gas (fixed)
ML_BULGE = 0.7      # Mass-to-light ratio for bulge [M☉/L☉]
KPC_TO_M = 3.086e19 # kpc to meters conversion
KMS_TO_MS = 1000.0  # km/s to m/s conversion

# ==========================================
# 2. COLOR SCHEME (Consistent with Paper)
# ==========================================
COLORS = {
    'observed_mature': 'cyan',      # Phase 5: Mature galaxy observation
    'observed_germinating': 'red',  # Phase 4: Germinating galaxy observation
    'prediction': 'white',          # QIC-S theoretical prediction (baryon only)
    'entropic_release': 'red',      # Energy excess region
    'background': 'black',
    'text': 'white',
    'title_mature': 'cyan',
    'title_germinating': 'orange'
}

# Landscape colormaps
CMAP_ORDER = 'viridis'   # Phase 5: Ordered (green-yellow concentric)
CMAP_CHAOS = 'magma'     # Phase 4: Chaotic (red-orange turbulent)


# ==========================================
# 3. QICS ANALYZER CLASS
# ==========================================
class QICSAnalyzer:
    """
    QIC-S Theory Galaxy Analyzer
    
    Analyzes rotation curves and generates Hamiltonian Landscape visualizations
    to determine the evolutionary phase of a galaxy.
    """
    
    def __init__(self, ml_disk=ML_DISK, ml_gas=ML_GAS, ml_bulge=ML_BULGE):
        """
        Initialize analyzer with mass-to-light ratios.
        
        Parameters:
            ml_disk: Mass-to-light ratio for stellar disk
            ml_gas: Mass-to-light ratio for gas
            ml_bulge: Mass-to-light ratio for bulge
        """
        self.ml_disk = ml_disk
        self.ml_gas = ml_gas
        self.ml_bulge = ml_bulge
        
    def load_sparc_file(self, filename):
        """
        Load a SPARC-format rotation curve data file.
        
        Parameters:
            filename: Path to the data file
            
        Returns:
            dict: Dictionary containing radius, velocities, and metadata
                  Returns None if loading fails
        """
        if not os.path.exists(filename):
            print(f"[ERROR] File not found: {filename}")
            return None
            
        try:
            data = np.loadtxt(filename, comments='#')
            
            # Extract columns
            r = data[:, 0]          # Radius [kpc]
            v_obs = data[:, 1]      # Observed velocity [km/s]
            
            # Handle optional error column
            if data.shape[1] > 2:
                v_err = data[:, 2] if not np.all(data[:, 2] == 0) else None
            else:
                v_err = None
            
            # Velocity components (absolute values to handle sign conventions)
            v_gas = np.abs(data[:, 3]) if data.shape[1] > 3 else np.zeros_like(r)
            v_disk = np.abs(data[:, 4]) if data.shape[1] > 4 else np.zeros_like(r)
            v_bul = np.abs(data[:, 5]) if data.shape[1] > 5 else np.zeros_like(r)
            
            # Compute baryonic velocity
            v_baryon = np.sqrt(
                (v_gas**2 * self.ml_gas) + 
                (v_disk**2 * self.ml_disk) + 
                (v_bul**2 * self.ml_bulge)
            )
            
            # Extract galaxy name from filename
            galaxy_name = os.path.basename(filename).replace('_rotmod.dat', '').replace('.dat', '')
            
            return {
                'name': galaxy_name,
                'radius': r,
                'v_obs': v_obs,
                'v_err': v_err,
                'v_baryon': v_baryon,
                'v_gas': v_gas,
                'v_disk': v_disk,
                'v_bulge': v_bul,
                'filename': filename
            }
            
        except Exception as e:
            print(f"[ERROR] Failed to load {filename}: {e}")
            return None
    
    def compute_qics_prediction(self, r, v_baryon):
        """
        Compute QIC-S theoretical prediction for rotation velocity.
        """
        # Baryonic gravitational acceleration
        g_bar = (v_baryon**2) / r * (KMS_TO_MS**2) / KPC_TO_M
        g_bar = np.where(g_bar < 1e-15, 1e-15, g_bar)
        
        # QIC-S interpolating function
        x = g_bar / A0
        g_tot = g_bar / (1 - np.exp(-np.sqrt(x)))
        
        # Convert back to velocity
        v_pred = np.sqrt(g_tot * r * KPC_TO_M) / KMS_TO_MS
        
        return v_pred
    
    def compute_hamiltonian_landscape(self, r, v_obs, v_baryon):
        """
        Compute the Hamiltonian Landscape for phase classification.
        """
        with np.errstate(divide='ignore', invalid='ignore'):
            force_diff = (v_obs**2 - v_baryon**2) / r
            force_diff = np.nan_to_num(force_diff, nan=0.0, posinf=0.0, neginf=0.0)
        
        dr = np.gradient(r)
        h_eff = np.cumsum(force_diff * dr)
        
        h_range = np.max(h_eff) - np.min(h_eff)
        if h_range > 0:
            h_eff_norm = (h_eff - np.min(h_eff)) / h_range
        else:
            h_eff_norm = np.zeros_like(h_eff)
        
        h_gradient = np.gradient(h_eff_norm)
        phase_metric = np.var(h_gradient) * 1000
        
        return h_eff_norm, phase_metric
    
    def classify_phase(self, phase_metric, threshold=0.5):
        """
        Classify galaxy evolutionary phase.
        """
        if phase_metric > threshold:
            return 4, "Phase 4: Germinating (Chaos)"
        else:
            return 5, "Phase 5: Mature (Order)"
    
    def analyze(self, data):
        """
        Perform full QIC-S analysis.
        """
        if data is None:
            return None
            
        r = data['radius']
        v_obs = data['v_obs']
        v_baryon = data['v_baryon']
        
        v_pred = self.compute_qics_prediction(r, v_baryon)
        h_eff, phase_metric = self.compute_hamiltonian_landscape(r, v_obs, v_baryon)
        phase, phase_label = self.classify_phase(phase_metric)
        energy_excess = np.maximum(0, v_obs - v_pred)
        
        return {
            **data,
            'v_pred': v_pred,
            'h_eff': h_eff,
            'phase_metric': phase_metric,
            'phase': phase,
            'phase_label': phase_label,
            'energy_excess': energy_excess
        }


# ==========================================
# 4. VISUALIZATION FUNCTIONS
# ==========================================
def plot_single_galaxy(results, ax_curve, ax_landscape, force_phase=None):
    if results is None:
        return
    
    r = results['radius']
    v_obs = results['v_obs']
    v_pred = results['v_pred']
    h_eff = results['h_eff']
    phase = force_phase if force_phase else results['phase']
    
    if phase == 5:
        obs_color = COLORS['observed_mature']
        title_color = COLORS['title_mature']
        cmap = CMAP_ORDER
        landscape_title = "Landscape: Order"
        show_excess = False
    else:
        obs_color = COLORS['observed_germinating']
        title_color = COLORS['title_germinating']
        cmap = CMAP_CHAOS
        landscape_title = "Landscape: Chaos"
        show_excess = True
    
    ax_curve.set_facecolor(COLORS['background'])
    ax_curve.plot(r, v_obs, color=obs_color, lw=2, label='Observed')
    ax_curve.plot(r, v_pred, 'w--', lw=1.5, alpha=0.9, label='QIC-S Pred')
    
    if show_excess:
        ax_curve.fill_between(r, v_pred, v_obs, 
                              where=(v_obs > v_pred),
                              color=COLORS['entropic_release'], 
                              alpha=0.3, 
                              label='Entropic Release')
    
    title = f"{results['name']} (Phase {phase})"
    ax_curve.set_title(title, color=title_color, fontsize=14, fontweight='bold')
    ax_curve.set_xlabel("Radius (kpc)", color=COLORS['text'])
    ax_curve.set_ylabel("Velocity (km/s)", color=COLORS['text'])
    ax_curve.legend(facecolor='black', labelcolor='white', loc='lower right')
    ax_curve.tick_params(colors=COLORS['text'])
    ax_curve.grid(alpha=0.3, color='gray')
    
    ax_landscape.set_facecolor(COLORS['background'])
    theta = np.linspace(0, 2*np.pi, 100)
    R, THETA = np.meshgrid(r, theta)
    Z = np.tile(h_eff, (100, 1))
    
    if phase == 4:
        turbulence_scale = min(0.2, results['phase_metric'] / 5)
        np.random.seed(42)
        Z += np.random.normal(0, turbulence_scale, Z.shape)
    
    ax_landscape.pcolormesh(THETA, R, Z, cmap=cmap, shading='gouraud')
    ax_landscape.set_title(landscape_title, color=COLORS['text'], fontsize=12, pad=10)
    ax_landscape.set_xticklabels([])
    ax_landscape.tick_params(colors=COLORS['text'])


def create_comparison_figure(results_list, output_filename="QICS_Analysis.jpg", 
                            title="QIC-S Theory: Hamiltonian Landscape Analysis"):
    n_galaxies = len(results_list)
    fig = plt.figure(figsize=(10*n_galaxies, 12), facecolor=COLORS['background'])
    gs = GridSpec(2, n_galaxies, figure=fig, hspace=0.25, wspace=0.15)
    
    for i, results in enumerate(results_list):
        if results is None: continue
        ax_curve = fig.add_subplot(gs[0, i], facecolor=COLORS['background'])
        ax_landscape = fig.add_subplot(gs[1, i], projection='polar', 
                                       facecolor=COLORS['background'])
        plot_single_galaxy(results, ax_curve, ax_landscape)
    
    plt.suptitle(title, color=COLORS['text'], fontsize=18, fontweight='bold', y=0.98)
    plt.savefig(output_filename, dpi=150, facecolor=COLORS['background'], 
                bbox_inches='tight', pad_inches=0.2)
    print(f"[SUCCESS] Figure saved: {output_filename}")
    return fig


# ==========================================
# 5. COMMAND LINE INTERFACE
# ==========================================
def main():
    parser = argparse.ArgumentParser(description='QIC-S Theory: Hamiltonian Landscape Analyzer')
    parser.add_argument('--file1', required=True, help='First galaxy data file')
    parser.add_argument('--file2', help='Second galaxy data file')
    parser.add_argument('--output', default='QICS_Analysis.jpg', help='Output filename')
    parser.add_argument('--title', default='QIC-S Theory: Hamiltonian Landscape Analysis')
    
    args = parser.parse_args()
    analyzer = QICSAnalyzer()
    results_list = []
    
    for fname in [args.file1, args.file2]:
        if fname:
            data = analyzer.load_sparc_file(fname)
            results = analyzer.analyze(data)
            results_list.append(results)
    
    create_comparison_figure(results_list, args.output, args.title)
    plt.show()
    return 0

if __name__ == "__main__":
    sys.exit(main())
