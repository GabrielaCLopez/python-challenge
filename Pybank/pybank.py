import csv
import os

# assign the file to a variable
filepath = os.path.join("Resources", "budget_data.csv")
# the file that will be written to
output_file = os.path.join("Analysis", "budgetanalysis.txt")

# start values at zero and create lists
total_months = 0
total_net = 0
months_list = []
net_change_list = []
max_increase = ["", 0]
max_decrease = ["", 9999999999]

# this will start to read the csv vile
with open (filepath) as data:
    reader = csv.reader(data)
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous = int(first_row[1])

    # each row will be read
    for row in reader:
        # the months and net change are logged at each row
        total_months += 1
        total_net += int(row[1])
        net_change = int(row[1]) - previous
        previous = int(row[1])
        net_change_list += [net_change]
            # above same as net_change_list.append(net_change)
        months_list += [row[0]]
        # these will determine which month had the largest increase in profit and the largest decrease
        if net_change > max_increase[1]:
            max_increase[0] = row [0]
            max_increase[1] = net_change
        if net_change < max_decrease[1]:
            max_decrease[0] = row [0]
            max_decrease[1] = net_change

# calculates the average change
monthly_changeavg = sum(net_change_list)/len(net_change_list)

# the variables above are inserted into the summary below and then written to the text file
output = (f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_net:,.2f}
Average Change: ${monthly_changeavg:,.2f}
Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]:,.2f})
Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]:,.2f})

""")

print(output)

# write the information to the text file
with open (output_file, "w") as text:
    text.write(output)
