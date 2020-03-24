import os
import csv
PyBankcsv = os.path.join("/Users/jyan0/UCBwork/Python-project/Instructions/PyBank/Resources/budget_data.csv")
profit = []
monthly_changes = []
date = []
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0
with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        count = count+1
        date.append(row[0])
        profit.append(row[1])
        total_profit = total_profit+int(row[1])
        final_profit = int(row[1])
        monthly_changes_profits = final_profit - initial_profit
        monthly_changes.append(monthly_changes_profits)
        total_change_profits = total_change_profits + monthly_changes_profits
        initial_profit = final_profit
        average_change_profit = (total_change_profits/count)
        greatest_increase_profit = max(monthly_changes)
        greatest_decrease_profit = min(monthly_changes)
        greatest_increase_date = date[monthly_changes.index(greatest_increase_profit)]
        greatest_decrease_date = date[monthly_changes.index(greatest_decrease_profit)]
    print("total months:" + str(count))
    print("total profits:" +"$"+str(total_profit))
    print("average change:" +"$"+str(int(average_change_profit)))
    print("greatest increase profits:" + str(greatest_increase_date) + "$"+str(greatest_increase_profit))
    print("greatest decrease profits:" + str(greatest_decrease_date) + "$"+str(greatest_decrease_profit))



