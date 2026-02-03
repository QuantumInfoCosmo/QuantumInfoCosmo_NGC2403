"""
QIC-S Phase Metric Analyzer (Ver 9.1 - Logic Aligned)
Author: Yoshiaki Sasada
Description: Calculates Phase Metric (M) and extracts scaling parameters (R, D_eff)
             using logic synchronized with the plotting scripts (Max-Radius logic).
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# ==========================================
# Configuration
# ==========================================
DATA_DIR = 'data'
OUTPUT_CSV = 'results/QIC_S_Result_N170.csv'  # Updated path for new structure
OUTPUT_IMAGE = 'images/Fig2_Phase_Histogram.png'
THRESHOLD = 0.5 
MIN_POINTS = 5 

def calculate_galaxy_metrics(df):
    """
    Calculates phase metric M and physical properties (R, D_eff) for scaling laws.
    Logic is synchronized with plot_scaling_law.py (Max-Radius method).
    Returns: (M, R_max, D_eff) or None if invalid.
    """
    try:
        # 1. Data Cleaning
        data = df.apply(pd.to_numeric, errors='coerce').dropna()
        r, v = data.iloc[:, 0].values, data.iloc[:, 1].values
        
        # Physical filter: Radius and Velocity must be positive
        mask = (r > 0) & (v > 0)
        r, v = r[mask], v[mask]
        
        if len(r) < MIN_POINTS: 
            return None
        
        # 2. Phase Metric M (Tier 1 Dynamics)
        grad_H = (v ** 2) / r 
        m_metric = np.var(np.log(grad_H))
        
        # 3. Scaling Law Parameters (Tier 2 Dynamics)
        # --- Logic synchronized with plot_scaling_law.py ---
        idx_max = np.argmax(r)
        r_max = r[idx_max]
        v_at_rmax = v[idx_max]
        d_eff = r_max * v_at_rmax
        
        return m_metric, r_max, d_eff

    except Exception as e:
        return None

def main():
    print(f"QIC-S Phase Metric Analyzer Ver 9.1")
    print(f"Analyzing SPARC data from: {DATA_DIR}...")
    
    # Ensure output directories exist
    os.makedirs('results', exist_ok=True)
    os.makedirs('images', exist_ok=True)
    
    files = glob.glob(os.path.join(DATA_DIR, '*_rotmod.dat'))
    results = []

    for f in files:
        try:
            df = pd.read_csv(f, sep=r'\s+', engine='python', header=None, comment='#')
            metrics = calculate_galaxy_metrics(df)
            
            if metrics:
                m, r_max, d_eff = metrics
                results.append({
                    'Galaxy': os.path.basename(f), 
                    'M': m,
                    'R': r_max,
                    'D_eff': d_eff
                })
        except Exception as e:
            print(f"Skipping {os.path.basename(f)}: {e}")
            continue

    # --- Save Results ---
    if not results:
        print("No valid data found!")
        return

    res_df = pd.DataFrame(results)[['Galaxy', 'M', 'R', 'D_eff']]
    res_df.to_csv(OUTPUT_CSV, index=False)
    
    # --- Statistics ---
    n_total = len(res_df)
    n_order = len(res_df[res_df['M'] < THRESHOLD])
    n_chaos = len(res_df[res_df['M'] >= THRESHOLD])
    
    print(f"\n[Analysis Complete]")
    print(f"Total valid samples: N={n_total}")
    print(f"Order Phase (M < {THRESHOLD}): {n_order} ({100*n_order/n_total:.1f}%)")
    print(f"Chaos Phase (M >= {THRESHOLD}): {n_chaos} ({100*n_chaos/n_total:.1f}%)")
    print(f"Results saved to: {OUTPUT_CSV}")
    
    # --- Visualization ---
    plt.figure(figsize=(11, 7))
    sns.set_style("ticks", {"axes.grid": True, "grid.linestyle": ":"})
    bins = np.arange(0, 2.6, 0.12)
    
    sns.histplot(res_df['M'], bins=bins, kde=True, color='purple', 
                 alpha=0.6, edgecolor='black', label='SPARC Dataset')
    plt.axvline(x=THRESHOLD, color='red', linestyle='--', linewidth=2.5, 
                label=f'Threshold (M={THRESHOLD})')

    # Annotations
    plt.text(0.1, plt.ylim()[1]*0.7, "Laminar Flux\n(Order Phase)", 
             color='blue', fontweight='bold', fontsize=12)
    plt.text(1.2, plt.ylim()[1]*0.3, "Turbulent Flux\n(Chaos Phase)", 
             color='red', fontweight='bold', fontsize=12)

    plt.title(f"QIC-S Phase Metric Distribution (N={n_total})", fontsize=20, pad=20)
    plt.xlabel("Phase Metric M [Hamiltonian Gradient Variance]", fontsize=14)
    plt.ylabel("Galaxy Count", fontsize=14)
    plt.xlim(-0.05, 2.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    plt.savefig(OUTPUT_IMAGE, dpi=300, bbox_inches='tight')
    print(f"Histogram saved to: {OUTPUT_IMAGE}")

if __name__ == "__main__":
    main()
