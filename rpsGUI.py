import random
import tkinter as tk

class RPS:
    def __init__(self ,root):
        self.root=root
        self.root.title("Rock Paper Scissor")
        
        self.label=tk.Label(root,text="Choose Rock,Paper, or Scissor",font=("Arial",12))
        self.label.pack(pady=10)
        
        self.result_label=tk.Label(root,text="",font=("Arial",14,"bold"))
        self.result_label.pack()
        
        self.option={1:"Rock",2:"Paper",3:"Scissor"}
        
        for choice in self.option.values():
            button=tk.Button(root,text=choice,font=("Arial",12),command=lambda c=choice: self.play(c))
            button.pack(pady=5)
    def play(self,Player_choice):
        computer_choice=random.choice(list(self.option.values()))
        result=self.get_winner(Player_choice,computer_choice)
        self.result_label.config(text=f"You: {Player_choice} | computer:{computer_choice}\n{result}")
        
    def get_winner(self,Player,Computer):
        if Player == Computer:
                return "Its a tie"
        elif (Player == "Rock" and Computer == "Scissor") or \
             (Player == "Paper" and Computer == "Rock") or\
             (Player == "Scissor" and Computer == "Paper"):
            return "You Win1"
        else:
            return "Computer Wins!"
            
        
        
        
if __name__=="__main__":
    root=tk.Tk()
    game=RPS(root)
    root.mainloop()
    
        
