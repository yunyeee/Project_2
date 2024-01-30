import csv


# funciton to find differences between entris of cash on hand column
def find_differences(cash_on_hand):
    differences = []
    for i in range(1, len(cash_on_hand)):
        differences.append(cash_on_hand[i] - cash_on_hand[i-1])
    return differences


# fnction fo find whethre trend is increasing, decreasing or fluctuaintg
def find_trend(differences):
    if all(diff > 0 for diff in differences):
        return 'increasing'
    elif all(diff < 0 for diff in differences):
        return 'decreasing'
    else:
        return 'fluctuating'
    


def analyze_cash_on_hand(file_path):
    with open(file_path, 'r', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        
        # Extracting data from CSV
        days = []
        cash_on_hand = []
        for row in reader:
            days.append(int(row['Day']))
            cash_on_hand.append(int(row['Cash On Hand']))

    # Computing differences in Cash-On-Hand
    differences=find_differences(cash_on_hand)

    # Checking if cash-on-hand is always increasing, always decreasing, or fluctuating
    trend=find_trend(differences)

    # if trend is increasing
    if trend=='increasing':
        max_increment_day = days[differences.index(max(differences)) + 1]
        max_increment_amount = max(differences)
        return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n[HIGHEST CASH SURPLUS] DAY {max_increment_day}, AMOUNT: {max_increment_amount}"
    # if trend is decreasing
    elif trend=='decreasing':
        print('heelllo')
        max_decrement_day = days[differences.index(min(differences)) + 1]
        max_decrement_amount = min(differences)
        return f"[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n[HIGHEST CASH DEFICIT] DAY {max_decrement_day}, AMOUNT: {max_decrement_amount}"
    # if trend is fluctuating
    else:
        deficits = [(days[i], differences[i]) for i in range(len(differences)) if differences[i] < 0]
        top_deficits = sorted(deficits, key=lambda x: x[1])[:3]
        
        return f"[CASH FLUCTUATING] CASH ON EACH DAY IS FLUCTUATING\n[TOP 3 DEFICITS] (1). DAY {top_deficits[0][0]} AMOUNT {top_deficits[0][1]}, (2). DAY {top_deficits[1][0]} AMOUNT {top_deficits[1][1]}, (3). DAY {top_deficits[2][0]}, AMOUNT {top_deficits[2][1]}"

