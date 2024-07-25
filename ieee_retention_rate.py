'''does not work'''

import csv

def get_members(retention_year):
    previous_year_of_retention=retention_year-1
    with open('ieee_retention.csv', 'r') as file:
        csv_reader = csv.reader(file)
        # skip header row
        next(csv_reader)
        ms=0
        me=0
        for row in csv_reader:
            if((row[2])==str(previous_year_of_retention)):
                ms+=1
            if((row[2])==str(retention_year)):
                me+=1
        print(f"Members at the start of the year {previous_year_of_retention}: {ms}")
        print(f"Members at the end of the year {retention_year}: {me}")
        mn=int(input("Enter how many members were acquired during the time period: "))
        retention_rate=((me-mn)/ms)*100
        print(f"Retention Rate for the year {retention_year}: {retention_rate}")

if __name__=='__main__':
    retention_time_period=int(input("Enter the year you want to get the retention for: "))
    
    get_members(retention_year=retention_time_period)