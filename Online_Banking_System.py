import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class OnlineBankingSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Online Banking System")

        # Initialize variables
        self.users = {'user1': {'password': 'password1', 'balance': 1000}}
        self.transaction_history = []

        # Screen dimensions
        self.SCREEN_WIDTH = 400
        self.SCREEN_HEIGHT = 360

        # Create login frame
        self.login_frame = tk.Frame(self.master)
        self.login_frame.pack()

        # Labels and entries for login
        tk.Label(self.login_frame, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=0, column=1)
        
        tk.Label(self.login_frame, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        # Login button
        tk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, columnspan=2)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username]['password'] == password:
            self.show_account_management(username)
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def show_account_management(self, username):
        self.login_frame.destroy()

        # Create account management frame
        self.account_frame = tk.Frame(self.master)
        self.account_frame.pack()

        # Account balance label
        self.balance_var = tk.StringVar()
        self.balance_var.set(f"Balance: ${self.users[username]['balance']}")
        tk.Label(self.account_frame, text=f"Welcome {username}").grid(row=0, columnspan=2)
        tk.Label(self.account_frame, textvariable=self.balance_var).grid(row=1, columnspan=2)

        # Buttons for account management
        tk.Button(self.account_frame, text="Deposit", command=lambda: self.deposit(username)).grid(row=2, column=0)
        tk.Button(self.account_frame, text="Withdraw", command=lambda: self.withdraw(username)).grid(row=2, column=1)
        tk.Button(self.account_frame, text="Check Balance", command=lambda: self.check_balance(username)).grid(row=3, columnspan=2)
        tk.Button(self.account_frame, text="Transaction History", command=self.show_transaction_history).grid(row=4, columnspan=2)

    def deposit(self, username):
        amount = simpledialog.askfloat("Deposit", "Enter amount to deposit:")
        self.master.geometry(f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}")
        
        if amount is not None and amount > 0:
            self.users[username]['balance'] += amount
            self.transaction_history.append(f"{username} deposited ${amount}")
            self.balance_var.set(f"Balance: ${self.users[username]['balance']}")
            messagebox.showinfo("Success", f"${amount} deposited successfully")
        else:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw(self, username):
        amount = simpledialog.askfloat("Withdraw", "Enter amount to withdraw:")
        self.master.geometry(f"{self.SCREEN_WIDTH}x{self.SCREEN_HEIGHT}")

        if amount is not None and amount > 0:
            if amount <= self.users[username]['balance']:
                self.users[username]['balance'] -= amount
                self.transaction_history.append(f"{username} withdrew ${amount}")
                self.balance_var.set(f"Balance: ${self.users[username]['balance']}")
                messagebox.showinfo("Success", f"${amount} withdrawn successfully")
            else:
                messagebox.showerror("Error", "Insufficient funds")
        else:
            messagebox.showerror("Error", "Invalid amount")

    def check_balance(self, username):
        messagebox.showinfo("Balance", f"Your balance is ${self.users[username]['balance']}")

    def show_transaction_history(self):
        messagebox.showinfo("Transaction History", "\n".join(self.transaction_history))

if __name__ == "__main__":
    root = tk.Tk()
    app = OnlineBankingSystem(root)
    root.geometry("400x360")  # Set the dimensions of the window
    root.mainloop()  
