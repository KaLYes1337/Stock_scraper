import os
import csv
import tkinter as tk
from tkinter import messagebox

working_dir=r"c:\Users\snowb\OneDrive\Desktop\Testing_Programs\WebScraper"
os.chdir(working_dir)
# Function to read stock prices from CSV file
def read_stock_prices_from_csv(filename):
    stock_data = {}

    print(f"Current working directory: {os.getcwd()}")  # Print current working directory
    print(f"Attempting to open file: {filename}")  # Debugging filename

    try:
        with open(filename, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                ticker, price = row
                stock_data[ticker] = price
        return stock_data
    except FileNotFoundError:
        messagebox.showerror("Error", f"File {filename} not found.")
        return {}
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return {}

# Function to fetch stock prices from the CSV and display in the UI
def display_stock_prices_from_csv():
    filename = entry.get()  # Get the file name from user input
    stock_prices = read_stock_prices_from_csv(filename)

    result_text.delete(1.0, tk.END)  # Clear previous results
    if stock_prices:
        for ticker, price in stock_prices.items():
            result_text.insert(tk.END, f"{ticker}: {price}\n")

# Basic UI setup using tkinter
root = tk.Tk()
root.title("Stock Price Viewer from CSV")

# Input field for the CSV file name
label = tk.Label(root, text="Enter CSV file name (with .csv extension):")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Button to fetch stock prices from CSV
fetch_button = tk.Button(root, text="Fetch Prices", command=display_stock_prices_from_csv)
fetch_button.pack(pady=10)

# Text area to display stock prices
result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=5)

# Run the tkinter main loop
root.mainloop()
