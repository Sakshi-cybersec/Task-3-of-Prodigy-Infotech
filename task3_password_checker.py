import tkinter as tk
import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) < 6:
        feedback.append("Password too short (min 6 characters).")
    elif len(password) >= 12:
        strength += 2
        feedback.append("Good length.")
    else:
        strength += 1
        feedback.append("Okay length.")

    if re.search(r"[A-Z]", password):
        strength += 1
        feedback.append("Has uppercase letter.")
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
        feedback.append("Has lowercase letter.")
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        strength += 1
        feedback.append("Has a number.")
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[^A-Za-z0-9]", password):
        strength += 1
        feedback.append("Has a special character.")
    else:
        feedback.append("Add at least one special character (!@#...).")

    if strength <= 2:
        status = "Weak"
        color = "red"
    elif strength <= 4:
        status = "Moderate"
        color = "orange"
    else:
        status = "Strong"
        color = "green"

    return status, feedback, color

def on_check():
    password = entry.get()
    status, feedback, color = check_password_strength(password)
    result_label.config(text=f"Strength: {status}", fg=color)
    feedback_text.delete("1.0", tk.END)
    feedback_text.insert(tk.END, "\n".join(feedback))

# GUI
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter Password:").pack(pady=10)
entry = tk.Entry(root, show="*", width=30)
entry.pack()

tk.Button(root, text="Check Strength", command=on_check).pack(pady=10)

result_label = tk.Label(root, text="Strength: ", font=("Arial", 14))
result_label.pack(pady=5)

tk.Label(root, text="Feedback:").pack()
feedback_text = tk.Text(root, height=6, width=45)
feedback_text.pack()

root.mainloop()
