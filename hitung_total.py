def hitung_total(row):
    try:
        # Validasi kolom yang dibutuhkan
        if not all(key in row for key in ['Fee', 'Duration', 'Percentage Discount', 'Categories']):
            raise KeyError("Data tidak lengkap untuk menghitung total.")

        # Ambil data dengan validasi tipe data
        fee = float(row['Fee'])
        duration = int(row['Duration'])
        pers_disc = float(row['Percentage Discount'])

        # Hitung total discount
        total_discount = (fee * duration) * (pers_disc / 100.0)

        if row['Categories'] == 'PI':
            return (fee * duration) - total_discount - (total_discount * 0.02)
        else:
            return (fee * duration) - total_discount
    except ValueError as e:
        print(f"Error: Data tidak valid ({e})")
        return None
    except KeyError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error tak terduga: {e}")
        return None
