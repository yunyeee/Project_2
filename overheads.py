import csv

def find_highest_overhead_category(file_path):
    with open(file_path, 'r', encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        
        # Extracting data from CSV
        categories = []
        overheads = []
        for row in reader:
            categories.append(row['Category'])
            overheads.append(float(row['Overheads']))

    # Finding the highest overhead category
    max_overhead_index = overheads.index(max(overheads))
    highest_overhead_category = categories[max_overhead_index]
    highest_overhead_value = overheads[max_overhead_index]

    return f"[HIGHET OVERHEAD] {highest_overhead_category}: {highest_overhead_value}%"

