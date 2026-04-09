import pandas as pd
import matplotlib.pyplot as plt


class GrafStat:
    def __init__(self, csv_path: str):
        self.df = pd.read_csv(csv_path)

    def plot_pay_system_pie(self):
        # Группируем по типу карты
        grouped = self.df.groupby("Account Name")["Amount"].sum()

        # Цвета как на скрине
        colors = [
            "#2E7D32",  # тёмно-зелёный
            "#4CAF50",  # зелёный
            "#64B5F6",  # голубой
            "#FFEB3B"   # жёлтый
        ]

        # Создаём donut chart
        fig, ax = plt.subplots(figsize=(8, 8))

        wedges, texts, autotexts = ax.pie(
            grouped.values,
            labels=grouped.index,
            autopct="%1.0f%%",
            colors=colors[:len(grouped)],
            startangle=90,
            pctdistance=0.8,     # проценты ближе к центру
            textprops={"fontsize": 14, "weight": "bold"}
        )

        # Делаем дырку в центре (donut)
        centre_circle = plt.Circle((0, 0), 0.55, fc="white")
        fig.gca().add_artist(centre_circle)

        # Заголовок
        plt.title(
            "Траты по типу платежной системы ( в процентах % )",
            fontsize=18,
            weight="bold",
            pad=20
        )

        plt.tight_layout()
        plt.show()