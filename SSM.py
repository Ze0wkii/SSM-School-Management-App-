import time
import random as r
import pyautogui
import tkinter as tk
from tkinter import filedialog

class SchlManagement:
    def __init__(self):
        time.sleep(0.5)
        print("Welcome to Eight Inner Gates Academy Portal!")

        self.registry = {
            "NameT1": "Vivek Singh",
            "Profession": "Teacher",
            "CodeT1": 123,
            "NameT2": "Vedant Garje ",
            "Profession": "Teacher",
            "CodeT2": 124,
            "NameS1": "Atharva Khade",
            "Profession": "Student",
            "CodeS1": 126,
            "NameS2": "Prathamesh Garje",
            "Profession": "Student",
            "CodeS2": 112,
        }

        self.quoteT = [
            "You Look Amazing Today!",
            "You Will be doomed soon.",
            "Hey, What brings you here today?",
            "Roses are red, Violets are blue, please do your work, If you can"

        ]

        self.quoteS = [
            "Hey, you look intelligent today😉"
            "Please pay your remaining dues as soon as possible.",
            "What brings you here today?",
            "Heyyy, Tomorrow wil be final exams be prepared:)"
        ]

        self.guii = [
            "Type 1 to access profile of students",
            "Type 2 to upload your notes",
            "Type 3 to check your students attendence",
            "Type 4 to upload circulars"
        ]

        self.guiS = [
            "Type 1 to check your financial summary",
            "Type 2 to check your assignments",
            "Type 3 to check your circulars",
            "Type 4 to check your result"
        ]

        self.studentsp = {
            "Name1": "Vedant Garje",
            "Profession1": "Student",
            "Fees1": "Not Paid",
            "Religion1": "Hindu",
            "Attendence1": "60%",

            "Name2": "Prathamesh GarjeS",
            "Profession2": "Student",
            "Fees2": "Paid",
            "Religion2": "Hindu",
            "Attendence2": "65%"
        }



    '''NOT WORKING'''
    # def save_file(self):
    #     """Opens a standard save as dialog for the user to save their file."""
    #     filename = filedialog.asksaveasfilename()
    #     save_button = tk.Button(self.window, text="Save", command=self.save_file)
    #     save_button.pack()

    def gui(self):

        if self.in2 == 'T':
            print(r.choice(self.quoteT))
            for i in self.guii:
                time.sleep(0.5)
                print(i)
            in4 = input(":")
            in4 = int(in4)
            if in4 == 1:
                    print(self.studentsp.items())
            
            elif in4 == 2:
                pass

            elif in4 == 3:
                print(self.studentsp['A'])
 

            
                
        elif self.in2 == 'S':
            print(r.choice(self.quoteS))

        

    def login(self):
        self.in2 = input("Teacher Or Student? (T/S): ").upper()
        time.sleep(0.5)
        self.in1 = input("Your Name: ")
        time.sleep(0.5)


        if self.in2 == "T":
            if self.in1 in ["Vivek Singh", "Vedant Garje"]:
                in3 = int(input("Code Please: "))
                if (self.in1 == "Vivek Singh" and in3 == 123) or (
                   self.in1 == "Vedant Garje" and in3 == 1245
                ):
                    print(f"Welcome To Eight Inner Gates Academy {self.in1}!")
                    self.gui()

                else:
                    print("Error: Incorrect code.")
            else:
                print("Error: Invalid name or profession.")

        elif self.in2 == "S":
            if self.in1 in ["Atharva Khade", "Prathamesh Garje"]:
                in3 = int(input("Code Please: "))
                if (self.in1 == "Atharva Khade" and in3 == 1269) or (
                    self.in1 == "Prathamesh Garje" and in3 == 112
                ):
                    print(f"Welcome {self.in1}!")
                    self.gui()
                else:
                    print("Error: Incorrect code.")
            else:
                print("Error: Invalid name or profession.")

        else:
            print("Error: Invalid input. Please enter 'T' or 'S'.")

    
        time.sleep(0.5)


schl = SchlManagement()
schl.login()
