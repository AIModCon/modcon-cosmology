#!/usr/bin/env python3

import argparse
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file-class-Pk", required=True)
    args = parser.parse_args()

    data = np.loadtxt(args.file_class)
    k_cl = data[:,0]; 
    Pk_cl = data[:,1]; 

    # -------- Figure 1: Column 2 --------
    plt.figure()
    plt.loglog(k_cl, Pk_cl, '-o', label="cosmicic", markersize=3,markerfacecolor="none")
    plt.xlabel("$k$")
    plt.ylabel("$P(k)$")
    plt.legend()
    plt.tight_layout()
    plt.savefig("Pk_CLASS.png", dpi=300)

if __name__ == "__main__":
    main()

