import pandas as pd

def load_data():
    # Data awal 5 baris
    data_awal = [
        ["Spark", "DS", 20000, 30, 5],
        ["Hadoop", "DS", 25000, 40, 10],
        ["Pandas", "PI", 30000, 35, 5],
        ["Java", "PI", 22000, 60, 5],
        ["Pyspark", "DS", 26000, 50, 5]
    ]

    # Tambahkan nama kolom agar lebih jelas
    df = pd.DataFrame(data_awal, columns=["Courses", "Categories", "Fee", "Duration", "Percentage Discount"])

    # Data tambahan 5 baris
    data_tambahan = [
        ["Python", "DS", 23000, 45, 8],
        ["C++", "PI", 28000, 55, 7],
        ["JavaScript", "DS", 27000, 38, 6],
        ["Ruby", "PI", 21000, 30, 4],
        ["Go", "DS", 25000, 50, 9]
    ]

    df_tambahan = pd.DataFrame(data_tambahan, columns=["Courses", "Categories", "Fee", "Duration", "Percentage Discount"])

    # Gabungkan data
    df = pd.concat([df, df_tambahan], ignore_index=True)

    return df