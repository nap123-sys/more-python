import tkinter as tk
from tkinter import messagebox

def submit_job():
    job_title = title_entry.get()
    job_description = description_entry.get("1.0", tk.END)
    if job_title and job_description.strip():
        messagebox.showinfo("Job Submitted", f"Job Title: {job_title}\nDescription: {job_description}")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.")

root = tk.Tk()
root.title("Job Listing")

tk.Label(root, text="Job Title").grid(row=0, column=0, padx=10, pady=10)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Job Description").grid(row=1, column=0, padx=10, pady=10)
description_entry = tk.Text(root, height=10, width=30)
description_entry.grid(row=1, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_job)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
# oh nvm