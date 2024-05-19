import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv
import os

# Define the main application class
class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        self.users_data = {}
        self.load_data()

        self.create_widgets()

    def create_widgets(self):
        # Create the input fields and buttons
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=5)
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Height (cm):").grid(row=2, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(self.root)
        self.height_entry.grid(row=2, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.view_data_button = tk.Button(self.root, text="View Historical Data", command=self.view_historical_data)
        self.view_data_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calculate_bmi(self):
        name = self.name_entry.get()
        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get()) / 100  # convert cm to meters
            bmi = weight / (height * height)
            bmi = round(bmi, 2)
            messagebox.showinfo("BMI Result", f"Name: {name}\nBMI: {bmi}")

            self.save_data(name, weight, height * 100, bmi)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

    def save_data(self, name, weight, height, bmi):
        if name not in self.users_data:
            self.users_data[name] = []
        self.users_data[name].append((weight, height, bmi))

        with open('bmi_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, weight, height, bmi])

    def load_data(self):
        if os.path.exists('bmi_data.csv'):
            with open('bmi_data.csv', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, weight, height, bmi = row[0], float(row[1]), float(row[2]), float(row[3])
                    if name not in self.users_data:
                        self.users_data[name] = []
                    self.users_data[name].append((weight, height, bmi))

    def view_historical_data(self):
        if not self.users_data:
            messagebox.showinfo("No Data", "No historical data available.")
            return

        def on_select(event):
            selected_user = listbox.get(listbox.curselection())
            self.plot_data(selected_user)

        window = tk.Toplevel(self.root)
        window.title("Select User")
        listbox = tk.Listbox(window)
        listbox.pack(padx=10, pady=10)
        for user in self.users_data:
            listbox.insert(tk.END, user)
        listbox.bind("<<ListboxSelect>>", on_select)

    def plot_data(self, user):
        dates = range(1, len(self.users_data[user]) + 1)
        bmis = [data[2] for data in self.users_data[user]]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, bmis, marker='o')
        plt.title(f'BMI Trend for {user}')
        plt.xlabel('Entry Number')
        plt.ylabel('BMI')
        plt.grid(True)
        plt.show()

# Initialize and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
