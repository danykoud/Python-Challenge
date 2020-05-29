import os
import csv

Total_Vote=0
t_frist=0
t_second= 0
t_third= 0
t_fourth= 0
Winner_result = 0
list_candidate = []


# set the path for csv file

election_data_path= os.path.join("_ファイル","Homework","03-Python","Instructions","PyPoll","Resources","election_data.csv")

# open and read the CSV file 
with open(election_data_path, 'r') as election_file:
    election_read= csv.reader(election_file, delimiter=',')

    Header=next(election_read)

# create a function that calculates the percentage of votes for each candidate 
    def percentage_votes(candidate_vote,Total_Vote):
        return((candidate_vote / Total_Vote) * 100 )  
    
#Looping through the csv file 
# calculation of the total number of votes and the total number of votes per candidate
    for row in election_read:
        Total_Vote +=1
                
        if row[2] not in list_candidate:
            list_candidate.append(row[2])
        
        elif row[2]== list_candidate[0] :
            t_frist+=1
            Khan_vote= t_frist
        elif row[2]== list_candidate[1] :
            t_second+=1
            Correy_vote= t_second 
        
        elif row[2]== list_candidate[2] :
            t_third+=1
            Li_vote= t_third
           
        
        elif row[2]== list_candidate[3] :
            t_fourth+=1
            O_Tooley_vote= t_fourth

# Use of the function(Line 18) to find the percentage of votes for each candidate         
Khan_percentage_vote= round(percentage_votes(Khan_vote,Total_Vote))         
Correy_percentage_vote= round(percentage_votes(Correy_vote,Total_Vote))          
Li_percentage_vote= round(percentage_votes(Li_vote,Total_Vote))          
O_Tooley_percentage_vote= round(percentage_votes(O_Tooley_vote,Total_Vote))         

# Create a list for candidate's total number of vote 
# combine candidate's total number of vote with condidates' name
List_sum=[Khan_vote,Correy_vote, Li_vote, O_Tooley_vote]
Summary_View= zip(List_sum,list_candidate)     

# Looping through the combined list (toople) 
# retrieve the winner
for info in Summary_View:
    if int(info[0]) > Winner_result :
        Winner_result= int(info[0])
        Winner= info[1]

print("Election Results")
print("-------------------------------")
print(f"{ list_candidate[0]}: {Khan_percentage_vote:.3f}%  ({Khan_vote}) ") 
print("--------------------------------")
print(f"{ list_candidate[1]}: {Correy_percentage_vote:.3f}%  ({Correy_vote}) ")               
print(f"{ list_candidate[2]}: {Li_percentage_vote:.3f}%  ({Li_vote}) ")                
print(f"{ list_candidate[3]}: {O_Tooley_percentage_vote:.3f}%  ({O_Tooley_vote}) ")
print("---------------------------------") 
print(f"Winner : {Winner}")
print("---------------------------------")

text_path= os.path.join("PyPoll","Result_script_02.txt")

with open(text_path, "w") as file_txt:

    file_txt.write ("Election Results \n")
    file_txt.write("-------------------------------\n")
    file_txt.write(f"{ list_candidate[0]}: {Khan_percentage_vote:.3f}%  ({Khan_vote}) \n") 
    file_txt.write("--------------------------------\n")
    file_txt.write(f"{ list_candidate[1]}: {Correy_percentage_vote:.3f}%  ({Correy_vote})\n ")               
    file_txt.write(f"{ list_candidate[2]}: {Li_percentage_vote:.3f}%  ({Li_vote}) \n")                
    file_txt.write(f"{ list_candidate[3]}: {O_Tooley_percentage_vote:.3f}%  ({O_Tooley_vote}) \n")
    file_txt.write("---------------------------------\n") 
    file_txt.write(f"Winner : {Winner} \n")
    file_txt.write("---------------------------------\n")

