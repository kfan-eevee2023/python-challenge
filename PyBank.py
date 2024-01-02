
import csv
import os
 
# csv file name
csv_file = os.path.join("Resources","budget_data.csv")

# result file name
text_file = os.path.join("analysis","PyBank_Result.txt")


# variable to store header row
fields = []
 
# variables for output
num_months = 0
curr_pl = 0
curr_month = ''
first_pl = 0
last_pl = 0
pre_pl = 0
total_pl = 0
avg_pl = 0
change_pl = 0
avg_change = 0
greatest_inc = 0
greatest_inc_month = ''
greatest_dec = 0
greatest_dec_month = ''

# reading csv file
with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # extracting headers through first row
    fields = next(csvreader)
     
    # extracting each data row one by one
    for row in csvreader:
        #print("Current Record: {}, {}, {}".format(num_months, row[0], row[1]))
        num_months = num_months + 1
        curr_month = row[0]
        curr_pl = int(row[1])
        if  num_months == 1:
            first_pl = curr_pl
            pre_pl = curr_pl
        last_pl = curr_pl
        total_pl = total_pl + curr_pl
        change_pl = change_pl + (curr_pl - pre_pl)
        if  curr_pl - pre_pl >= greatest_inc:
            greatest_inc = curr_pl - pre_pl
            greatest_inc_month = curr_month
        if  curr_pl - pre_pl <= greatest_dec:
            greatest_dec = curr_pl - pre_pl
            greatest_dec_month = curr_month
        pre_pl = curr_pl
        

#if  num_months != 0:
#   avg_pl = round(total_pl / num_months, 2)

if  num_months > 1:
    avg_change = round(change_pl / (num_months - 1), 2)
    

# printing the header row
#print("----------------------------")
#print('Field names are: ' + ', '.join(field for field in fields))
#print("----------------------------")

print("Financial Analysis")
print("----------------------------")
print("Total Months: {}".format(num_months))
print("Total: ${}".format(total_pl))
print("Average Change: ${}".format(avg_change))
print("Greatest Increase in Profits: {} (${})".format(greatest_inc_month, greatest_inc))
print("Greatest Decrease in Profits: {} (${})".format(greatest_dec_month, greatest_dec))


with open(text_file, "w") as textfile:
    print("Financial Analysis", file=textfile)
    print("----------------------------", file=textfile)
    print("Total Months: {}".format(num_months), file=textfile)
    print("Total: ${}".format(total_pl), file=textfile)
    print("Average Change: ${}".format(avg_change), file=textfile)
    print("Greatest Increase in Profits: {} (${})".format(greatest_inc_month, greatest_inc), file=textfile)
    print("Greatest Decrease in Profits: {} (${})".format(greatest_dec_month, greatest_dec), file=textfile)

