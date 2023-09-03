import tkinter as tk
from tkinter import messagebox

class MultipleChoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Choice Question App")

        self.question_label = tk.Label(root, text="What is the capital of France?")
        self.question_label.pack()

        self.choices = ["Paris", "Berlin", "London", "Rome"]

        self.selected_choice = tk.StringVar()
        for choice in self.choices:
            choice_radio = tk.Radiobutton(root, text=choice, variable=self.selected_choice, value=choice)
            choice_radio.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        correct_answer = "Paris"
        user_answer = self.selected_choice.get()

        if user_answer == correct_answer:
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer is {correct_answer}.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MultipleChoiceApp(root)
    root.mainloop()