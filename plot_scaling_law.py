"""
QIC-S Universal Scaling Law Plotter (Ver 9.1 - Pipeline Integrated)
Author: Yoshiaki Sasada
Description: Visualizes the universal scaling law of the effective transport coefficient 
             D_eff across galactic and filament scales. Now reads R and D_eff directly 
             from CSV for pipeline consistency.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import linregress

# ==========================================
# Configuration
# ==========================================
CSV_FILE = 'results/QIC_S_Result_N170.csv'  # Updated path
OUTPUT_IMAGE = 'images/Fig3_Scaling_Law.png'

# Filament Data (From Tudorache et al., 2025)
# Format: (Label, Radius_kpc, Velocity_km_s)
FILAMENT_DATA = [
    ("Filament Core", 50, 110),       # 0.05 Mpc
    ("HI Structure", 1700, 110),      # 1.7 Mpc
    ("Full Filament", 15000, 110)     # 15 Mpc
]

def main():
    # 1. Load Galaxy Data (Now includes R and D_eff)
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} not found.")
        print("Please run phase_analysis.py first.")
        return
    
    # Ensure output directory exists
    os.makedirs('images', exist_ok=True)
        
    df = pd.read_csv(CSV_FILE)
    
    # Verify required columns exist
    required_cols = ['Galaxy', 'M', 'R', 'D_eff']
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        print(f"Error: CSV missing columns: {missing}")
        print("Please regenerate CSV with phase_analysis.py Ver 9.1+")
        return
    
    print(f"Loaded {len(df)} galaxies from {CSV_FILE}")
    
    # 2. Prepare Filament Data
    filament_points = []
    for label, r, v in FILAMENT_DATA:
        d_eff = r * v
        filament_points.append({'Label': label, 'R': r, 'D_eff': d_eff})
        
    # 3. Fit Scaling Law (Power Law) - All data combined
    all_r = np.concatenate([df['R'].values, [p['R'] for p in filament_points]])
    all_d = np.concatenate([df['D_eff'].values, [p['D_eff'] for p in filament_points]])
    
    slope, intercept, r_value, p_value, std_err = linregress(
        np.log10(all_r), np.log10(all_d)
    )
    r_squared = r_value ** 2
    
    # 4. Visualization (Log-Log Plot)
    plt.figure(figsize=(12, 8))
    sns.set_style("whitegrid")
    
    # Plot Galaxies (Colored by Phase Metric M)
    sc = plt.scatter(df['R'], df['D_eff'], c=df['M'], cmap='coolwarm', 
                     s=50, alpha=0.7, edgecolors='k', 
                     label=f'SPARC Galaxies (N={len(df)})')
    plt.colorbar(sc, label='Phase Metric M (Order < 0.5 < Chaos)')
    
    # Plot Filament Points
    for pt in filament_points:
        plt.scatter(pt['R'], pt['D_eff'], color='gold', marker='*', 
                    s=300, edgecolors='black', zorder=10)
        plt.text(pt['R']*1.1, pt['D_eff'], 
                 f"  {pt['Label']}\n  ({pt['R']/1000:.1f} Mpc)", 
                 fontsize=11, fontweight='bold', color='darkorange', va='center')

    # Plot Trend Line
    x_range = np.linspace(min(all_r)*0.8, max(all_r)*1.5, 100)
    y_fit = 10**intercept * x_range**slope
    plt.plot(x_range, y_fit, 'k--', linewidth=1.5, alpha=0.8, 
             label=f'Universal Scaling Law\n(Slope = {slope:.2f}, R²={r_squared:.3f})')

    # Formatting
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Characteristic Scale R [kpc]', fontsize=14)
    plt.ylabel('Effective Transport Coefficient D_eff [kpc km/s]', fontsize=14)
    plt.title('Universal Scaling of Hamiltonian Dynamics: From Galaxies to Filaments', 
              fontsize=18)
    plt.legend(fontsize=12, loc='upper left')
    plt.grid(True, which="both", ls="--", alpha=0.4)
    
    plt.savefig(OUTPUT_IMAGE, dpi=300, bbox_inches='tight')
    
    # Output Summary
    print(f"\n[Success] Scaling Law Plot generated: {OUTPUT_IMAGE}")
    print(f"=" * 50)
    print(f"Scaling Law: D_eff ∝ R^{slope:.2f}")
    print(f"R² = {r_squared:.3f}")
    print(f"Standard Error: {std_err:.3f}")
    print(f"=" * 50)

if __name__ == "__main__":
    main()
