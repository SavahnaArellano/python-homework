# Dependencies
import csv

# Files
file_load = "/budget_data.csv"
file_output = "budget_analysis.txt"

# revenue calculations
total_months = 0
prev_revenue = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(file_load) as data:
    reader = csv.DictReader(data)

    for row in reader:

        # total change
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Average
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Output
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Terminal print
print(output)

# Txt export
with open(file_output, "w") as txt_file:
    txt_file.write(output)
