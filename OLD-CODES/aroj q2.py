# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 01:07:33 2020

@author: farhan
"""

def numberOfDays(month, year):
    daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month > len(daysInMonths) or year < 0 or month < 0:
        return "Please enter a valid month/year"

    return daysInMonths[month-1] + int((year % 4) == 0 and month == 2)
def main():
   year = int(input("Enter a year: "))
   month = int(input("Enter a month in terms of a number: "))
   if month == 1:
        month = 'January'
   
   print("There are" ,  numberOfDays(month, year) , "days in" , month, "of" , year )

if __name__ == '__main__': 
   main()
