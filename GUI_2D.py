#------------------------------------------------------------------------------------------------------------------#
# Name : Suhas Adiga
# Project : Toy model to explain Cooper pair formation in superconductors  
# Code : GUI Integration - 2D System with Dropdowns
# Date : 17-11-2024
#------------------------------------------------------------------------------------------------------------------#

# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#------------------------------------------------------------------------------------------------------------------#
# Declaring Global constants
k = 8.99e9
e = -1.6e-19

#------------------------------------------------------------------------------------------------------------------#
# Function to generate position of lattice points

def generate_positions(m, a, x):
    if m == 3:
        positions = {
            "A": (a, 0),
            "B": (0, 0),
            "L1": (-a / 2, a / 2),
            "L2": (-a / 2, -a / 2),
            "L3": (a - x / np.sqrt(2), x / np.sqrt(2)),
            "L4": (a - x / np.sqrt(2), -x / np.sqrt(2)),
            "L5": (a + x / np.sqrt(2), x / np.sqrt(2)),
            "L6": (a + x / np.sqrt(2), -x / np.sqrt(2)),
        }
    else:
        positions = {
            "A": (a, 0),
            "B": (-a, 0),
            "L1": (-a / 2, a / 2),
            "L2": (-a / 2, -a / 2),
            "L3": (a - x / np.sqrt(2), x / np.sqrt(2)),
            "L4": (a - x / np.sqrt(2), -x / np.sqrt(2)),
            "L5": (a + x / np.sqrt(2), x / np.sqrt(2)),
            "L6": (a + x / np.sqrt(2), -x / np.sqrt(2)),
        }
    for i in range(1, m):
        positions[f"L7_m{i}"] = (-a * (2 * i - 1) / 2, a / 2)
        positions[f"L8_m{i}"] = (-a * (2 * i - 1) / 2, -a / 2)

    return positions
#------------------------------------------------------------------------------------------------------------------#
# Function to plot the graph 

def graph_plot():
    m = int(selected_m.get())  
    a = float(selected_a.get())*1e-9  
    λ = float(selected_lambda.get())*1e-9  
    n = int(entry_N.get())  

    x = λ 

    # Calculating forces
    def calculate_force(N):
        Fleft = sum(
            ((2 * k * N * e**2) * ((2 * i - 1) * a) / 2)
            / (((((2 * i - 1) * a) / 2)**2 + (a / 2)**2)**(3 / 2))
            for i in range(1, int((m + 3) / 2))
        )
        Fright = sum(
            ((2 * k * N * e**2) * ((2 * i - 1) * a) / 2)
            / (((((2 * i - 1) * a) / 2)**2 + (a / 2)**2)**(3 / 2))
            for i in range(1, int((m - 1) / 2))
        )
        Fee = (k * e**2) / (((m - 1) * a) / 2)**2

        def f(x):
            return -1 * (
                -Fleft
                + Fright
                + (2 * k * N * e**2)
                / ((((m - 1) * a) / 2 + (x / np.sqrt(2)))**2 + (x / np.sqrt(2))**2)**(3 / 2)
                * (((m - 1) * a) / 2 + (x / np.sqrt(2)))
                + (2 * k * N * e**2)
                / ((((m - 1) * a) / 2 - (x / np.sqrt(2)))**2 + (x / np.sqrt(2))**2)**(3 / 2)
                * (((m - 1) * a) / 2 - (x / np.sqrt(2)))
                - Fee
            )
        return f

    positions = generate_positions(m, a, x)
    plt.figure(fig1.number)
    plt.clf()
    for label, (x_pos, y_pos) in positions.items():
        if label in ['A', 'B']:
            plt.plot(x_pos, y_pos, 'ko', markersize=4)  # Black dots for "A" and "B"
        else:
            color = 'magenta' if "7" in label or "8" in label else 'blue' if "1" in label or "2" else 'green' if "5" in label or "6" else 'red'
            plt.plot(x_pos, y_pos, 'o', color=color, markersize=10)
    plt.axis('off')
    plt.title(f"Distorted {m}x1 Unit Cell Lattice (2-D)", fontweight='bold', fontsize=15, color='red')
    canvas1.draw()

    plt.figure(fig2.number)
    plt.clf()
    x_vals = np.linspace(0.01 * a, 0.75*a, 1000)
    colors = ['limegreen', 'blue', 'darkgreen', 'red']
    for i in range(4):
        N_current = n + i
        force_func = calculate_force(N_current)
        plt.plot(x_vals, force_func(x_vals), color=colors[i % len(colors)], label=f'N={N_current}')
    plt.axhline(0, color='grey', linestyle='--')
    plt.legend()
    plt.title('$F_{res}$ vs (x/a) (2-D)', fontsize=15)
    plt.ylabel('$F_{res}$', fontsize=16)
    plt.xlabel('x/a', fontsize=16)
    plt.yticks([])
    canvas2.draw()

    force_func = calculate_force(n)  
    result_value = force_func(x) 
    result_label.config(text=f"The net resultant force on electron - A is: {result_value:.2e} Newton")



#------------------------------------------------------------------------------------------------------------------#

# GUI setup
root = tk.Tk()
root.title('Toy Model to Explain Cooper Pair Formation in Superconductors (2D)')
root.geometry("1600x1200")

# Input Frame
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Dropdown options
m_options = [3, 5, 7, 9, 11, 13, 15]
a_options = [1.0]
lambda_options = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.707]

selected_m = tk.StringVar(value=m_options[0])
selected_a = tk.StringVar(value=a_options[0])
selected_lambda = tk.StringVar(value=lambda_options[0])

# Inputs
tk.Label(input_frame, text='Number of Unit Cells (m):', font=("helv15", 14)).grid(row=0, column=0, sticky='w')
tk.OptionMenu(input_frame, selected_m, *m_options).grid(row=0, column=1)

tk.Label(input_frame, text='Lattice Parameter (a) (in nm):', font=("helv15", 14)).grid(row=1, column=0, sticky='w')
tk.OptionMenu(input_frame, selected_a, *a_options).grid(row=1, column=1)

tk.Label(input_frame, text='λ = x/a :', font=("helv15", 14)).grid(row=2, column=0, sticky='w')
tk.OptionMenu(input_frame, selected_lambda, *lambda_options).grid(row=2, column=1)

tk.Label(input_frame, text='Atomic Number (N):', font=("helv15", 14)).grid(row=3, column=0, sticky='w')
entry_N = tk.Entry(input_frame, font=("helv15", 14))
entry_N.grid(row=3, column=1)

tk.Button(input_frame, text='Plot', command=graph_plot, font=("Arial", 12), bg='blue', fg='white').grid(row=4, columnspan=2)

result_label = tk.Label(input_frame, text="Result:", font=("helv15", 16))
result_label.grid(row=5, columnspan=2, pady=10)

note_label = tk.Label(input_frame, text="Note: The region below the dotted line represents Attractive Force and above represents Repulsive Force.", font=("helv15", 16))
note_label.grid(row=6, columnspan=2, pady=10)

# Figures
fig1 = plt.figure(figsize=(8, 6))
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

fig2 = plt.figure(figsize=(8, 6))
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

root.mainloop()

#------------------------------------------------------------------------------------------------------------------#
