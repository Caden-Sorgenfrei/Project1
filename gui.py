from tkinter import *
import csv

class Gui:
    
    #Varaibles so that names can be changed easily
    canidate_one = "Chen"
    canidate_two = "Nguyen"
    canidate_three = "Peng"
    canidate_four = "Detloff"
        
    def __init__(self, window):
        self.window = window
        
        #Voter Check
        self.frame_voter = Frame(self.window)
        self.label_voter = Label(self.frame_voter, text='Voter ID\t')
        self.entry_voter = Entry(self.frame_voter, width=40)
        self.label_voter.pack(padx=20, side='left')
        self.entry_voter.pack(padx=20, side='left')
        self.frame_voter.pack(anchor='w', pady=10)

        # Radio buttons for Canidates
        self.frame_canidate = Frame(self.window)
        self.label_operation = Label(self.frame_canidate, text='Canidates\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_name1 = Radiobutton(self.frame_canidate, text = Gui.canidate_one, variable=self.radio_1, value=1, command=self.canidate)
        self.radio_name2 = Radiobutton(self.frame_canidate, text = Gui.canidate_two, variable=self.radio_1, value=2, command=self.canidate)
        self.radio_name3 = Radiobutton(self.frame_canidate, text = Gui.canidate_three, variable=self.radio_1, value=3, command=self.canidate)
        self.radio_name4 = Radiobutton(self.frame_canidate, text = Gui.canidate_four, variable=self.radio_1, value=4, command=self.canidate)
        self.label_operation.pack(side='left', padx=5)
        self.radio_name1.pack(side='left')
        self.radio_name2.pack(side='left')
        self.radio_name3.pack(side='left')
        self.radio_name4.pack(side='left')
        self.frame_canidate.pack(anchor='w', pady=10)
    
        #Button Box
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()
        
        #Submission Button
        self.frame_button1 = Frame(self.window)
        self.button_compute = Button(self.frame_button1, text='SUBMIT', command=self.vote)
        self.button_compute.pack(padx=10)
        self.frame_button1.pack()
               
    
    """_Asks if the voter it sure about their selection_"""
    def canidate(self):
        canidate = self.radio_1.get()
        
        if canidate == 1:
            self.label_result.config(text=f'Are you sure you want to vote for {Gui.canidate_one}', fg='green')
        elif canidate == 2:
            self.label_result.config(text=f'Are you sure you want to vote for {Gui.canidate_two}', fg='green')
        elif canidate == 3:
            self.label_result.config(text=f'Are you sure you want to vote for {Gui.canidate_three}', fg='green')
        elif canidate == 4:
            self.label_result.config(text=f'Are you sure you want to vote for {Gui.canidate_four}', fg='green')
            
            
    """_Processes the vote and does everything_"""
    def vote(self):
        vote = self.radio_1.get()
        voter_ID = self.entry_voter.get()

        try:
            (type(float(voter_ID)))
            
            with open('votes.csv') as myfile:
        
            
                if(len(voter_ID.strip()) != 8):
                    self.label_result.config(text=f'Please Enter an 8 digit voter ID', fg='red')
                elif(vote == 0):
                    self.label_result.config(text=f'Please select someone to vote for', fg='red')
                elif voter_ID in myfile.read():
                    self.label_result.config(text=f'Voter ID has already been used', fg='red')
                
                else:
                    if vote == 1:
                        with open('votes.csv', 'a', newline="") as output_csv_file:
                            data = csv.writer(output_csv_file)
                            data.writerow([voter_ID, Gui.canidate_one])
                        self.label_result.config(text=f'Your vote has been proccessed', fg='blue')
                        #self.entry_voter.delete("1.0", "end")
                        self.radio_1.set(0)
                    elif vote == 2:
                        with open('votes.csv', 'a', newline="") as output_csv_file:
                            data = csv.writer(output_csv_file)
                            data.writerow([voter_ID, Gui.canidate_two])
                        self.label_result.config(text=f'Your vote has been proccessed', fg='blue')
                        #self.entry_voter.delete("1.0", "end")
                        self.radio_1.set(0)
                    elif vote == 3:
                        with open('votes.csv', 'a', newline="") as output_csv_file:
                            data = csv.writer(output_csv_file)
                            data.writerow([voter_ID, Gui.canidate_three])
                        self.label_result.config(text=f'Your vote has been proccessed', fg='blue')
                        #self.entry_voter.delete("1.0", "end")
                        self.radio_1.set(0)
                    elif vote == 4:
                        with open('votes.csv', 'a', newline="") as output_csv_file:
                            data = csv.writer(output_csv_file)
                            data.writerow([voter_ID, Gui.canidate_four])
                        self.label_result.config(text=f'Your vote has been proccessed', fg='blue')
                        #self.entry_voter.delete("1.0", "end")
                        self.radio_1.set(0)
        except ValueError:
            self.label_result.config(text=f'Your voter ID must be numerical', fg='red')