#! /usr/bin/env python3
from tkinter import *
import tkinter as tk 

global count
def calculate():
     hours = float(employeeHours.get())
     rate = float(employeeRate.get())   
     taxes = 0.85
     salary = rate * hours * taxes
     salary2 = salary
     if count == 0:
          results = Label(root, text = "Week's Pay: $%.2f" % salary).grid(row=7, column=1)
     else:
          salary2, salary = salary, salary2
          results = Label(root, text = "Week's Pay: $%.2f" % salary2).grid(row=7, column=1)
          results = Label(root, text = "Last Week's Pay: $%.2f" % salary).grid(row=7, column=1)
     return          

          
if __name__ == '__main__':
     count = 0
     root = tk.Tk()
     root.geometry('450x200')
     root.title('Payroll Calculator')
     
     employeeID = tk.StringVar(root)
     employeeName = tk.StringVar(root)
     employeeHours = tk.StringVar(root)
     employeeRate = tk.StringVar(root)
     
     label1 = Label(root, text = "Welcome to the Payroll Calculator", fg='black').grid(row=0,column=0)  
     
     label2 = Label(root, text = "EmployeeID: ", fg='red').grid(row=1,column=0)
     label3 = Label(root, text = "Employee: ", fg='red').grid(row=2,column=0)
     label4 = Label(root, text = "Enter Hourly Rate: ", fg='red').grid(row=3,column=0)
     label5 = Label(root, text = "Weekly Hours: ", fg='red').grid(row=4,column=0)
      
     myID = Entry(root, textvariable=employeeID).grid(row=1, column=1)
     myName = Entry(root, textvariable=employeeName).grid(row=2, column=1)
     myHours = Entry(root, textvariable=employeeHours).grid(row=4, column=1)
     myRate = Entry(root, textvariable=employeeRate).grid(row=3, column=1)
     
     button1 = Button(root, text="Calculate",command = calculate)
     button1.grid(row=6, column=0)
     
     root.mainloop()
               

