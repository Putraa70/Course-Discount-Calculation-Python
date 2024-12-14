# statistik.py

class Statistik:
    """
    Kelas Statistik untuk menghitung mean, median, dan modus secara manual.
    """

    def __init__(self, data):
        self.data = data

    def mean(self):
        """
        Menghitung rata-rata (mean) secara manual.
        """
        return sum(self.data) / len(self.data) if len(self.data) > 0 else None

    def median(self):
        """
        Menghitung median secara manual.
        """
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n == 0:
            return None
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

    def modus(self):
        """
        Menghitung modus secara manual.
        """
        if not self.data:
            return None
        frequency = {}
        for item in self.data:
            frequency[item] = frequency.get(item, 0) + 1
        max_freq = max(frequency.values())
        modus = [key for key, val in frequency.items() if val == max_freq]
        return modus
