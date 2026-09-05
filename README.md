# Rock Paper Scissors Game with GUI

A simple Python game where you play Rock Paper Scissors against the computer using a graphical user interface (GUI) with real-time score tracking.

## Authors
Khin Moe Moe Latt (2025. 6. 20.)

## Synopsis
This project is an interactive Rock Paper Scissors game implemented in Python with a GUI using Tkinter. The user selects their move by clicking a button (Rock, Paper, or Scissors). The computer randomly selects its move, and the result is displayed along with updated scores for both the player and the computer. The interface is simple and user-friendly, making the game accessible and fun for all ages.

## How to Install
* Requires Python 3.x (no additional modules needed for basic Tkinter)
* To check if Tkinter is installed, run:

python -m tkinter
* If you see a window pop up, Tkinter is available. If not, install Python with Tkinter support.

## How to Use
* Works on any OS with Python 3.x (e.g., Windows 11, macOS, Linux)
* Save the source code as `rps_game.py` in your project folder.
* Open a terminal or command prompt in your project folder and run:

python rps_gui.py
* Click the "Rock", "Paper", or "Scissors" button to play. The computer's choice and the round result will appear, and scores will update automatically.

## Example Code Snippet
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

## Example Execution

When you run the program, a window appears with three buttons:
- Click "Rock", "Paper", or "Scissors".
- The computer's choice and the result (win/lose/tie) are shown.
- The current score is displayed and updates after each round.

Sample output in the GUI:
Computer chose: Scissors
You win!
Player: 1 Computer: 0


## License
This project is licensed under the MIT License.
