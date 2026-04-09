from graf_stat import GrafStat
from logs import log

@log
def main():
    gs = GrafStat("personal_transactions.csv")
    gs.plot_pay_system_pie()


if __name__ == "__main__":
    main()
