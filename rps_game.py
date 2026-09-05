import tkinter as tk
import random

# Initialize scores
player_score = 0
computer_score = 0

def play(choice):
    global player_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    result = ""
    if choice == computer_choice:
        result = "It's a tie!"
    elif (choice == "Rock" and computer_choice == "Scissors") or \
         (choice == "Paper" and computer_choice == "Rock") or \
         (choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Player: {player_score}  Computer: {computer_score}")

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Buttons
tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack()
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack()
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack()

# Labels for results and scores
result_label = tk.Label(root, text="Make your move!")
result_label.pack()
score_label = tk.Label(root, text="Player: 0  Computer: 0")
score_label.pack()

root.mainloop()
