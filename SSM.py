import time
import random as r
import tkinter as t
import pygame
import json


class SchlManagement:
    def __init__(self):
        time.sleep(0.5)
        print("Welcome to ze0wkii.education Portal!")
        self.login()

        



    def playSong(self):
        """
        Plays the song 'Verified.mp3' using pygame
        """
        pygame.init()

        song = 'Verified.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        while True:
            """
            Waits for the song to finish playing
            """
            time.sleep(0.1)
            if not pygame.mixer.music.get_busy():
                """
                Breaks out of the loop when the song finishes playing
                """
                break

    def login(self):
        """
        This function is responsible for handling the login of teachers and students.
        It takes input from the user for name and profession and verifies it with the stored data.
        If the input is correct it generates a welcome message and calls the GUI function.
        """
        self.in2 = input("Teacher Or Student? (T/S): ").upper()
        time.sleep(0.5)
        self.in1 = input("Your Name: ")
        time.sleep(0.5)


        if self.in2 == "T":
            # If the input is for a teacher check if the name and code are correct
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
            # If the input is for a student check if the name and code are correct
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

    def save(self):
        with open("data.json", "w") as f:
            json.dump(self.registry, f, indent=4)


    
    def write(self, x, y):
        """
        Writes the given name, profession, code, fees and standard to the registry.

        Parameters
        ----------
        x : str
            The name of the student.
        y : int
            The standard of the student.
        """
        name = x
        profession = "Student"
        code = r.randint(100, 1000)
        fees = "Not Paid"
        std = y
        self.registry["NameS" + str(len(self.registry) // 5)] = name
        self.registry["Profession"] = profession
        self.registry["CodeS" + str(len(self.registry) // 5)] = code
        self.registry["FeesS" + str(len(self.registry) // 5)] = fees
        self.registry["StdS" + str(len(self.registry) // 5)] = std
        # Print a confirmation message
        print(
            f"{name} added to the records with code: {code}, fees: {fees}, class: {std}"
        )



    def gui(self):
        """
        GUI function is the main function of the program. It is called
        when the program starts. This function is responsible for providing
        the user with a menu and then based on the choice given by the user,
        it performs the required action.
        """
        self.registry = {
            "NameT1": "Vivek Singh",
            "Profession": "Teacher",
            "CodeT1": 123,
            "NameT2": "Vedant Garje ",
            "Profession": "Teacher",
            "CodeT2": 124,  # IMPORTANT VARIABLES
            "NameS1": "Atharva Khade",
            "Profession": "Student",
            "CodeS1": 126,
            "NameS2": "Prathamesh Garje",
            "Profession": "Student",
            "CodeS2": 112,
        }

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

        self.quoteT = [
            "You Look Amazing Today!",
            "You Will be doomed soon.",
            "Hey, What brings you here today?",
            "Roses are red, Violets are blue, please do your work, If you can"

        ]

        self.quoteS = [
            "Hey, you look intelligent today😉",
            "Please pay your remaining dues as soon as possible.",
            "What brings you here today?",
            "Heyyy, Tomorrow wil be final exams be prepared:)"
        ]

        self.guii = [
            "Type 1 to access profile of students",
            "Type 2 to register a new student",
            "Type 3 to upload circulars",
            "Type 4 to mark the attendence of students"
        ]

        self.guiS = [
            "Type 1 to check your financial summary",
            "Type 2 to check your assignments",
            "Type 3 to check your circulars",
            "Type 4 to check your result"
        ]

        if self.in2 == 'T':  # Checking if his teacher or a student to give him quotes according to them.
            print(r.choice(self.quoteT))

            for i in self.guii:
                time.sleep(0.5)
                print(i)

            in4 = input(":")
            in4 = int(in4)

            if in4 == 1:  # It prints the students profile 
                print(self.studentsp.items())

            elif in4 == 2:
                self.ver0 = input("Please type the code asked you before: ")
                self.ver0 = int(self.ver0)

                if self.ver0 == self.registry['CodeT1'] or self.ver0 == self.registry['CodeT2']:
                    time.sleep(0.5)
                    print("Verified!")

                    self.ver1 = input("Enter the name of the student: ")
                    time.sleep(0.5)
                    self.ver2 = input("Enter the current class of the student: ")
                    print("Please wait...")
                    time.sleep(0.5)
                    self.write(self.ver1, self.ver2)
                    self.save()
                    self.playSong()


                else:
                    print("Code Rejected")

            elif in4 == 3:
                print(self.studentsp['A'])
 

            
                
        elif self.in2 == 'S':
            print(r.choice(self.quoteS))

        



schl = SchlManagement()
# schl.login()

