import csv

def find_trend(differences):
    if all(diff > 0 for diff in differences):
        return 'increasing'
    elif all(diff < 0 for diff in differences):
        return 'decreasing'
    else:
        return 'fluctuating'

def analyze_net_profit(file_path):
    with open(file_path, 'r', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        
        # open the file and read data and seperte days and net_profits
        days = []
        net_profits = []
        for row in reader:
            days.append(int(row['Day']))
            net_profits.append(int(row['Net Profit']))

    # finsd all diffferencs
    differences = []
    for i in range(1, len(net_profits)):
        differences.append(net_profits[i] - net_profits[i-1])

    # Checking if cash-on-hand is always increasing, always decreasing, or fluctuating
    trend= find_trend(differences)
    
    # if trend is increasing
    if trend=='increasing':
        max_increment_day = days[differences.index(max(differences)) + 1]
        max_increment_amount = max(differences)
        return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY {max_increment_day}, AMOUNT: {max_increment_amount}"
    # if trend is decsreasing
    elif trend== 'decreasing':
        max_decrement_day = days[differences.index(min(differences)) + 1]
        max_decrement_amount = min(differences)
        return f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n[HIGHEST NET PROFIT DEFICIT] DAY {max_decrement_day}, AMOUNT: {max_decrement_amount}"
    # if trned is flucutuating
    else:
        deficits = [(days[i], differences[i]) for i in range(len(differences)) if differences[i] < 0]
        top_deficits = sorted(deficits, key=lambda x: x[1])[:3]

        return f"[NET PROFIT FLUCTUATING] NET PROFIT ON EACH DAY IS FLUCTUATING\n[TOP 3 DEFICITS] (1). DAY {top_deficits[0][0]} AMOUNT {top_deficits[0][1]}, (2). DAY {top_deficits[1][0]} AMOUNT {top_deficits[1][1]}, (3). DAY {top_deficits[2][0]}, AMOUNT {top_deficits[2][1]}"






# Test data for continous profit
# 35,24303924,8866269,2605990,6260279
# 36,24471890,8953446,2661675,6291771
# 37,25233785,9345165,2716605,6628560
# 38,25797345,9635457,2771130,6864327
# 39,26020982,9748900,2825655,6874707
# 40,26034115,9755787,2881080,6923245
            
# test data for continous deficit
# Day,Sales,Trading Profit,Operating Expense,Net Profit
# 55,24581954,10961651,3103600,7858051
# 56,25243070,11352799,3489523,7855275
# 57,24439292,10868637,3025395,7843242
# 58,25080914,11252470,3411504,7832965
# 59,24915273,11154876,2946830,7620749
# 60,23996300,10579870,3334127,7533040




# import csv
# file_path = "./csv_reports/profit-and-loss-1.csv"


# def read_csv(file_path):
#     data = []
#     with open(file_path, "r", encoding="utf-8-sig") as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             data.append(row)
#     return data


# def compute_net_profit_difference(data):
#     profit_per_day = [(int(row["Day"]), int(row["Net Profit"])) for row in data]
#     differences = [(profit_per_day[i][0], profit_per_day[i][1] - profit_per_day[i - 1][1]) for i in range(1, len(profit_per_day))]
#     return differences


# def analyze_net_profit():
#     # Read data from file
#     data = read_csv(file_path)
#         #find difffences in the net profit colmn 
#     differences = compute_net_profit_difference(data)
#     # If the difference is positive and always increasing from top to bottom, then set increasing True
#     increasing = all(diff[1] >= 0 for diff in differences)
#     # If the difference is negative and always decreasing from top to bottom, then set decreasing True
#     decreasing = all(diff[1] <= 0 for diff in differences)
#     # If the difference is fulctuating and not stable from top to bottom, then set fluctuating True
#     fluctuating = not increasing and not decreasing
    
    
#     if increasing:
#         max_difference = max(differences, key=lambda x: x[1])
#         return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY: {max_difference[0]}, AMOUNT: {max_difference[1]}"
#     elif decreasing:
#         min_difference = min(differences, key=lambda x: x[1])
#         return f"[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN PREVIOUS DAY\n[HIGHEST NET PROFIT SURPLUS] DAY: {min_difference[0]}, AMOUNT: {min_difference[1]}"

#     elif fluctuating:
#         print('Achhhaaa')
#         deficit_days = [diff[0] for  diff in differences if diff[1] < 0]
#         deficit_amounts = [diff[1] for diff in differences if diff[1] < 0]

#         # Find top 3 deficit amounts and corresponding days
#         top_deficits = sorted(
#             zip(deficit_days, deficit_amounts), key=lambda x: x[1], reverse=True
#         )[:3]
#         return f'[NET PROFIT FLUCTUATING] NET PROFIT FLUCTUATES DURING THE WHOLE PERIOD\n[TOP 3 HIGHEST DEFICITS] (1) DAY: {top_deficits[0][0]}, AMOUNT: {top_deficits[0][1]},(2) DAY: {top_deficits[1][0]}, AMOUNT: {top_deficits[1][1]},(3) DAY: {top_deficits[2][0]}, AMOUNT: {top_deficits[2][1]},'
