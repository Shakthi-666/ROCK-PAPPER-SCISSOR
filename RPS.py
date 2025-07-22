import tkinter as tk
import random

# Initialize scores
player_score = 0
computer_score = 0

# Main Game Logic
def play(user_choice):
    global player_score, computer_score
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)

    user_choice_label.config(text=f"You chose: {user_choice}")
    comp_choice_label.config(text=f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        result_label.config(text="Result: It's a Tie!", fg="blue")
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result_label.config(text="Result: You Win! 🎉", fg="green")
        player_score += 1
    else:
        result_label.config(text="Result: You Lose! ❌", fg="red")
        computer_score += 1

    update_score()

# Reset the game
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    user_choice_label.config(text="You chose: ")
    comp_choice_label.config(text="Computer chose: ")
    result_label.config(text="Result: ", fg="black")
    update_score()

# Update score display
def update_score():
    score_label.config(text=f"Score - You: {player_score}  |  Computer: {computer_score}")

# Tkinter Window Setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)

# Labels
tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16, "bold")).pack(pady=10)
user_choice_label = tk.Label(root, text="You chose: ", font=("Arial", 12))
user_choice_label.pack()
comp_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_choice_label.pack()
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text="Score - You: 0  |  Computer: 0", font=("Arial", 12, "bold"))
score_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Reset Button
tk.Button(root, text="Reset Game", width=20, command=reset_game, bg="#f44336", fg="white").pack(pady=20)

# Run the App
root.mainloop()
