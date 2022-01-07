import os 
import csv
def data_analysis(csv_path):
    with open(csv_path) as csv_file:
        csv_reader=csv.reader(csv_file,delimiter=",")
        csv_header = next(csv_reader)
        profit_loss=[]
        Date_=[]
    
        for row in csv_reader:
            profit_loss.append(row[1])
            Date_.append(row[0])
    Total_Months=len(Date_)
    profit_loss=[int(i) for i in profit_loss]
    Total=sum(profit_loss)
    Changes=[profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]
    Average_Change= sum(Changes)/len(Changes)
    Greatest_Increase_amount= max(Changes)
    Greatest_Increase_Date= Date_[Changes.index(max(Changes))+1]
    Greatest_Decrease_amount= min(Changes)
    Greatest_Decrease_date= Date_[Changes.index(min(Changes))+1]
    return Total_Months,Total,Average_Change,Greatest_Increase_amount,\
         Greatest_Increase_Date,Greatest_Decrease_amount,Greatest_Decrease_date   

def text_writer(csv_input,txt_output):
    input_path=os.path.join("Resources",csv_input)
    output_path = os.path.join( "Analysis", txt_output)
    Total_Months,Total,Average_Change,Greatest_Increase_amount,\
    Greatest_Increase_Date,Greatest_Decrease_amount,Greatest_Decrease_date=\
    data_analysis(input_path)
    f= open(output_path,"w+")
    f.write("-"*60+"\n")
    f.write("Financial Analysis\n")
    f.write("-"*60+"\n")
    f.write(f"Total Months: {Total_Months}\n")
    f.write(f"Total: ${Total}\n")
    f.write(f"Average  Change: ${round(Average_Change,2)}\n")
    f.write(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase_amount})\n")
    f.write(f"Greatest Decrease in Profits: {Greatest_Decrease_date} (${Greatest_Decrease_amount})\n")
    f.write("-"*60+"\n")
    f.close()

text_writer("budget_data.csv","output.txt")