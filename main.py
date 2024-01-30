from overheads import find_highest_overhead_category
from profit_loss import analyze_net_profit
from cash_on_hand import analyze_cash_on_hand


def main():
    # print(find_highest_overhead_category('./csv_reports/overheads-day-90.csv'))
    # print(analyze_cash_on_hand('./csv_reports/cash-on-hand.csv'))
    # print(analyze_net_profit('./csv_reports/profit-and-loss.csv'))
    with open('summary_report.txt', 'w') as summary:
        summary.write(find_highest_overhead_category('./csv_reports/overheads.csv')+'\n')
        summary.write(analyze_cash_on_hand('./csv_reports/cash-on-hand.csv')+'\n')
        summary.write(analyze_net_profit('./csv_reports/profit-and-loss.csv'))


main()
print('hello')


