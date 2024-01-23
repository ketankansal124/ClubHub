import tkinter as tk
from tkinter import messagebox

# Define the quiz questions and answers
questions = [
    "Question 1: What is the capital of France?",
    "Question 2: Who painted the Mona Lisa?",
    "Question 3: Which planet is known as the Red Planet?",
    # Add more questions here...
]

answers = [
    "Paris",
    "Leonardo da Vinci",
    "Mars",
    # Add more answers here...
]

# Create the quiz window
window = tk.Tk()
window.title("Quiz")
window.geometry("400x300")

# Variables to keep track of the score and current question
score = 0
current_question = 0

# Function to check the answer and move to the next question
def check_answer():
    global score, current_question
    answer = entry.get().strip()
    if answer.lower() == answers[current_question].lower():
        score += 1
    entry.delete(0, tk.END)
    current_question += 1
    if current_question < len(questions):
        label.config(text=questions[current_question])
    else:
        messagebox.showinfo("Quiz Complete", f"Your score: {score}/{len(questions)}")
        window.destroy()

# Function to start the quiz and collect user information
def start_quiz():
    global score, current_question

    name = name_entry.get().strip()
    roll_no = roll_no_entry.get().strip()

    # Store user information and score
    user_info = f"Name: {name}\nRoll No: {roll_no}\n"
    score_info = f"Score: {score}/{len(questions)}\n"
    with open("quiz_results.txt", "a") as file:
        file.write(user_info)
        file.write(score_info)
        file.write("------------------------------\n")

    # Reset score and current question
    score = 0
    current_question = 0

    # Start the quiz
    name_frame.destroy()
    label.config(text=questions[current_question])
    entry.pack(pady=10)
    button.config(text="Submit", command=check_answer)

# Create and place the name input elements
name_frame = tk.Frame(window)
name_frame.pack(pady=20)

name_label = tk.Label(name_frame, text="Name:", font=("Arial", 12))
name_label.grid(row=0, column=0)

name_entry = tk.Entry(name_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1)

roll_no_label = tk.Label(name_frame, text="Roll No:", font=("Arial", 12))
roll_no_label.grid(row=1, column=0)

roll_no_entry = tk.Entry(name_frame, font=("Arial", 12))
roll_no_entry.grid(row=1, column=1)

start_button = tk.Button(window, text="Start Quiz", command=start_quiz)
start_button.pack(pady=10)

# Create and place the quiz elements
label = tk.Label(window, text="", font=("Arial", 12))
entry = tk.Entry(window, font=("Arial", 12))
button = tk.Button(window, text="", command=None)

# Run the quiz
window.mainloop()
