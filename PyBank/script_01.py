import os
import csv


Total_Months=0
Total_PL = 0
PL_change=[]
change_month= []
Greatest= 0
Lowest= 0

budget_data_path= os.path.join("PyBank","Resources","budget_data.csv")
with open(budget_data_path, 'r') as budget_file:
    file_read= csv.reader(budget_file, delimiter=',')

    Header=next(file_read)
    row=next(file_read)
    previous_PL= int(row[1])
    def Average_Change (PL_change):
        return(sum(PL_change)/len(PL_change))
    def change_PL(current_PL, previous_PL):
        return( current_PL - previous_PL)
 
    for row in file_read:
        
        
        
        Total_Months +=1
        Total_PL += int(row[1])
        current_PL= int(row[1])
        PL_change.append(change_PL(current_PL,previous_PL))
        previous_PL= current_PL
# Getting the starting Date of the the Greatest Increase and Decrease  of Profit
        if int(row[1]) > Greatest:
                Greatest = int(row[1])
                Greatest_Date = row[0]
        if int(row[1]) < Lowest:
                Lowest = int(row[1])
                Lowest_Date = row[0]

Greatest_Increase_Profits=  max(PL_change)
Greatest_Decrease_Profits= min(PL_change)
Average_Change_PL= Average_Change(PL_change)


print( "Financial Analysis")
print("-----------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_PL}")
print(f"Average  Change: ${Average_Change_PL:.2f}")
print(f"Greatest Increase in Profits: {Greatest_Date} (${Greatest_Increase_Profits})")
print(f" Greatest Decrease in Profits: {Lowest_Date } (${Greatest_Decrease_Profits}) ")


Text_path= os.path.join("PyBank","Result_script_01.txt")

with open(Text_path, "w") as Text_file:
   
    Text_file.write("Financial Analysis \n")
    Text_file.write("----------------------\n")
    Text_file.write(f"Total Months: {Total_Months} \n")
    Text_file.write(f"Total: ${Total_PL} \n")
    Text_file.write(f"Average  Change: ${Average_Change_PL:.2f} \n")
    Text_file.write(f"Greatest Increase in Profits: {Greatest_Date} (${Greatest_Increase_Profits}) \n")
    Text_file.write(f" Greatest Decrease in Profits: {Lowest_Date } (${Greatest_Decrease_Profits}) \n ")