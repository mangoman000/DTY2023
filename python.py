import tkinter as tk
import random

class Calculator:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Calculator")

        # Create an entry field for input and display
        self.entry = tk.Entry(self.root, width=30)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Generate a random number for the user to reach
        self.random_number = random.randint(1, 1000)

        # Display the target number to the user
        self.random_number_label = tk.Label(self.root, text="Make: " + str(self.random_number))
        self.random_number_label.grid(row=5, column=0, columnspan=4)

        # Initialize labels and buttons for congratulations and play again
        self.congrats_label = None
        self.play_again_button = None

    def button_click(self, number):
        # Append the clicked number to the entry field
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current + str(number))

    def button_clear(self):
        # Clear the entry field
        self.entry.delete(0, tk.END)

    def button_equal(self):
        try:
            # Get the user's answer from the entry field
            user_answer = self.entry.get()
            self.entry.delete(0, tk.END)

            # Check if the user's answer includes an operator
            if '+' in user_answer or '-' in user_answer or '*' in user_answer or '/' in user_answer:
                # Evaluate the user's answer and check if it matches the target number
                result = eval(user_answer)
                if result == self.random_number:
                    # Display congratulations message and play again button
                    self.congrats_label = tk.Label(self.root, text="Congratulations!")
                    self.congrats_label.grid(row=6, column=0, columnspan=4)
                    self.play_again_button = tk.Button(self.root, text="Play Again", padx=20, pady=10, command=self.reset_game)
                    self.play_again_button.grid(row=7, column=0, columnspan=4)
                else:
                    # Display the result in the entry field
                    self.entry.insert(tk.END, result)
            elif user_answer.isdigit() and int(user_answer) == self.random_number:
                # Display an error message if the user's answer is the same as the target number without using operators
                self.entry.insert(tk.END, "Invalid; must use an operator")
            else:
                # Display an error message for any other invalid input
                self.entry.insert(tk.END, "Invalid")

        except Exception:
            # Display an error message if there's an exception during evaluation
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

    def reset_game(self):
        # Reset the game by clearing the entry field and generating a new target number
        self.entry.delete(0, tk.END)
        self.random_number = random.randint(1, 1000)
        self.random_number_label.config(text="Make: " + str(self.random_number))

        # Remove the congratulations message and play again button
        if self.congrats_label:
            self.congrats_label.grid_forget()
        if self.play_again_button:
            self.play_again_button.grid_forget()

    def run(self):
        # Create buttons for numbers 1-9
        for i in range(9):
            button = tk.Button(self.root, text=str(i + 1), padx=20, pady=10, command=lambda i=i: self.button_click(i + 1))
            button.grid(row=(i // 3) + 1, column=i % 3)

        # Create buttons for special characters: +, -, *, /
        operators = ['+', '-', '*', '/']
        for i, operator in enumerate(operators):
            button = tk.Button(self.root, text=operator, padx=20, pady=10, command=lambda operator=operator: self.button_click(operator))
            button.grid(row=i + 1, column=3)

        # Create a button for zero
        button_zero = tk.Button(self.root, text='0', padx=20, pady=10, command=lambda: self.button_click(0))
        button_zero.grid(row=4, column=1)

        # Create a button to clear the entry field
        button_clear = tk.Button(self.root, text='C', padx=20, pady=10, command=self.button_clear)
        button_clear.grid(row=4, column=0)

        # Create a button to perform the calculation
        button_equal = tk.Button(self.root, text='=', padx=20, pady=10, command=self.button_equal)
        button_equal.grid(row=4, column=2)

        # Start the GUI main loop
        self.root.mainloop()

if __name__ == "__main__":
    calculator = Calculator()
    # Run the calculator program
    calculator.run()
