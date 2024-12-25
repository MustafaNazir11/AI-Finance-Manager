from tkinter import *
import pandas as pd
import os
from datetime import datetime
from login import login

categories = ["Food", "Rent", "Shopping", "Utilities", "Transport", "Others"]
df_transaction = pd.DataFrame(columns=categories)

def register(root):
    """Sets up the registration page."""

    def handle_registration():
        """Handles user registration logic."""
        global username
        user_name = entry_name.get()
        user_email = entry_email.get()
        user_password = entry_password.get()

        global username
        username = user_email.split("@")[0]

        new_data = pd.DataFrame({
            "timestamp": [datetime.now().strftime("%d|%m|%Y %H:%M:%S")],
            "name": [user_name],
            "email": [user_email],
            "password": [user_password]
        })

        if os.path.exists("register.csv"):
            new_data.to_csv('register.csv', mode='a', index=False, header=False)
        else:
            new_data.to_csv('register.csv', mode='w', index=False, header=True)

      
        label_output.config(
            text=f"User registered successfully! Your username is '{username}'", fg="#006400"
        )

        login(root)

    
    for widget in root.winfo_children():
        widget.destroy()

    
    root.configure(bg="#f0f0f0")

    
    Label(
        root,
        text="Register User",
        font=("Helvetica", 22, "bold"),
        fg="#000080",
        bg="#f0f0f0"
    ).pack(pady=30)

    Label(
        root,
        text="Name:",
        font=("Helvetica", 14),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=10)
    entry_name = Entry(root, width=40, font=("Helvetica", 14))
    entry_name.pack()

    Label(
        root,
        text="Email:",
        font=("Helvetica", 14),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=10)
    entry_email = Entry(root, width=40, font=("Helvetica", 14))
    entry_email.pack()

    Label(
        root,
        text="Password:",
        font=("Helvetica", 14),
        fg="#404040",
        bg="#f0f0f0"
    ).pack(pady=10)
    entry_password = Entry(root, width=40, show="*", font=("Helvetica", 14))
    entry_password.pack()

    Button(
        root,
        text="Register",
        command=handle_registration,
        fg="white",
        bg="#004080",
        font=("Helvetica", 14, "bold"),
        width=12,
        height=1,
        relief="raised",
        bd=4
    ).pack(pady=25)

    
    global label_output
    label_output = Label(
        root,
        text="",
        fg="#8B0000",
        font=("Helvetica", 14),
        bg="#f0f0f0"
    )
    label_output.pack()
