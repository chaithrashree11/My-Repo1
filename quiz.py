
import tkinter as tk
from tkinter import messagebox

# =================================
# 1. CREATE MAIN APPLICATION WINDOW
# =================================

root = tk.Tk()
root.title("Python Quiz Application")
root.geometry("650x520")
root.configure(bg="#EAF2F8")
root.resizable(False, False)

# =================================
# 2. QUIZ QUESTIONS
# =================================

questions = [
    {
        "question": "Which language is used for AI?",
        "options": ["HTML", "Python", "CSS", "SQL"],
        "answer": "Python"
    },
    {
        "question": "What is the extension of Python files?",
        "options": [".html", ".java", ".py", ".cpp"],
        "answer": ".py"
    },
    {
        "question": "Which function displays output?",
        "options": ["input()", "print()", "type()", "int()"],
        "answer": "print()"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["int", "str", "float", "bool"],
        "answer": "bool"
    },
    {
        "question": "Which symbol is used for comments?",
        "options": ["#", "@", "$", "&"],
        "answer": "#"
    }
]

# =================================
# 3. GLOBAL VARIABLES
# =================================

current_question = 0
score = 0
student_name = ""

selected_answer = tk.StringVar(master=root)

# =================================
# 4. MAIN HEADING
# =================================

title = tk.Label(
    root,
    text="PYTHON QUIZ APPLICATION",
    font=("Arial", 22, "bold"),
    bg="#EAF2F8",
    fg="#154360"
)
title.pack(pady=20)

# =================================
# 5. MAIN CONTENT FRAME
# =================================

content = tk.Frame(
    root,
    bg="white",
    padx=25,
    pady=20
)
content.pack(padx=30, pady=10, fill="both", expand=True)

# =================================
# 6. WELCOME SCREEN
# =================================

welcome_frame = tk.Frame(content, bg="white")
welcome_frame.pack(fill="both", expand=True)

welcome_label = tk.Label(
    welcome_frame,
    text="Welcome to the Quiz!",
    font=("Arial", 21, "bold"),
    bg="white",
    fg="#2874A6"
)
welcome_label.pack(pady=25)

description = tk.Label(
    welcome_frame,
    text="Test your Python knowledge!\nAnswer all questions and check your score.",
    font=("Arial", 13),
    bg="white"
)
description.pack(pady=10)

name_label = tk.Label(
    welcome_frame,
    text="Enter Your Name:",
    font=("Arial", 12, "bold"),
    bg="white"
)
name_label.pack(pady=10)

name_entry = tk.Entry(
    welcome_frame,
    font=("Arial", 13),
    width=25,
    justify="center"
)
name_entry.pack(pady=5)

# =================================
# 7. QUIZ SCREEN
# =================================

quiz_frame = tk.Frame(content, bg="white")

progress_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#2874A6"
)
progress_label.pack(pady=15)

question_label = tk.Label(
    quiz_frame,
    text="",
    font=("Arial", 16, "bold"),
    bg="white",
    wraplength=520
)
question_label.pack(pady=20)

answer_buttons = []

for i in range(4):
    button = tk.Radiobutton(
        quiz_frame,
        text="",
        variable=selected_answer,
        value="",
        font=("Arial", 13),
        bg="white",
        activebackground="white",
        anchor="w"
    )
    button.pack(fill="x", padx=80, pady=6)
    answer_buttons.append(button)

# =================================
# 8. SHOW QUESTION FUNCTION
# =================================

def show_question():

    selected_answer.set("")

    q = questions[current_question]

    progress_label.config(
        text=f"Question {current_question + 1} of {len(questions)}"
    )

    question_label.config(
        text=q["question"]
    )

    for i, option in enumerate(q["options"]):

        answer_buttons[i].config(
            text=option,
            value=option
        )

    if current_question == len(questions) - 1:
        next_button.config(text="Submit Quiz")
    else:
        next_button.config(text="Next Question")

# =================================
# 9. START QUIZ FUNCTION
# =================================

def start_quiz():

    global student_name

    student_name = name_entry.get().strip()

    if student_name == "":
        messagebox.showwarning(
            "Warning",
            "Please enter your name!"
        )
        return

    welcome_frame.pack_forget()
    quiz_frame.pack(fill="both", expand=True)

    show_question()

# =================================
# 10. NEXT QUESTION FUNCTION
# =================================

def next_question():

    global current_question, score

    if selected_answer.get() == "":
        messagebox.showwarning(
            "Warning",
            "Please select an answer!"
        )
        return

    if selected_answer.get() == questions[current_question]["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        show_result()

# =================================
# 11. RESULT SCREEN
# =================================

result_frame = tk.Frame(content, bg="white")

result_title = tk.Label(
    result_frame,
    text="QUIZ COMPLETED!",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="#2874A6"
)
result_title.pack(pady=25)

result_label = tk.Label(
    result_frame,
    text="",
    font=("Arial", 17, "bold"),
    bg="white"
)
result_label.pack(pady=15)

grade_label = tk.Label(
    result_frame,
    text="",
    font=("Arial", 15, "bold"),
    bg="white",
    fg="green"
)
grade_label.pack(pady=15)

def show_result():

    quiz_frame.pack_forget()

    result_frame.pack(fill="both", expand=True)

    percentage = (score / len(questions)) * 100

    result_label.config(
        text=f"Student Name: {student_name}\n\n"
             f"Total Questions: {len(questions)}\n"
             f"Correct Answers: {score}\n"
             f"Wrong Answers: {len(questions) - score}\n"
             f"Final Score: {score}/{len(questions)}\n"
             f"Percentage: {percentage:.0f}%"
    )

    if percentage >= 80:
        grade_label.config(text="Excellent Performance!")
    elif percentage >= 60:
        grade_label.config(text="Good Performance!")
    elif percentage >= 40:
        grade_label.config(text="Average Performance!")
    else:
        grade_label.config(text="Need More Practice!")

# =================================
# 12. RESTART QUIZ FUNCTION
# =================================

def restart_quiz():

    global current_question, score, student_name

    current_question = 0
    score = 0
    student_name = ""

    selected_answer.set("")
    name_entry.delete(0, tk.END)

    result_frame.pack_forget()
    welcome_frame.pack(fill="both", expand=True)

# =================================
# 13. BUTTONS
# =================================

start_button = tk.Button(
    welcome_frame,
    text="START QUIZ",
    font=("Arial", 13, "bold"),
    bg="#2874A6",
    fg="white",
    width=18,
    command=start_quiz
)
start_button.pack(pady=25)

next_button = tk.Button(
    quiz_frame,
    text="Next Question",
    font=("Arial", 13, "bold"),
    bg="#2874A6",
    fg="white",
    width=18,
    command=next_question
)
next_button.pack(pady=25)

restart_button = tk.Button(
    result_frame,
    text="RESTART QUIZ",
    font=("Arial", 13, "bold"),
    bg="#2874A6",
    fg="white",
    width=18,
    command=restart_quiz
)
restart_button.pack(pady=25)

# =================================
# 14. RUN APPLICATION
# =================================

root.mainloop()
