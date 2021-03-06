#import the os module and csv Module for reading CSV files
import os 
import csv

#function for analyzing the csv_file
def data_analysis(csv_path):
    #csv_path=os.path.join("Resources",csv_file)
    with open(csv_path) as file:
        csv_reader=csv.reader(file,delimiter=",")
        # Read the header row first
        csv_header = next(csv_reader)
        candidates_list=[]
        candidates_poll=[]
        
        #looping through all rows
        for row in csv_reader:
            candidates_poll.append(row[2])
            if not row[2] in candidates_list:
                candidates_list.append(row[2])
        
        
    Total_Votes= len(candidates_poll)      
    candidates_percent=[candidates_poll.count(candidate)/Total_Votes for candidate in candidates_list ]     
    candidates_count=[candidates_poll.count(candidate) for candidate in candidates_list ]     
    winner = list({k: v for k, v in zip(candidates_list, candidates_count) if v==max(candidates_count)}.keys())[0]
    return candidates_list,Total_Votes,candidates_percent,candidates_count,winner


#function for writing the analysis result in txt_file
def text_writer(csv_input,txt_output):
    # Set path for file
    input_path=os.path.join("Resources",csv_input)
    output_path = os.path.join( "Analysis", txt_output)
    candidates_list,Total_Votes,candidates_percent,candidates_count,winner=data_analysis(input_path)
    #for writing in txt_file
    f= open(output_path,"w+")
    f.write("Election Results\n")
    f.write("-"*40+"\n")
    f.write(f"Total Votes:{Total_Votes}\n")
    f.write("-"*40+"\n")
    for i in range(len(candidates_list)):
        f.write(("{}" + ": "+ "{:.3%} " +"("+"{}"+")").format(candidates_list[i],candidates_percent[i],candidates_count[i]))
        f.write("\n")
    f.write("-"*40+"\n")
    f.write(f"Winner: {winner}\n")
    f.write("-"*40+"\n")
    f.close()

    #for printing in terminal
    print("-"*40+"\n")
    print("Election Results\n")
    print("-"*40+"\n")
    print(f"Total Votes:{Total_Votes}\n")
    print("-"*40+"\n")
    for i in range(len(candidates_list)):
        print(("{}" + ": "+ "{:.3%} " +"("+"{}"+")").format(candidates_list[i],candidates_percent[i],candidates_count[i]))
        print("\n")
    print("-"*40+"\n")
    print(f"Winner: {winner}\n")
    print("-"*40+"\n")
   


text_writer("election_data.csv","output.txt")
