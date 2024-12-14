import pandas as pd
import numpy as np
from data_kursus import load_data
from perhitungan_statistik import Statistik
from hitung_total import hitung_total

def main():
    # Load data
    df = load_data()

    # Tambahkan kolom Total
    df['Total'] = df.apply(hitung_total, axis=1)

    # Hilangkan baris dengan Total None
    df = df.dropna(subset=['Total'])

    # Buat objek Statistik untuk Fee dan Total
    stat_fee = Statistik(df['Fee'].tolist())
    stat_total = Statistik(df['Total'].tolist())

    # Tampilkan hasil mean, median, modus Fee
    print("\nStatistik untuk Fee:")
    print("Mean Fee:", stat_fee.mean())
    print("Median Fee:", stat_fee.median())
    print("Modus Fee:", stat_fee.modus())

    # Tampilkan hasil mean, median, modus Total
    print("\nStatistik untuk Total:")
    print("Mean Total:", stat_total.mean())
    print("Median Total:", stat_total.median())
    print("Modus Total:", stat_total.modus())

    # Contoh penggunaan library numpy untuk cross-check mean Fee
    mean_fee_np = np.mean(df['Fee'])
    median_fee_np = np.median(df['Fee'])
    std_fee_np = np.std(df['Fee'])

    print("\nCross-Check dengan NumPy:")
    print("Mean Fee (NumPy):", mean_fee_np)
    print("Median Fee (NumPy):", median_fee_np)
    print("Standard Deviation Fee (NumPy):", std_fee_np)

if __name__ == '__main__':
    main()

